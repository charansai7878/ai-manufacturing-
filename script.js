// ════════════════════════════════════════════════════════════════
//  CONFIG — Backend API URL
// ════════════════════════════════════════════════════════════════

const API_URL = "https://ai-manufacturing.onrender.com";

// ════════════════════════════════════════════════════════════════
//  GLOBAL STATE
// ════════════════════════════════════════════════════════════════

var domains = {};
var investments = {};
var dataHub = {};
var selection = { investment: null, domain: null, business: null };

// ════════════════════════════════════════════════════════════════
//  INIT — Fetch all data from backend on page load
// ════════════════════════════════════════════════════════════════

document.addEventListener('DOMContentLoaded', async () => {
  await loadUser();
  await loadAllData();
  fetchSummary();
});

async function loadUser() {
  try {
    const res = await fetch(`${API_URL}/api/user`, { credentials: 'include' });
    if (!res.ok) return;
    const user = await res.json();
    document.getElementById('username').innerText = user.fullname || 'OPERATOR';
  } catch (e) {
    console.error("Failed to load user", e);
  }
}

async function loadAllData() {
  try {
    const [domRes, invRes, hubRes] = await Promise.all([
      fetch(`${API_URL}/api/domains`, { credentials: 'include' }),
      fetch(`${API_URL}/api/investments`, { credentials: 'include' }),
      fetch(`${API_URL}/api/data-hub`, { credentials: 'include' })
    ]);
    domains = await domRes.json();
    investments = await invRes.json();
    dataHub = await hubRes.json();
    renderDomainGrid();
  } catch (e) {
    console.error("Failed to load data", e);
  }
}

function renderDomainGrid() {
  const container = document.getElementById('domain-grid');
  if (!container) return;
  container.innerHTML = '';
  Object.entries(domains).forEach(([key, d]) => {
    const div = document.createElement('div');
    div.className = 'domain-btn';
    div.onclick = () => showStage('stage3', key);
    div.innerHTML = `
      <div style="font-size: 1.4rem; margin-bottom: 8px;">${d.icon}</div>
      <div class="mono" style="font-size: 0.7rem; font-weight: 700;">${d.title.toUpperCase()}</div>
    `;
    container.appendChild(div);
  });
}

// ════════════════════════════════════════════════════════════════
//  NAVIGATION & FLOW
// ════════════════════════════════════════════════════════════════

function showStage(stageId, dataKey = null) {
  document.querySelectorAll('section').forEach(s => s.classList.add('hidden'));
  const target = document.getElementById(stageId);
  target.classList.remove('hidden');
  target.scrollIntoView({ behavior: 'smooth' });

  if (stageId === 'stage2' && dataKey) {
    renderInvestmentLevel(dataKey);
  } else if (stageId === 'stage3' && dataKey) {
    renderDomain(dataKey);
  } else if (stageId === 'stage4') {
    renderBusinessTypes();
  } else if (stageId === 'stage5') {
    renderOperationalDetails();
  } else if (stageId === 'stage7') {
    fetchAIAnalytics();
  } else if (stageId === 'stage8') {
    filterDataHub();
  } else if (stageId === 'stage9') {
    initROICalculator();
  }
}

async function runSimulation() {
  const idea = document.getElementById('sim-idea').value.trim();
  const investment = document.getElementById('sim-investment').value;
  const currency = document.getElementById('sim-currency').value;

  if (!idea) { alert("Please specify a business concept for simulation."); return; }

  const btn = event.target;
  const originalText = btn.innerText;
  btn.innerText = "SIMULATING...";
  btn.disabled = true;

  try {
    const res = await fetch(`${API_URL}/api/simulate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: 'include',
      body: JSON.stringify({ idea, investment, currency })
    });
    const data = await res.json();
    if (data.error) throw new Error(data.error);

    document.getElementById('sim-res-revenue').innerText = data.revenue;
    document.getElementById('sim-res-breakeven').innerText = data.breakeven;
    document.getElementById('sim-res-viability').innerText = data.viability;
    document.getElementById('sim-res-plan').innerHTML = data.plan;
    document.getElementById('sim-results').classList.remove('hidden');
    document.getElementById('sim-results').scrollIntoView({ behavior: 'smooth' });
  } catch (e) {
    alert("Simulation calibration failed. Check console for details.");
    console.error(e);
  } finally {
    btn.innerText = originalText;
    btn.disabled = false;
  }
}

function transferToCopilot() {
  const plan = document.getElementById('sim-res-plan').innerText;
  const widget = document.getElementById('ai-chat-widget');
  if (!widget.classList.contains('active')) toggleChat();
  const input = document.getElementById('chat-input');
  input.value = `Discuss this simulated plan: ${plan.substring(0, 500)}...`;
  sendChatMessage();
}

function initROICalculator() {
  const biz = selection.business;
  if (!biz) return;
  document.getElementById('roi-input-cost').value = biz.startup_cost;
  document.getElementById('roi-input-revenue').value = biz.monthly_revenue;
  document.getElementById('roi-input-opex').value = biz.monthly_expense;
  calculateROI();
}

function calculateROI() {
  const cost = parseFloat(document.getElementById('roi-input-cost').value) || 0;
  const rev = parseFloat(document.getElementById('roi-input-revenue').value) || 0;
  const opex = parseFloat(document.getElementById('roi-input-opex').value) || 0;

  const monthlyProfit = rev - opex;
  const annualYield = monthlyProfit * 12;
  const breakeven = monthlyProfit > 0 ? (cost / monthlyProfit).toFixed(1) : "∞";

  document.getElementById('roi-net-profit').innerText = `₹${monthlyProfit.toLocaleString()}`;
  document.getElementById('roi-annual-yield').innerText = `₹${annualYield.toLocaleString()}`;
  document.getElementById('roi-breakeven').innerText = breakeven + " MONTHS";

  const advisoryEl = document.getElementById('roi-advisory');
  if (breakeven === "∞" || monthlyProfit <= 0) {
    advisoryEl.innerText = "[CRITICAL] NEGATIVE MARGIN DETECTED. OPERATIONAL COSTS EXCEED REVENUE. ANALYZE SUPPLY CHAIN EFFICIENCY.";
    advisoryEl.style.color = "var(--red)";
  } else if (breakeven < 12) {
    advisoryEl.innerText = "[OPTIMAL] HIGH-VELOCITY ROI DETECTED. BREAK-EVEN WITHIN 12 MONTHS. RECOMMEND IMMEDIATE SCALE-UP.";
    advisoryEl.style.color = "var(--green)";
  } else if (breakeven < 24) {
    advisoryEl.innerText = "[STABLE] STANDARD INDUSTRIAL RECOVERY CYCLE. PROFITABILITY INDEX WITHIN NOMINAL RANGE.";
    advisoryEl.style.color = "var(--accent)";
  } else {
    advisoryEl.innerText = "[STRATEGIC] LONG-TERM RECOVERY DETECTED. FOCUS ON REDUCING FIXED COSTS AND INCREASING THROUGHPUT.";
    advisoryEl.style.color = "var(--yellow)";
  }
}

function goBackFromStage3() {
  if (selection.investment) showStage('stage2');
  else showStage('stage1');
}

// ════════════════════════════════════════════════════════════════
//  RENDERING LOGIC
// ════════════════════════════════════════════════════════════════

function renderInvestmentLevel(key) {
  const data = investments[key];
  selection.investment = key;
  document.getElementById('inv-title').innerText = data.title;
  document.getElementById('inv-subtitle').innerText = data.description;
  document.getElementById('inv-range').innerText = data.range;
  document.getElementById('inv-auto').innerText = data.automation;
  document.getElementById('inv-roi').innerText = data.roi;
  document.getElementById('inv-ex').innerText = data.examples.join(', ');
}

function renderDomain(key) {
  const data = domains[key];
  selection.domain = key;
  document.getElementById('dom-title').innerText = data.title + " Domain";
  document.getElementById('dom-icon').innerText = data.icon;
  document.getElementById('dom-name').innerText = data.title;
  document.getElementById('dom-overview').innerText = data.overview;
  document.getElementById('dom-market').innerText = data.market_size;

  const methodsList = document.getElementById('dom-methods');
  methodsList.innerHTML = '';
  data.methods.forEach(m => {
    const li = document.createElement('li');
    li.style.background = 'var(--glass)';
    li.style.padding = '8px 15px';
    li.style.borderRadius = '20px';
    li.style.fontSize = '0.8rem';
    li.innerText = m;
    methodsList.appendChild(li);
  });
}

function renderBusinessTypes() {
  const bizList = document.getElementById('biz-list');
  bizList.innerHTML = '';

  if (!selection.domain) {
    bizList.innerHTML = '<p class="stage-subtitle">Please select a domain first.</p>';
    return;
  }

  const domainData = domains[selection.domain];
  domainData.business_types.forEach(biz => {
    const card = document.createElement('div');
    card.className = 'card animate';
    card.onclick = () => { selection.business = biz; showStage('stage5'); };
    card.innerHTML = `
      <div class="card-title">${biz.name}</div>
      <div class="card-info"><span>Investment:</span> <strong>${biz.investment}</strong></div>
      <div class="card-info"><span>Capacity:</span> <strong>${biz.capacity}</strong></div>
      <div class="card-info"><span>Required Skills:</span> <strong>${biz.skills}</strong></div>
      <button class="btn" style="width: 100%; margin-top: 15px; font-size: 0.8rem;">OPERATIONAL BLUEPRINT ➔</button>
    `;
    bizList.appendChild(card);
  });
}

function renderOperationalDetails() {
  const biz = selection.business;
  if (!biz) return;
  document.getElementById('ops-name').innerText = biz.name;

  const matList = document.getElementById('mat-list');
  matList.innerHTML = '';
  biz.materials.forEach(m => {
    const div = document.createElement('div');
    div.className = 'cat-item';
    div.style.padding = '10px 15px';
    div.innerHTML = `<strong>${m}</strong>`;
    matList.appendChild(div);
  });

  const machList = document.getElementById('mach-list');
  machList.innerHTML = '';
  biz.machinery.forEach(m => {
    const div = document.createElement('div');
    div.className = 'cat-item';
    div.style.padding = '10px 15px';
    div.style.borderLeftColor = 'var(--accent)';
    div.innerHTML = `<strong>${m}</strong>`;
    machList.appendChild(div);
  });
}

// ════════════════════════════════════════════════════════════════
//  API INTEGRATION
// ════════════════════════════════════════════════════════════════

async function fetchSummary() {
  try {
    const res = await fetch(`${API_URL}/api/overview`, { credentials: 'include' });
    const data = await res.json();
    document.getElementById('sum-biz').innerText = data.total_business_types;
    document.getElementById('sum-mach').innerText = data.machine_categories;
    document.getElementById('sum-mat').innerText = data.raw_material_categories;
    document.getElementById('sum-growth').innerText = data.industry_growth;
  } catch (e) {
    console.error("Summary fetch failed", e);
  }
}

async function fetchAIAnalytics() {
  const biz = selection.business;
  if (!biz) return;
  try {
    const res = await fetch(`${API_URL}/api/analytics/${biz.id}`, { credentials: 'include' });
    const data = await res.json();
    const a = data.analytics;

    document.getElementById('ai-health').innerText = a.machine_health + '%';
    document.getElementById('ai-risk').innerText = a.failure_risk;
    document.getElementById('ai-eff').innerText = a.production_efficiency;
    document.getElementById('ai-mat').innerText = data.domain + " baseline: " + a.material_consumption + " efficiency.";
    document.getElementById('ai-maint').innerText = a.maintenance;
    document.getElementById('ai-cost').innerText = a.cost_optimization;

    const healthVal = document.getElementById('ai-health');
    if (a.machine_health > 90) healthVal.style.color = 'var(--green)';
    else if (a.machine_health > 70) healthVal.style.color = 'var(--yellow)';
    else healthVal.style.color = 'var(--red)';
  } catch (e) {
    console.error("Analytics fetch failed", e);
  }
}

// ════════════════════════════════════════════════════════════════
//  INDUSTRY DATA HUB LOGIC
// ════════════════════════════════════════════════════════════════

function filterDataHub() {
  const domain = document.getElementById('hub-filter-domain').value;
  const freq = document.getElementById('hub-filter-freq').value;
  const type = document.getElementById('hub-filter-type').value;

  ['monthly', 'quarterly', 'yearly'].forEach(f => {
    const listEl = document.getElementById(`hub-${f}-list`);
    const sectionEl = document.getElementById(`hub-${f}`);

    if (!dataHub[f]) { sectionEl.classList.add('hidden'); return; }

    let filtered = dataHub[f].filter(item => {
      const matchDomain = domain === 'All' || item.domains.includes('All') || item.domains.includes(domain);
      const matchFreq = freq === 'All' || f === freq;
      const matchType = type === 'All' || item.data_type === type;
      return matchDomain && matchFreq && matchType;
    });

    if (filtered.length > 0 && (freq === 'All' || f === freq)) {
      sectionEl.classList.remove('hidden');
      renderHubSection(listEl, filtered);
    } else {
      sectionEl.classList.add('hidden');
    }
  });
}

function renderHubSection(container, data) {
  container.innerHTML = '';
  data.forEach(item => {
    const card = document.createElement('div');
    card.className = 'card animate';
    card.style.cssText = 'display:flex; flex-direction:column; gap:10px;';
    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 10px;">
        <div class="card-title mono" style="font-size: 0.9rem; margin-bottom: 0; color: var(--accent);">${item.title}</div>
        <span class="mono" style="font-size: 0.6rem; padding: 4px 8px; background: rgba(94,250,242,0.1); border-radius: 4px; color: var(--accent); border: 1px solid var(--border); white-space: nowrap;">${item.data_type.toUpperCase()}</span>
      </div>
      <p style="font-size: 0.8rem; color: var(--text-dim); line-height: 1.5; margin-top: 10px;">${item.description}</p>
      <div style="margin-top: 15px;">
        <div class="mono" style="font-size: 0.65rem; color: var(--accent); font-weight: 700; letter-spacing: 1px;">[SOURCE PROTOCOL]</div>
        <div class="mono" style="font-size: 0.75rem; margin-top: 4px; color: #fff;">${item.source}</div>
      </div>
      <div style="margin-top: 15px;">
        <div class="mono" style="font-size: 0.65rem; color: var(--green); font-weight: 700; letter-spacing: 1px;">[USE CASE MODULES]</div>
        <ul style="font-size: 0.75rem; padding-left: 15px; margin-top: 8px; color: var(--text-dim); line-height: 1.6;">
          ${item.use_cases.map(uc => `<li>${uc}</li>`).join('')}
        </ul>
      </div>
      <button class="btn" style="width: 100%; margin-top: auto; font-size: 0.7rem; padding: 10px; border-radius: 4px;">SYNCHRONIZE DATASET ➔</button>
    `;
    container.appendChild(card);
  });
}

// ════════════════════════════════════════════════════════════════
//  AI COPILOT CHAT LOGIC
// ════════════════════════════════════════════════════════════════

function toggleChat() {
  const widget = document.getElementById('ai-chat-widget');
  widget.classList.toggle('active');
  if (widget.classList.contains('active')) document.getElementById('chat-input').focus();
}

async function sendChatMessage() {
  const input = document.getElementById('chat-input');
  const container = document.getElementById('chat-messages');
  const msg = input.value.trim();
  if (!msg) return;

  const userDiv = document.createElement('div');
  userDiv.className = 'msg user';
  userDiv.innerText = msg;
  container.appendChild(userDiv);
  input.value = '';
  container.scrollTop = container.scrollHeight;

  const context = {
    domain: selection.domain ? domains[selection.domain].title : "General",
    biz_name: selection.business ? selection.business.name : "Manufacturing"
  };

  const botDiv = document.createElement('div');
  botDiv.className = 'msg bot';
  botDiv.innerText = "...";
  container.appendChild(botDiv);
  container.scrollTop = container.scrollHeight;

  try {
    const res = await fetch(`${API_URL}/api/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify({ message: msg, context })
    });
    const data = await res.json();
    botDiv.innerHTML = data.response;
  } catch (e) {
    botDiv.innerText = "Error: Protocol disconnected.";
    console.error(e);
  }
  container.scrollTop = container.scrollHeight;
}
