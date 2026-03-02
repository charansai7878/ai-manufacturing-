
from flask import Flask, render_template, jsonify, request, session, redirect, url_for, flash
import random, math, time, os, hashlib
from datetime import datetime, timedelta
from functools import wraps
from dotenv import load_dotenv
from groq import Groq
from data import INVESTMENT_DATA, DOMAINS_DATA, INDUSTRY_DATA_HUB

from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Groq Client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Initialize Supabase Client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL and SUPABASE_KEY else None

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
app = Flask(__name__,
            template_folder=BASE_DIR,
            static_folder=os.path.join(BASE_DIR, 'static'))
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'manufacturing-overview-secret-2026')

# ════════════════════════════════════════════════════════════════
#  DATABASE HELPERS (Supabase)
# ════════════════════════════════════════════════════════════════

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# ════════════════════════════════════════════════════════════════
#  ROUTES
# ════════════════════════════════════════════════════════════════

@app.route("/login", methods=["GET", "POST"])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        
        if not supabase:
            flash("Database connection error", "error")
            return render_template("login.html")

        # Query Supabase for the user
        response = supabase.table("users").select("*").eq("username", username).execute()
        user = response.data[0] if response.data else None
        
        if user and user["password"] == hash_password(password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["fullname"] = user["fullname"]
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password", "error")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if 'user_id' in session:
        return redirect(url_for('index'))
    if request.method == "POST":
        fullname = request.form.get("fullname", "").strip()
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm  = request.form.get("confirm_password", "")
        if not fullname or not username or not password:
            flash("All fields are required", "error")
        elif password != confirm:
            flash("Passwords do not match", "error")
        else:
            if not supabase:
                flash("Database connection error", "error")
                return render_template("register.html")

            # Check if user already exists
            existing = supabase.table("users").select("id").eq("username", username).execute()
            if existing.data:
                flash("Username already exists", "error")
            else:
                # Insert new user
                data = {
                    "fullname": fullname,
                    "username": username,
                    "password": hash_password(password)
                }
                supabase.table("users").insert(data).execute()
                flash("Account created successfully", "success")
                return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/")
@login_required
def index():
    return render_template("index.html", 
                           domains=DOMAINS_DATA, 
                           investments=INVESTMENT_DATA, 
                           data_hub=INDUSTRY_DATA_HUB)

@app.route("/api/overview")
@login_required
def get_overview():
    total_biz = sum(len(d["business_types"]) for d in DOMAINS_DATA.values())
    machine_cats = set()
    material_cats = set()
    for d in DOMAINS_DATA.values():
        for b in d["business_types"]:
            for m in b["machinery"]: machine_cats.add(m)
            for mat in b["materials"]: material_cats.add(mat)
    
    return jsonify({
        "total_business_types": total_biz,
        "machine_categories": len(machine_cats),
        "raw_material_categories": len(material_cats),
        "industry_growth": "8.5% YoY",
        "domains": DOMAINS_DATA,
        "investments": INVESTMENT_DATA
    })

@app.route("/api/data_hub")
@login_required
def get_data_hub():
    return jsonify(INDUSTRY_DATA_HUB)

@app.route("/api/analytics/<biz_id>")
@login_required
def get_analytics(biz_id):
    # Find the business type in the data
    found_biz = None
    domain_key = None
    for dk, d in DOMAINS_DATA.items():
        for b in d["business_types"]:
            if b["id"] == biz_id:
                found_biz = b
                domain_key = dk
                break
        if found_biz: break
    
    if not found_biz:
        return jsonify({"error": "Business type not found"}), 404
    
    # Generate some mock AI metrics
    health_score = random.randint(85, 98)
    
    # Get LLM strategic advice
    advisory_content = "Strategic advisory pending connection..."
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are an Industrial Strategy AI for 'Industrial Nexus'. Provide 3 concise bullet points of strategic advice for a manufacturing business. Focus on efficiency, cost, and maintenance. Keep it strictly professional and technical. Maximum 15 words per bullet."},
                {"role": "user", "content": f"Provide strategic advice for a '{found_biz['name']}' business in the '{DOMAINS_DATA[domain_key]['title']}' sector. Startup cost: {found_biz.get('startup_cost')}, Capacity: {found_biz['capacity']}."}
            ],
            temperature=0.7,
            max_tokens=150
        )
        advisory_content = completion.choices[0].message.content
    except Exception as e:
        print(f"Groq API Error: {e}")
        advisory_content = "• Optimize supply chain logistics.\n• Implement predictive maintenance.\n• Monitor energy consumption patterns."

    return jsonify({
        "business": found_biz,
        "domain": DOMAINS_DATA[domain_key]["title"],
        "analytics": {
            "machine_health": health_score,
            "failure_risk": "Low" if health_score > 90 else "Medium",
            "production_efficiency": f"{random.randint(88, 96)}%",
            "material_consumption": f"{random.randint(70, 90)}%",
            "maintenance": "Scheduled in 12 days",
            "cost_optimization": advisory_content
        }
    })

@app.route("/api/simulate", methods=["POST"])
@login_required
def simulate_idea():
    data = request.json
    idea = data.get("idea", "")
    investment = data.get("investment", "Unknown")
    currency = data.get("currency", "INR")

    if not idea:
        return jsonify({"error": "No idea provided"}), 400

    try:
        system_prompt = (
            "You are the 'Industrial Nexus Simulation Engine'. Analyze the user's business idea and investment level. "
            "Return a JSON response with exactly 4 keys: 'revenue', 'breakeven', 'viability', and 'plan'. "
            "- 'revenue': Estimated monthly revenue based on investment. "
            "- 'breakeven': Estimated time to recover investment. "
            "- 'viability': One word (High, Medium, or Low). "
            "- 'plan': A concise HTML-formatted list (<ul><li>...</li></ul>) with 4 key steps to start. "
            "Respond ONLY with valid JSON."
        )
        
        user_prompt = f"Idea: {idea}. Investment: {investment} {currency}."
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        
        import json
        sim_data = json.loads(completion.choices[0].message.content)
        return jsonify(sim_data)
        
    except Exception as e:
        print(f"Simulation Error: {e}")
        return jsonify({
            "revenue": "Calibration Error",
            "breakeven": "N/A",
            "viability": "Medium",
            "plan": "<ul><li>Failed to initialize simulation.</li><li>Check API credentials.</li></ul>"
        })

@app.route("/api/chat", methods=["POST"])
@login_required
def chat_copilot():
    user_msg = request.json.get("message", "")
    biz_context = request.json.get("context", {})
    
    if not user_msg:
        return jsonify({"error": "No message provided"}), 400

    try:
        system_prompt = (
            "You are the 'Industrial Nexus AI Copilot'. You assist industrial operators with technical, logistical, and financial advice. "
            "Respond in a helpful, professional, and technical tone. Use bullet points and bold text for clarity. "
            f"Context: Operating in {biz_context.get('domain', 'Industrial')} sector, specifically {biz_context.get('biz_name', 'General Manufacturing')}."
        )
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_msg}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return jsonify({"response": completion.choices[0].message.content})
    except Exception as e:
        print(f"Chat API Error: {e}")
        return jsonify({"response": "I apologize, but I'm having trouble connecting to the intelligence nexus right now. Please try again shortly."})

if __name__ == "__main__":
    app.run(
        debug=os.getenv('DEBUG', 'True').lower() == 'true',
        port=int(os.getenv('PORT', 5000))
    )
