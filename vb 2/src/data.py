
# Manufacturing Overview Data

INVESTMENT_DATA = {
    "low": {
        "title": "Low Investment Manufacturing",
        "color": "green",
        "range": "₹5L - ₹25L",
        "automation": "Manual / Semi-Automatic",
        "roi": "12 - 18 months",
        "examples": ["Bakery", "Small Textile Workshop", "Handmade Soap", "Paper Bags"],
        "description": "Ideal for startups and micro-enterprises. Minimal machinery and low labor requirements."
    },
    "medium": {
        "title": "Medium Investment Manufacturing",
        "color": "yellow",
        "range": "₹25L - ₹2Cr",
        "automation": "Semi-Automatic / Automatic",
        "roi": "18 - 36 months",
        "examples": ["Juice Bottling", "Plastic Injection Molding", "Garment Factory", "Auto Spare Parts"],
        "description": "Standard Industry 4.0 ready setups. Requires skilled labor and specialized machinery."
    },
    "high": {
        "title": "High Investment Manufacturing",
        "color": "red",
        "range": "₹2Cr - ₹50Cr+",
        "automation": "Fully Automated / AI-Driven",
        "roi": "3 - 5 years",
        "examples": ["Steel Plant", "Pharma Formulation", "Automobile Assembly", "Semiconductor Fab"],
        "description": "Large scale industrial operations with global market reach and high-tech integration."
    }
}

DOMAINS_DATA = {
    "food": {
        "title": "Food Processing",
        "icon": "🍎",
        "overview": "Converting raw agricultural products into food or into other forms.",
        "market_size": "$4.5 Trillion Global",
        "methods": ["Dehydration", "Canning", "Freezing", "Fermentation"],
        "business_types": [
            {
                "id": "juice_bottling",
                "name": "Fruit Juice Bottling",
                "investment": "Medium",
                "capacity": "5000 units/day",
                "skills": "Quality Control, Machine Operation",
                "materials": ["Fruit Pulp", "Sugar", "Preservatives", "PET Bottles", "Labels"],
                "machinery": ["Washing Unit", "Pulper", "Pasteurizer", "Filling Machine", "Labeling Machine"],
                "startup_cost": 4500000,
                "monthly_revenue": 1200000,
                "monthly_expense": 850000
            },
            {
                "id": "bakery_industrial",
                "name": "Industrial Bakery",
                "investment": "Low to Medium",
                "capacity": "2000 loaves/day",
                "skills": "Food Science, Logistics",
                "materials": ["Flour", "Yeast", "Butter", "Packaging Film"],
                "machinery": ["Dough Mixer", "Proofer", "Rotary Oven", "Slicing Machine"],
                "startup_cost": 1500000,
                "monthly_revenue": 600000,
                "monthly_expense": 420000
            }
        ]
    },
    "textile": {
        "title": "Textile & Apparel",
        "icon": "👕",
        "overview": "Design, production, and distribution of yarn, cloth, and clothing.",
        "market_size": "$1.5 Trillion Global",
        "methods": ["Spinning", "Weaving", "Knitting", "Dyeing"],
        "business_types": [
            {
                "id": "yarn_mfg",
                "name": "Yarn Manufacturing",
                "investment": "High",
                "capacity": "10 Tons/day",
                "skills": "Mechanical Engineering, Textile Tech",
                "materials": ["Raw Cotton", "Synthetic Fibers", "Lubricants"],
                "machinery": ["Blow Room", "Carding Machine", "Draw Frame", "Ring Frame"],
                "startup_cost": 25000000,
                "monthly_revenue": 8000000,
                "monthly_expense": 5500000
            },
            {
                "id": "garment_prod",
                "name": "Garment Production",
                "investment": "Medium",
                "capacity": "1000 pieces/day",
                "skills": "Stitching, Pattern Making",
                "materials": ["Fabric", "Thread", "Buttons/Zippers", "Labels", "Packaging Bags"],
                "machinery": ["Cutting Machine", "Sewing Machine", "Overlock Machine", "Button Hole Machine", "Ironing Station"],
                "startup_cost": 3500000,
                "monthly_revenue": 1500000,
                "monthly_expense": 1100000
            }
        ]
    },
    "automobile": {
        "title": "Automobile & Engineering",
        "icon": "🚗",
        "overview": "Manufacturing of vehicle components and precision engineering parts.",
        "market_size": "$3 Trillion Global",
        "methods": ["Casting", "Forging", "Machining", "Assembly"],
        "business_types": [
            {
                "id": "auto_parts",
                "name": "Brake Pad Manufacturing",
                "investment": "Medium",
                "capacity": "500 sets/day",
                "skills": "Material Science, CNC Operation",
                "materials": ["Steel Plates", "Friction Material", "Adhesives", "Powder Coating"],
                "machinery": ["Mixing Machine", "Hot Press", "Grinding Machine", "Curing Oven"],
                "startup_cost": 8500000,
                "monthly_revenue": 2800000,
                "monthly_expense": 1900000
            }
        ]
    },
    "electronics": {
        "title": "Electronics",
        "icon": "💻",
        "overview": "Assembly and manufacturing of electronic components and consumer gadgets.",
        "market_size": "$2.2 Trillion Global",
        "methods": ["SMT Assembly", "Soldering", "Testing"],
        "business_types": [
            {
                "id": "pcb_assembly",
                "name": "LED Lighting Assembly",
                "investment": "Medium",
                "capacity": "2000 units/day",
                "skills": "Electrical Engineering, SMT Precision",
                "materials": ["PCBs", "LED Chips", "Solder Paste", "Aluminium Housing"],
                "machinery": ["Pick & Place Machine", "Reflow Oven", "Stencil Printer", "Testing Jig"],
                "startup_cost": 5500000,
                "monthly_revenue": 2200000,
                "monthly_expense": 1600000
            }
        ]
    },
    "pharma": {
        "title": "Pharma & Chemicals",
        "icon": "💊",
        "overview": "Discovering, developing, producing, and marketing drugs or pharmaceutical drugs.",
        "market_size": "$1.4 Trillion Global",
        "methods": ["Granulation", "Compression", "Coating", "Packaging"],
        "business_types": [
            {
                "id": "tablet_mfg",
                "name": "Tablet Formulation",
                "investment": "High",
                "capacity": "1 Million tablets/day",
                "skills": "Pharmacy, Lab Analysis",
                "materials": ["APIs", "Excipients", "Coating Polymers", "Blister Foil"],
                "machinery": ["Rapid Mixer Granulator", "Tablet Press", "Coating Machine", "Blister Packing Machine"],
                "startup_cost": 45000000,
                "monthly_revenue": 15000000,
                "monthly_expense": 9500000
            }
        ]
    },
    "plastic": {
        "title": "Plastic & Polymer",
        "icon": "🧪",
        "overview": "Processing of polymer resins into finished plastic products.",
        "market_size": "$600 Billion Global",
        "methods": ["Injection Molding", "Extrusion", "Blow Molding"],
        "business_types": [
            {
                "id": "injection_molding",
                "name": "Plastic Household Items",
                "investment": "Medium",
                "capacity": "5000 units/day",
                "skills": "Mold Design, Polymer Chem",
                "materials": ["PP Granules", "Masterbatch Color", "Recycled Flakes"],
                "machinery": ["Injection Molding Machine", "Cooling Tower", "Granulator", "Molds"],
                "startup_cost": 7500000,
                "monthly_revenue": 2500000,
                "monthly_expense": 1800000
            }
        ]
    },
    "metal": {
        "title": "Metal & Steel",
        "icon": "🏗️",
        "overview": "Processing of iron ore and scrap into steel products and fabrication.",
        "market_size": "$2.5 Trillion Global",
        "methods": ["Rolling", "Galvanizing", "Welding"],
        "business_types": [
            {
                "id": "sheet_metal",
                "name": "Sheet Metal Fabrication",
                "investment": "Medium",
                "capacity": "5 Tons/day",
                "skills": "Welding, CAD Design",
                "materials": ["HR Sheets", "CR Sheets", "Welding Rods", "Zinc Paint"],
                "machinery": ["Shearing Machine", "Bending Machine", "Punching Press", "Arcon Welding Machine"],
                "startup_cost": 6500000,
                "monthly_revenue": 2000000,
                "monthly_expense": 1450000
            }
        ]
    },
    "fmcg": {
        "title": "FMCG",
        "icon": "🧼",
        "overview": "Fast-moving consumer goods that are sold quickly and at a relatively low cost.",
        "market_size": "$10 Trillion Global",
        "methods": ["Mixing", "Extrusion", "Packaging"],
        "business_types": [
            {
                "id": "soap_mfg",
                "name": "Soap Manufacturing",
                "investment": "Low to Medium",
                "capacity": "3000 bars/day",
                "skills": "Chemical Mixing, Branding",
                "materials": ["Soap Noodles", "Fragrance", "Colorant", "Wrapping Paper"],
                "machinery": ["Sigma Mixer", "Plodder", "Cutting Machine", "Stamping Machine"],
                "startup_cost": 2500000,
                "monthly_revenue": 900000,
                "monthly_expense": 650000
            }
        ]
    },
    "smart_mfg": {
        "title": "Smart Manufacturing / AI",
        "icon": "🤖",
        "overview": "Using IoT and AI to optimize manufacturing processes and efficiency.",
        "market_size": "$400 Billion Global",
        "methods": ["Data Acquisition", "Predictive Analytics", "Robotic Automation"],
        "business_types": [
            {
                "id": "iot_sensors",
                "name": "IoT Sensor Nodes",
                "investment": "Medium",
                "capacity": "500 units/day",
                "skills": "Embedded Systems, AI Algorithms",
                "materials": ["Microcontrollers", "Sensors", "Plastic Casing", "Batteries"],
                "machinery": ["PCB Assembly Line", "3D Printers", "Electronic Calibration Bench"],
                "startup_cost": 5000000,
                "monthly_revenue": 2000000,
                "monthly_expense": 1400000
            }
        ]
    }
}

INDUSTRY_DATA_HUB = {
    "monthly": [
        {
            "id": "production_output",
            "title": "Monthly Production Output",
            "description": "Real-time production volume, IIP indices, and sector-wise output tracking.",
            "source": "MOSPI / Central Statistical Office",
            "use_cases": ["👉 Efficiency analysis", "👉 Manufacturing growth tracking"],
            "data_type": "Production",
            "domains": ["All"]
        },
        {
            "id": "commodity_prices",
            "title": "Material Prices & Consumption",
            "description": "Price indices for steel, chemicals, textiles, and monthly consumption levels.",
            "source": "Commodity Exchanges (MCX, LME) / Industry Panels",
            "use_cases": ["👉 Cost forecasting", "👉 Supply chain management"],
            "data_type": "Raw Materials",
            "domains": ["Metal", "Textile", "Pharma & Chemicals"]
        },
        {
            "id": "pmi_sentiment",
            "title": "Manufacturing PMI & Sentiment",
            "description": "Purchasing Managers' Index and business outlook surveys.",
            "source": "S&P Global / Industrial Surveys",
            "use_cases": ["👉 Supply chain monitoring", "👉 Investment planning"],
            "data_type": "Investment",
            "domains": ["All"]
        },
        {
            "id": "logistics_tracker",
            "title": "Logistics & Delivery Timelines",
            "description": "Freight rates, port congestion indices, and average delivery timelines.",
            "source": "Logistics Data Bank (LDB) / Export Port data",
            "use_cases": ["👉 Supply chain & Logistics tracking", "👉 Inventory turnover optimization"],
            "data_type": "Supply Chain & Logistics",
            "domains": ["All"]
        }
    ],
    "quarterly": [
        {
            "id": "capital_investment",
            "title": "Capital Investment & FDI Data",
            "description": "Quarterly investment trends, FDI inflows, and new project announcements.",
            "source": "DPIIT / RBI Capital Investment Surveys",
            "use_cases": ["👉 Business planning", "👉 ROI analysis"],
            "data_type": "Investment",
            "domains": ["All"]
        },
        {
            "id": "financial_performance",
            "title": "Financial Performance Data",
            "description": "Quarterly financials, profit margins, and operational cost trends.",
            "source": "Stock Exchange Filings (NSE/BSE)",
            "use_cases": ["👉 Business benchmarking", "👉 Cost optimization analysis"],
            "data_type": "Financial Performance",
            "domains": ["All"]
        },
        {
            "id": "capacity_utilization",
            "title": "Factory Utilization & Machine Health",
            "description": "Tracking installed capacity vs actual production and machine performance logs.",
            "source": "RBI / Industry-wide Machine IoT Panels",
            "use_cases": ["👉 Machine health monitoring", "👉 Predictive maintenance"],
            "data_type": "Machinery & Equipment",
            "domains": ["Heavy Machinery", "Automobile", "Metal"]
        },
        {
            "id": "quality_maintenance",
            "title": "Quality & Maintenance Metrics",
            "description": "Industry average defect rates, downtime statistics, and maintenance schedules.",
            "source": "Quality Council of India / Industry benchmarks",
            "use_cases": ["👉 Quality & Maintenance analysis", "👉 Downtime reduction planning"],
            "data_type": "Quality & Maintenance",
            "domains": ["All"]
        }
    ],
    "yearly": [
        {
            "id": "annual_growth",
            "title": "Annual Sectoral Growth & ASI",
            "description": "Yearly manufacturing sector growth rates and Annual Survey of Industries data.",
            "source": "MOSPI / World Bank Industrial reports",
            "use_cases": ["👉 Strategic planning", "👉 Long-term forecasting"],
            "data_type": "Production",
            "domains": ["All"]
        },
        {
            "id": "tech_automation",
            "title": "Automation & Technology Adoption",
            "description": "Yearly report on robotic automation levels and technology adoption trends.",
            "source": "Global Tech Consultants / IFRA",
            "use_cases": ["👉 Market expansion decisions", "👉 Technology benchmarking"],
            "data_type": "Machinery & Equipment",
            "domains": ["Smart Manufacturing / AI", "Electronics"]
        },
        {
            "id": "export_import_yearly",
            "title": "Supply Chain & Export/Import Yearly",
            "description": "Comprehensive yearly summary of trade balance and global supply chain shifts.",
            "source": "Ministry of Commerce / WTO",
            "use_cases": ["👉 Strategic Supply Chain planning", "👉 Global market entry"],
            "data_type": "Supply Chain & Logistics",
            "domains": ["All"]
        }
    ]
}
