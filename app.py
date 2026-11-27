import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Guma Adolf | NG Advisory Co. Platform",
    page_icon="📊",
    layout="wide",
)

# Custom CSS for SaaS Dark Theme Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f3f4f6;
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1.2;
        margin-bottom: 20px;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        color: #9ca3af;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #38bdf8;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

GITHUB_TRAFFIC_SUMMARY_URL = (
    "https://raw.githubusercontent.com/gumaadolfda-blip/dubai-traffic-incidents-analysis/main/"
    "Dubai_Traffic_Incident_Executive_Summary.jpeg"
)
GITHUB_NETZERO_SUMMARY_URL = (
    "https://raw.githubusercontent.com/gumaadolfda-blip/uae-netzero-freight-ai/main/"
    "UAE_NetZero_Executive_Summary_Report.jpg"
)
GITHUB_TRAFFIC_REPO_URL = "https://github.com/gumaadolfda-blip/dubai-traffic-incidents-analysis"
GITHUB_NETZERO_REPO_URL = "https://github.com/gumaadolfda-blip/uae-netzero-freight-ai"


def render_image_safe(path: str, caption: str):
    """Render an image cleanly without crashing if a local or remote asset is missing."""
    try:
        st.image(path, use_container_width=True, caption=caption)
    except Exception:
        st.warning(f"Image asset not found: `{path}` — verify filename, URL, and casing in the repository.")


# --- SESSION STATE INITIALIZATION ---
if "reviews_list" not in st.session_state:
    st.session_state.reviews_list = [
        {
            "name": "Supply Chain Director, Global Logistics",
            "rating": "⭐⭐⭐⭐⭐",
            "comment": "Guma and NG Advisory Co. provided incredible clarity on our freight delay bottlenecks. Highly recommend their dashboard frameworks!",
        },
        {
            "name": "Operations Manager, FCL Freight",
            "rating": "⭐⭐⭐⭐⭐",
            "comment": "The automated data pipelines and risk models built for our inventory workflows completely transformed our daily execution.",
        },
    ]

if "client_logged_in" not in st.session_state:
    st.session_state.client_logged_in = False

if "registered_accounts" not in st.session_state:
    st.session_state.registered_accounts = {"demo.client@ngadvisory.example": "DemoPass123!"}

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# --- SIDEBAR CONTACT & ADVISORY ---
st.sidebar.markdown("---")
st.sidebar.subheader("Contact & Advisory")
st.sidebar.markdown("**Guma Adolf**")
st.sidebar.markdown("*Founder & Lead Data Architect, NG Advisory Co.*")
st.sidebar.markdown("guma.adolf.da@gmail.com")
st.sidebar.markdown("+971 56 123 3978")
st.sidebar.markdown("[LinkedIn Profile](https://www.linkedin.com/in/gumadolf)")
st.sidebar.markdown("---")
st.sidebar.markdown("### NG Advisory Co.")

NAV_ITEMS = [
    "Home & Overview",
    "Dubai Traffic & Corridor Risk AI",
    "UAE NetZero Freight AI (Maritime)",
    "Commercial & Apparel Supply Chain BI",
    "Global Freight & Carbon Operations",
    "UAE Logistics & Operations Capabilities",
    "Warehouse & Lead-Time Optimization",
    "Superstore Supply Chain & Profitability",
    "Global Logistics & Risk Intelligence",
    "Global CO2 Emissions Analytics",
    "UAE Energy & Carbon Monoxide Engineering",
    "Remote Case Study: ROA",
    "Tableau Public & Wildlife Analytics",
    "Weather & Lightning Risk Analysis",
    "Foundational BI Suite (Pharmacy & Retail)",
    "Data Products & Risk Simulation",
    "Client Portal & Feedback",
    "Advisory Framework",
]

section = st.sidebar.radio("Navigation", NAV_ITEMS)

if section == "Home & Overview":
    render_image_safe(
        "NG logo.jpeg",
        "NG Advisory Co. | Guma Adolf, Founder & Lead Data Architect",
    )
    st.markdown(
        '<div class="hero-title">Build better business control without overcomplicating operations.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hero-subtitle">SOPs, warehouse controls, reporting automation, data products, and statistical modeling for enterprises that need clarity, structure, and execution velocity. Founded & Architected by Guma Adolf.</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Logistics Scale Handled</div>
                <div class="metric-value">AED 36M+</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">SOP Compliance Target</div>
                <div class="metric-value">92%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Core Tech Stack</div>
                <div class="metric-value" style="font-size: 1.3rem;">Python • SQL • BI • AI</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### Flagship ML & Geospatial Intelligence Comparison")
    st.markdown("Compare the **Dubai Traffic Incidents** and **UAE NetZero Freight** engines side by side:")

    flagship_df = pd.DataFrame(
        {
            "Project": [
                "Dubai Traffic Incidents Analysis",
                "UAE NetZero Freight AI (Maritime)",
            ],
            "Dataset & Scope": [
                "23,472 cleaned Dubai incident records (5.74% severe baseline)",
                "43,020 port-day records across 15 UAE ports (IMF PortWatch, Bayanat.ae, DataCo)",
            ],
            "Core Methods": [
                "K-Means clustering (k=3), feature engineering, Random Forest (RF v2) & threshold tuning",
                "Chronological RandomForestRegressor, Congestion Surge Classifier & JIT idling simulation",
            ],
            "Key Headline Results": [
                "Cluster 2 severe rate: 18.84% (>3x citywide); RF v2 ROC-AUC: 0.6881; threshold 0.55 -> 1,172 alerts & 43.87% recall",
                "Projected annual fuel ROI: AED 6.49M; 9,287 tons CO2 abated; 81.1% surge alert accuracy; MAE: 24,522 tons",
            ],
            "GitHub Repository": [
                GITHUB_TRAFFIC_REPO_URL,
                GITHUB_NETZERO_REPO_URL,
            ],
        }
    )
    st.dataframe(flagship_df, use_container_width=True, hide_index=True)

    st.markdown("### Executive Summary Briefings (GitHub Assets)")
    col_exec1, col_exec2 = st.columns(2)
    with col_exec1:
        render_image_safe(
            GITHUB_TRAFFIC_SUMMARY_URL,
            "Dubai Traffic Safety Executive Summary (dubai-traffic-incidents-analysis)",
        )
        st.markdown(f"[Open Dubai Traffic Repository on GitHub]({GITHUB_TRAFFIC_REPO_URL})")
    with col_exec2:
        render_image_safe(
            GITHUB_NETZERO_SUMMARY_URL,
            "UAE NetZero Freight Executive Summary (uae-netzero-freight-ai)",
        )
        st.markdown(f"[Open UAE NetZero Freight Repository on GitHub]({GITHUB_NETZERO_REPO_URL})")

    st.markdown("---")
    st.markdown("### New Dashboard Projects & In-Depth Visual Breakdowns")
    st.markdown("Explore the four newly added analytics dashboards, each covering a distinct operational and commercial domain:")

    col_n1, col_n2 = st.columns(2)
    with col_n1:
        render_image_safe(
            "NG pro1.jpeg",
            "Project 1: Logistics & Supply Chain Performance Dashboard (Jan–Jun 2024)",
        )
        st.markdown(
            """
            **Commercial Revenue, Brand Mix & Fulfillment Performance:**
- Tracks **$77M in total sales** (+2.1% vs. previous period) and **$6.49M in returns** (+1.5% across **4K return records**), led by **Jacket** ($16.6M), **Abaya** ($16.2M), and **Dress** ($10.9M).
- Breaks down brand performance across **Pharaoh Denim ($20.8M)**, **Luxor Co. ($19.2M)**, **Nile Wear ($16.0M)**, **Sphinx Kids ($7.1M)**, **Cairo Style ($6.4M)**, **Alex Trend ($4.8M)**, and **Delta Fashion ($2.6M)**, alongside regional sales led by **North America ($28.7M, +8.2%)** and **Middle East ($19.6M, +4.1%)**.
- Monitors operational execution via **6.2x inventory turnover**, **3.6-day average delivery time**, **96.1% order fulfillment rate**, **5.2% return rate**, **4.6/5 supplier performance**, and **8.7% logistics cost ratio**, with transport spend split across **Road ($45.2M / 58.7%)**, **Sea ($18.6M / 24.1%)**, **Air ($8.9M / 11.6%)**, and **Rail ($4.1M / 5.3%)**.
            """
        )

    with col_n2:
        render_image_safe(
            "NG PRO2.jpeg",
            "Project 2: Logistics & Supply Chain Dashboard (18.4K Shipments & CO₂ Tracking)",
        )
        st.markdown(
            """
            **Global Freight Flow, Route SLAs & Carbon Emissions:**
- Tracks **18.4K total shipments** (+12.5%), **$5.2M total logistics cost** (-8.3%), **92.6% on-time delivery** (+4.8%), **1.8% returns** (-0.6%), and **1,245 tons of CO₂ emissions** (-10.2%) from Jan–Jun 2024.
- Maps regional shipment volumes across **Asia (6.1K)**, **North America (4.8K)**, **Europe (3.9K)**, **South America (1.8K)**, **Africa (1.2K)**, and **Oceania (0.6K)**, paired with end-to-end flow metrics across **Suppliers** (98% on-time), **Warehouses** (96% in-stock), **Transportation** (92% on-time), and **Customers** (94% on-time).
- Evaluates category inventory levels (**Apparel 8.2M**, **Electronics 6.5M**, **Home & Living 5.1M**, **Beauty & Care 3.4M**, **Sports 2.8M**, **Toys 2.1M**), top suppliers such as **Pharaoh Denim** (4,812 orders, 96.4% on-time, 5-day lead time), major shipping corridors (**Shanghai → Los Angeles**, **Hamburg → New York**, **Dubai → London**, **Singapore → Sydney**, **Mumbai → Dubai**), and transport cost share (**Road 40%**, **Sea 28%**, **Air 20%**, **Rail 8%**, **Other 4%**).
            """
        )

    col_n3, col_n4 = st.columns(2)
    with col_n3:
        render_image_safe(
            "NG PRO3.jpeg",
            "Project 3: UAE Logistics & Operations Capabilities Overview (Fujairah, UAE)",
        )
        st.markdown(
            """
            **UAE Regional Operations, Tooling Impact & Automation Diagnostics:**
- Highlights **1,388 total transactions**, **11m average delivery lead time**, **96% on-time delivery rate**, and **98.5% inventory accuracy** with interactive filters for **Sector**, **Emirate**, and **KPI Type**.
- Compares 12-month operational transaction growth against process accuracy trends and benchmarks delivery performance across **Fujairah, Dubai, Abu Dhabi, and Sharjah**.
- Summarizes measurable portfolio outcomes—**Fujairah Port Fuel Analytics** (15% lead time reduction via Python), **Logistics Cost Optimization** (12% cost savings via SQL), and **Warehouse Automation** (20% efficiency increase via Power BI)—alongside tool adoption (**Python 22%**, **SQL 22%**, **Power BI 15%**, **Excel 12%**) and manual vs. automated workflow bottlenecks.
            """
        )

    with col_n4:
        render_image_safe(
            "NG PRO4.jpeg",
            "Project 4: Logistics Supply Chain Optimization Trend (12-Month Trajectory)",
        )
        st.markdown(
            """
            **12-Month Stock Accuracy vs. Turnaround Time Compression:**
- Tracks **stock accuracy climbing steadily from 88% in Month 1 to 98.5% by Month 12** (reaching 98% around Month 4 and 99% around Month 11) while **delivery turnaround time decreases from 5 days down to 1.9 days (optimized)**.
- Illustrates how tighter inventory controls and faster dispatch/turnaround cycles compound over a 12-month horizon.
- Anchors four core operational outcomes: **increased stock visibility**, **reduced order cycle time**, **enhanced data-driven decision making**, and **improved customer satisfaction**.
            """
        )

    st.markdown("---")
    st.markdown("### Executive Command Center & Professional Gallery")
    st.markdown("Explore the operational environments and professional milestones driving NG Advisory Co.:")

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        render_image_safe(
            "NG.jpeg",
            "NG Advisory Co. Executive Command Center & Strategic Leadership Environment",
        )
        st.markdown("**Field-Tested Logistics Execution & Advisory HQ:** Grounded in global supply chain operations managing AED 36M+ scale, freight handling, and exception resolution.")

    with col_p2:
        render_image_safe(
            "office.jpeg",
            "NG Advisory Co. Strategic Leadership & Client Consultation Environment",
        )
        st.markdown("**Client Consultation & Strategic Advisory:** Dedicated workspace tailored for executive sessions, operational audits, and stakeholder alignment.")

    col_p3, col_p4 = st.columns(2)
    with col_p3:
        render_image_safe(
            "MULT.jpeg",
            "NG Advisory Co. Enterprise Operations & Team Workspace",
        )
        st.markdown("**Collaborative Intelligence & Execution:** A unified advisory environment integrating enterprise analytics, continuous development, and cross-functional logistics execution.")

    with col_p4:
        render_image_safe(
            "Guma_Passport_Photo.JPG",
            "Guma Adolf | Founder & Lead Data Architect, NG Advisory Co.",
        )
        st.markdown("**Vision & Leadership:** Directing enterprise digital transformation, bridging heavy operational logistics with modern predictive data science.")

    st.markdown("---")
    st.markdown("### Live Operational Control Preview")
    st.text("Inventory Accuracy (Target: >85%)")
    st.progress(86)
    st.text("SOP Compliance & Governance")
    st.progress(92)

elif section == "Dubai Traffic & Corridor Risk AI":
    st.markdown(
        '<div class="hero-title">Dubai Traffic Safety: Geospatial Hotspot & Severity Risk Intelligence</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hero-subtitle">End-to-End Spatial Clustering (K-Means, k=3) & Probability-Tuned Random Forest (RF v2) across 23,472 Dubai Traffic Incidents | Smart Mobility & Emergency Dispatch Triage.</div>',
        unsafe_allow_html=True,
    )

    tc1, tc2, tc3, tc4 = st.columns(4)
    tc1.markdown('<div class="metric-card"><div class="metric-label">Incidents Analyzed</div><div class="metric-value">23,472</div></div>', unsafe_allow_html=True)
    tc2.markdown('<div class="metric-card"><div class="metric-label">Cluster 2 Severe Rate</div><div class="metric-value">18.84%</div></div>', unsafe_allow_html=True)
    tc3.markdown('<div class="metric-card"><div class="metric-label">RF v2 ROC-AUC</div><div class="metric-value">0.6881</div></div>', unsafe_allow_html=True)
    tc4.markdown('<div class="metric-card"><div class="metric-label">Alert Reduction (0.55)</div><div class="metric-value">-52%</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Executive Summary Visual (GitHub Asset)")
    render_image_safe(
        GITHUB_TRAFFIC_SUMMARY_URL,
        "Dubai Traffic Safety Executive Summary — Hotspot Clusters & Hourly Demand",
    )

    st.markdown("---")
    st.subheader("Spatial Corridor Breakdown & Model Progression")
    traffic_cluster_df = pd.DataFrame(
        {
            "Spatial Zone": [
                "Cluster 0 — Northern & Central Urban Core",
                "Cluster 1 — Southern & Western Metro Corridor",
                "Cluster 2 — Eastern Outlying / Hatta Highway Corridor",
            ],
            "Centroid Coordinates": [
                "~25.22°N, 55.35°E",
                "~25.06°N, 55.18°E",
                "~24.83°N, 55.92°E",
            ],
            "Corridor Profile": [
                "Deira, Bur Dubai, Downtown & adjacent interchanges",
                "Southwest arterial routes toward Dubai Marina & Jebel Ali",
                "High-speed inter-emirate corridor toward Hatta & southern Al Ain",
            ],
            "Severe Crash Rate": [
                "5.97% (Citywide Baseline)",
                "5.12% (Lowest Relative Severity)",
                "18.84% (>3x Citywide Baseline)",
            ],
        }
    )
    st.dataframe(traffic_cluster_df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("### Key Findings & Source Repository")
    st.markdown("* **Temporal Peaks:** Incidents climb steadily through midday to peak at **18:00** during evening commuter rush and on **Thursday** ahead of weekend travel (`5.74%` overall severe rate).")
    st.markdown("* **Model & Threshold Optimization:** Domain feature engineering lifted **Random Forest (`RF v2`) ROC-AUC from `0.5861` to `0.6881`**. Raising the decision threshold from `0.50` to **`0.55`** lifted severe-class **F1 to `0.1638`** and reduced flagged alerts from **2,443 to 1,172** while retaining **43.87%** severe-incident recall.")
    st.markdown(f"* **Full Code, Notebook & Reproducibility Guide:** [View on GitHub (`gumaadolfda-blip/dubai-traffic-incidents-analysis`)]({GITHUB_TRAFFIC_REPO_URL})")

elif section == "UAE NetZero Freight AI (Maritime)":
    st.markdown(
        '<div class="hero-title">UAE NetZero Freight: Maritime Decarbonization & Supply Chain AI</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hero-subtitle">Multi-Source Machine Learning & Generative AI Engine across 15 UAE Ports (43,020 Port-Day Records) | Aligned with UAE Net Zero 2050 & Federal Decree-Law No. 11/2023.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><div class="metric-label">Projected Annual Fuel ROI</div><div class="metric-value">AED 6.49M</div></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><div class="metric-label">Annual CO₂ Abated</div><div class="metric-value">9,287 Tons</div></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><div class="metric-label">Surge Alert Accuracy</div><div class="metric-value">81.1%</div></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><div class="metric-label">National Forecast MAE</div><div class="metric-value">24,522 Tons</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Executive Summary Visual (GitHub Asset)")
    render_image_safe(
        GITHUB_NETZERO_SUMMARY_URL,
        "UAE NetZero Freight Executive Summary — Port Congestion & Scope 3 Carbon Intelligence",
    )

    st.markdown("---")
    st.subheader("Interactive UAE Port Decarbonization Simulator")
    sim_col1, sim_col2 = st.columns(2)
    jit_reduction_pct = sim_col1.slider("AI Just-in-Time Anchorage Idling Reduction (%)", 5, 35, 15, 1)
    fuel_price_aed = sim_col2.number_input("Marine VLSFO Fuel Price (AED / Metric Ton)", 1500, 3500, 2200, 50)

    sim_co2_annual = (1190.67 * (jit_reduction_pct / 100.0)) * 52
    sim_fuel_annual = sim_co2_annual / 3.15
    sim_aed_annual = sim_fuel_annual * fuel_price_aed

    res1, res2, res3 = st.columns(3)
    res1.metric("Simulated Annual CO₂ Reduced", f"{sim_co2_annual:,.0f} Metric Tons")
    res2.metric("Simulated Marine Fuel Saved", f"{sim_fuel_annual:,.0f} Metric Tons")
    res3.metric("Simulated Annual Savings (AED)", f"AED {sim_aed_annual:,.0f}")

    st.markdown("---")
    st.subheader("Top UAE Maritime Carbon & Throughput Hotspots (7-Day Horizon)")
    port_df = pd.DataFrame(
        {
            "UAE Port": ["Port of Fujairah", "Jebel Ali (Dubai)", "Khalifa Port (Abu Dhabi)", "Khor Fakkan", "Sharjah"],
            "Primary Traffic Profile": ["Energy Tankers & Bunkering", "Container Mega-Hub", "Industrial & Container", "Transshipment Container", "General Cargo & Regional"],
            "Predicted Daily Tonnage": ["216,053 tons/day", "59,012 tons/day", "28,450 tons/day", "24,180 tons/day", "15,920 tons/day"],
            "7-Day CO₂ Saved (15% JIT)": ["55.9 tons", "43.7 tons", "14.2 tons", "13.9 tons", "9.4 tons"],
        }
    )
    st.dataframe(port_df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("### Executive Architecture & Source Repository")
    st.markdown("* **Data Integration:** Merged **IMF PortWatch** daily vessel calls, **Bayanat.ae** monthly UAE trade figures, and **DataCo** delay risk benchmarks across **43,020 records**.")
    st.markdown("* **Machine Learning & Explainability:** Chronological `RandomForestRegressor` paired with an `81.1%` accurate Congestion Surge Classifier.")
    st.markdown(f"* **Full Code & Jupyter Notebook:** [View on GitHub (`gumaadolfda-blip/uae-netzero-freight-ai`)]({GITHUB_NETZERO_REPO_URL})")

elif section == "Commercial & Apparel Supply Chain BI":
    st.header("Commercial & Apparel Supply Chain Performance (Jan–Jun 2024)")
    render_image_safe(
        "NG pro1.jpeg",
        "Logistics & Supply Chain Performance Dashboard — Commercial & Fulfillment View",
    )
    st.markdown(
        """
        ### In-Depth Project Breakdown
- **Revenue & Returns Scale:** Tracks **$77M in total sales** (+2.1% MoM) and **$6.49M in returns** (+1.5% MoM across **4K returns**), with **Jacket** ($16.6M), **Abaya** ($16.2M), and **Dress** ($10.9M) leading sub-categories.
- **Brand & Regional Performance:** Highlights top brands including **Pharaoh Denim** ($20.8M), **Luxor Co.** ($19.2M), and **Nile Wear** ($16.0M), with strongest regional revenue in **North America** ($28.7M, +8.2%) and the **Middle East** ($19.6M, +4.1%).
- **Fulfillment & Transport Mix:** Delivers **6.2x inventory turnover**, **3.6-day average delivery time**, **96.1% order fulfillment rate**, **5.2% return rate**, **4.6/5 supplier score**, and **8.7% logistics cost share**, across **Road ($45.2M)**, **Sea ($18.6M)**, **Air ($8.9M)**, and **Rail ($4.1M)**.
        """
    )

elif section == "Global Freight & Carbon Operations":
    st.header("Global Freight Volume, Route SLA & CO₂ Emissions Dashboard")
    render_image_safe(
        "NG PRO2.jpeg",
        "Logistics & Supply Chain Dashboard — Shipments, Routes & Emissions View",
    )
    st.markdown(
        """
        ### In-Depth Project Breakdown
- **Core Metrics:** Covers **18.4K shipments** (+12.5%), **$5.2M logistics cost** (-8.3%), **92.6% on-time delivery** (+4.8%), **1.8% returns** (-0.6%), and **1,245 tons of CO₂ emissions** (-10.2%).
- **Supply Chain Flow & Status:** Connects **Suppliers** (98% on-time supply), **Warehouses** (96% in-stock rate), **Transportation** (92% on-time transit), and **Customers** (94% on-time delivery), with **72.3% delivered**, **18.1% in transit**, **5.4% pending**, **2.9% delayed**, and **1.3% cancelled**.
- **Regions, Inventory & Corridors:** Shows shipment volume across **Asia (6.1K)**, **North America (4.8K)**, and **Europe (3.9K)**, inventory levels led by **Apparel (8.2M)** and **Electronics (6.5M)**, major trade lanes such as **Shanghai → Los Angeles** and **Mumbai → Dubai**, and transport cost shares led by **Road (40%)** and **Sea (28%)**.
        """
    )

elif section == "UAE Logistics & Operations Capabilities":
    st.header("UAE Logistics & Operations Capabilities Overview")
    render_image_safe(
        "NG PRO3.jpeg",
        "Guma Adolf — UAE Logistics & Operations Capabilities Dashboard (Fujairah, UAE)",
    )
    st.markdown(
        """
        ### In-Depth Project Breakdown
- **Operational KPIs:** Captures **1,388 total transactions**, **11m average delivery lead time**, **96% on-time delivery rate**, and **98.5% inventory accuracy**, with filters for **Sector**, **Emirate**, and **KPI Type**.
- **Trends & Emirate Comparison:** Tracks 12-month operational transaction growth alongside process accuracy and compares delivery performance across **Fujairah, Dubai, Abu Dhabi, and Sharjah**.
- **Portfolio Impact & Automation:** Details outcomes across **Fujairah Port Fuel Analytics** (15% lead time reduction via Python), **Logistics Cost Optimization** (12% cost savings via SQL), and **Warehouse Automation** (20% efficiency increase via Power BI), alongside tool adoption (**Python 22%**, **SQL 22%**, **Power BI 15%**, **Excel 12%**) and workflow bottleneck diagnostics.
        """
    )

elif section == "Warehouse & Lead-Time Optimization":
    st.header("12-Month Stock Accuracy & Delivery Turnaround Optimization")
    render_image_safe(
        "NG PRO4.jpeg",
        "Logistics Supply Chain Optimization Trend — 12-Month Performance Trajectory",
    )
    st.markdown(
        """
        ### In-Depth Project Breakdown
- **Accuracy vs. Turnaround Curve:** Tracks **stock accuracy rising from 88% in Month 1 to 98.5% by Month 12** (reaching 98% around Month 4 and 99% around Month 11) while **delivery turnaround time compresses from 5 days to 1.9 days (optimized)**.
- **Operational Takeaways:** Demonstrates how continuous stock accuracy gains and streamlined dispatch/turnaround cycles reinforce one another across a full 12-month cycle.
- **Key Outcomes:** Highlights **increased stock visibility**, **reduced order cycle time**, **enhanced data-driven decision making**, and **improved customer satisfaction**.
        """
    )

elif section == "Superstore Supply Chain & Profitability":
    st.header("Superstore Supply Chain & Profitability Optimization")
    st.write("**Project Type:** Enterprise Power BI Commercial & Profit Margin Analysis")
    st.write("**Scope:** Granular breakdown of sales revenue by product categories, segment profitability, regional performance, and shipping mode efficiencies.")

    st.markdown("---")
    col_sup1, col_sup2 = st.columns(2)
    with col_sup1:
        render_image_safe(
            "Screenshot 2026-07-01 095504.png",
            "Superstore Executive View | Sales Revenue & Segment Margins",
        )
    with col_sup2:
        render_image_safe(
            "Screenshot 2026-07-01 095527.png",
            "Average Days to Ship by Ship Mode",
        )

    st.markdown("---")
    st.subheader("Product Performance Breakdown")
    render_image_safe(
        "Screenshot 2026-02-27 071707.png",
        "Sum of Price, Total Revenue, and Units by Product Category",
    )

elif section == "Global Logistics & Risk Intelligence":
    st.header("Global Logistics & Supply Chain Analysis Dashboard (2026)")
    st.write("**Project Type:** Global Fulfillment Risk & Delivery Optimization Suite")
    st.write("**Scope:** Comprehensive multi-region tracking platform managing AED 36M+ in sales volume, late delivery risk modeling, shipping mode distributions, and global order mapping.")

    st.markdown("---")
    col_log1, col_log2 = st.columns(2)
    with col_log1:
        render_image_safe(
            "Screenshot 2026-03-12 221148.png",
            "Global Supply Chain Dashboard with Risk Slider & Mapping",
        )
    with col_log2:
        render_image_safe(
            "Screenshot 2026-02-28 091817.png",
            "Shipment Performance Dashboard | Geospatial Risk & Route Analysis",
        )

    st.markdown("---")
    st.subheader("Foundational Logistics Views & Route Mapping")
    col_lsub1, col_lsub2 = st.columns(2)
    with col_lsub1:
        render_image_safe(
            "logistics .png",
            "Logistics Performance Overview (Feb 2026)",
        )
    with col_lsub2:
        render_image_safe(
            "Screenshot 2026-02-28 093719.png",
            "Detailed Freight Cost & Status Breakdown",
        )

elif section == "Global CO2 Emissions Analytics":
    st.header("Global CO2 Emissions & Per Capita Intelligence Dashboard")
    st.write("**Project Type:** Environmental Impact & Macro-Economic Power BI Suite")
    st.write("**Scope:** Cross-country evaluation of historical total CO2 emissions alongside per capita emission rates, featuring dynamic country code filters.")

    st.markdown("---")
    render_image_safe(
        "Screenshot 2026-06-05 210806.png",
        "CO2 Emissions Executive Overview | Top Historical Countries & Per Capita Rankings",
    )

elif section == "UAE Energy & Carbon Monoxide Engineering":
    st.header("Energy Commodities & Carbon Monoxide Analytics")
    st.write("**Project Type:** Python Data Engineering & Power BI Executive Dashboard Suite")
    st.write("**Scope:** Comprehensive multi-sector examination of energy commodities and historical Carbon Monoxide (CO) concentration trends across locations.")

    st.markdown("---")
    st.subheader("1. Power BI Executive Dashboards")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        render_image_safe(
            "Screenshot proje1.png",
            "Energy Commodities Dashboard - Executive Overview",
        )
    with col_e2:
        render_image_safe(
            "Screenshot proje2.png",
            "Energy Sector Commodity Deep Dive & Geographic Mapping",
        )

    st.markdown("---")
    st.subheader("2. Python Jupyter Notebook Analysis (CO Concentrations)")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        render_image_safe(
            "chart.png",
            "Average CO Concentration Trend (2006–2016)",
        )
        render_image_safe(
            "plot.png",
            "Annual Average Carbon Monoxide Trends",
        )
    with col_c2:
        render_image_safe(
            "final.png",
            "Average CO Concentration by Location Type",
        )
        render_image_safe(
            "plot2.png",
            "Statistical Summary Table: CO by Location Type",
        )

elif section == "Remote Case Study: ROA":
    st.header("Remote Client Engagement: Repair Our Air (ROA)")
    st.write("**Role:** Lead Remote Data Scientist & Statistical Consultant (NG Advisory Co.)")
    st.write("**Client Profile:** Environmental think tank formulating national policy recommendations using EPA Air Quality Index (AQI) data.")

    st.markdown("---")
    st.subheader("Exploratory Data Analysis: State-Level AQI Distribution")
    render_image_safe(
        "California .png",
        "Seaborn Boxplot Analysis | State-Level AQI Distribution & Outlier Detection",
    )
    st.write(
        "Executed rigorous statistical evaluations using Python and SciPy (`scipy.stats.ttest_ind`) with Welch's t-test adjustments (`equal_var = False`) to account for unequal variances across regional populations (alpha = 0.05)."
    )

elif section == "Tableau Public & Wildlife Analytics":
    st.header("Tableau Public Portfolio & Wildlife Incident Analytics")
    st.write("**Project Type:** Cloud-Published Interactive Vizzes & Spatial Aviation Safety Analysis")
    st.write("**Scope:** Published Tableau Public vizzes (`GUMA_ADOLF_TABLEAU_PROJECT`, `CO2 VIZ`) alongside multi-year US bird strikes and wildlife incident density mapping.")

    st.markdown("---")
    render_image_safe(
        "WhatsApp Image 2026-09-12 at 8.55.09 AM.jpeg",
        "Tableau Public Creator Profile | Published Vizzes Showcase",
    )

    st.markdown("---")
    st.subheader("US Wildlife & Bird Strikes Analytics Suite")
    col_wld1, col_wld2 = st.columns(2)
    with col_wld1:
        render_image_safe(
            "WhatsApp Image 2026-09-07 at 10.58.27 AM.jpeg",
            "Wildlife Strike Frequency Bins (Tableau)",
        )
        render_image_safe(
            "WhatsApp Image 2026-09-07.jpeg",
            "Sum of Number of Strikes Trend Line (2016–2018)",
        )
    with col_wld2:
        render_image_safe(
            "WhatsApp Image 2026-09-07 at 10.58.29AM.jpeg",
            "US Spatial Density Incident Mapping",
        )
        render_image_safe(
            "09-10 at 10.36.28 AM.jpeg",
            "Seoul Bike Rentals Time-Series Analysis",
        )

elif section == "Weather & Lightning Risk Analysis":
    st.header("Environmental Risk: Weather & Lightning Strike Analytics")
    st.write("**Project Type:** Exploratory Time-Series & Statistical Distribution Analysis")
    st.write("**Scope:** Examining temporal weather volatility, weekday distributions, and seasonal percentage concentrations of lightning and storm strikes.")

    st.markdown("---")
    col_ltg1, col_ltg2 = st.columns(2)
    with col_ltg1:
        render_image_safe(
            "Screenshot 2026-08-23 081053[1].png",
            "Lightning Distribution per Weekday (2018)",
        )
    with col_ltg2:
        render_image_safe(
            "Screenshot 2026-08-23 081139[2].png",
            "Monthly Percentage Concentration of Lightning Strikes (2016–2018)",
        )

elif section == "Foundational BI Suite (Pharmacy & Retail)":
    st.header("Foundational Business Intelligence Suite")
    st.write("**Project Type:** Early Commercial, Pharmacy, and Logistics Power BI Reports")

    tab_f1, tab_f2, tab_f3 = st.tabs(
        ["Pharmacy Sales BI", "Retail Sales BI", "Logistics Milestones"]
    )

    with tab_f1:
        st.subheader("Pharmacy Sales Analysis")
        render_image_safe(
            "feb.png",
            "Geographic Mapping & Product Profitability",
        )
        render_image_safe(
            "Screenshot 2026-02-27 073605.png",
            "Pharmacy Sales Dashboard Detailed View",
        )

    with tab_f2:
        st.subheader("Retail Sales Dashboard")
        render_image_safe(
            "my.png",
            "AED 456K Total Sales, Category Breakdown & Demographic Slicers",
        )
        render_image_safe(
            "WhatsApp Image 2026-09-07 at 10.58.22AM.jpeg",
            "Retail Sales Distribution & Date Filtering",
        )

    with tab_f3:
        st.subheader("Early Logistics & Transport Reports")
        render_image_safe(
            "WhatsApp Image 2026-09-07 at 10.58.10AM.jpeg",
            "Logistics Performance Overview Map & Weights",
        )

elif section == "Data Products & Risk Simulation":
    st.header("Featured Data Products & Simulations")
    st.write("Interactive analytics engines built to optimize fulfillment pathways and reduce late delivery risks.")

    risk_slider = st.slider(
        "Select Late Delivery Risk Threshold Factor",
        min_value=0.0,
        max_value=1.0,
        value=0.25,
        step=0.05,
    )

    if risk_slider > 0.5:
        st.error(
            f"⚠️ High Risk Threshold ({risk_slider}): Rerouting logistics bottlenecks and triggering automated exception alerts."
        )
    else:
        st.success(
            f"✅ Optimal Risk Threshold ({risk_slider}): Fulfillment operations running smoothly within target thresholds."
        )

elif section == "Client Portal & Feedback":
    st.header("NG Advisory Co. | Client Portal, Account Creation & Resource Center")
    st.write("Welcome to the secure global gateway. Create an account or log in to access confidential advisory frameworks, download proprietary assessment templates, and connect directly with our team.")

    tab_portal1, tab_portal2, tab_portal3, tab_portal4 = st.tabs([
        "Client Login & Account Creation",
        "Downloadable Assets",
        "Reviews & Testimonials",
        "Contact Us",
    ])

    with tab_portal1:
        st.subheader("Client Portal Access")
        auth_mode = st.radio("Select Action", ["Log In to Existing Account", "Create New Account"], horizontal=True)

        if auth_mode == "Log In to Existing Account":
            if not st.session_state.client_logged_in:
                with st.form("login_form"):
                    login_email = st.text_input("Email Address")
                    login_pass = st.text_input("Passcode", type="password")
                    submit_login = st.form_submit_button("Log In")

                    if submit_login:
                        if login_email in st.session_state.registered_accounts and st.session_state.registered_accounts[login_email] == login_pass:
                            st.session_state.client_logged_in = True
                            st.session_state.user_email = login_email
                            st.success("Successfully authenticated! Welcome back to the global client dashboard.")
                            st.rerun()
                        else:
                            st.error("Invalid email or passcode. Please check your credentials or create an account.")
            else:
                st.success(f"🟢 Logged in as: **{st.session_state.user_email}**")
                st.info("🔓 **Exclusive Client Workspace:** Access to confidential logistics optimization models and direct consultation scheduling is currently unlocked.")
                if st.button("Log Out"):
                    st.session_state.client_logged_in = False
                    st.session_state.user_email = ""
                    st.rerun()
        else:
            st.subheader("Register a New Global Client Account")
            with st.form("signup_form"):
                new_email = st.text_input("Enter Email Address")
                new_pass = st.text_input("Create Passcode", type="password")
                confirm_pass = st.text_input("Confirm Passcode", type="password")
                submit_signup = st.form_submit_button("Create Account")

                if submit_signup:
                    if not new_email or not new_pass:
                        st.warning("Please fill out all fields.")
                    elif new_email in st.session_state.registered_accounts:
                        st.error("An account with this email already exists. Please log in.")
                    elif new_pass != confirm_pass:
                        st.error("Passcodes do not match. Please re-enter.")
                    else:
                        st.session_state.registered_accounts[new_email] = new_pass
                        st.session_state.client_logged_in = True
                        st.session_state.user_email = new_email
                        st.success("Account created successfully! You are now logged in.")
                        st.rerun()

    with tab_portal2:
        st.subheader("Proprietary Advisory Templates & Resources")
        st.write("Download field-tested logistics audit checklists and analytics templates crafted by NG Advisory Co.")

        sample_csv = "Metric,Target,Status\nInventory Accuracy,>85%,Optimal\nSOP Compliance,92%,Compliant\nLate Delivery Risk,<5%,Controlled"
        st.download_button(
            label="Download Logistics Audit Checklist (CSV)",
            data=sample_csv,
            file_name="NG_Advisory_Logistics_Audit_Template.csv",
            mime="text/csv",
        )

        sample_whitepaper = "NG Advisory Co. Enterprise Whitepaper:\nBridging Raw Data and Logistics Visibility through Python & SQL Automation.\nAuthor: Guma Adolf, Founder & Lead Data Architect."
        st.download_button(
            label="Download Enterprise Advisory Whitepaper (TXT)",
            data=sample_whitepaper,
            file_name="NG_Advisory_Enterprise_Whitepaper.txt",
            mime="text/plain",
        )

    with tab_portal3:
        st.subheader("Client Feedback & Global Reviews")
        st.write("See what partners and logistics operators are saying about our engagements, or leave your own review below!")

        for rev in st.session_state.reviews_list:
            st.markdown(f"> **{rev['name']}**  \n> {rev['rating']}  \n> *\"{rev['comment']}\"*")
            st.markdown("---")

        st.subheader("Leave a Review or Inquiry")
        with st.form("review_form"):
            reviewer_name = st.text_input("Your Name / Company")
            reviewer_rating = st.selectbox("Rating", ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐"])
            reviewer_comment = st.text_area("Your Feedback or Project Experience")
            submit_review = st.form_submit_button("Submit Review")

            if submit_review:
                if reviewer_name and reviewer_comment:
                    new_rev = {"name": reviewer_name, "rating": reviewer_rating, "comment": reviewer_comment}
                    st.session_state.reviews_list.append(new_rev)
                    st.success("Thank you! Your review has been successfully posted to the platform.")
                    st.rerun()
                else:
                    st.warning("Please fill in both your name and feedback comment before submitting.")

    with tab_portal4:
        st.subheader("Direct Contact & Enterprise Inquiries")
        st.write("Have a custom project or enterprise advisory requirement? Reach out directly to our headquarters:")
        st.markdown(
            """
- **Founder & Lead Data Architect:** Guma Adolf
- **Direct Mobile / WhatsApp:** +971 56 123 3978
- **Official Email:** guma.adolf.da@gmail.com
- **Global Network:** LinkedIn (`https://www.linkedin.com/in/gumadolf`)
            """
        )
        st.info("We respond to all global client inquiries within 24 hours.")

elif section == "Advisory Framework":
    st.header("Practical Systems & Business Control")
    st.markdown(
        """
- **Diagnostic Analytics & Bottleneck Identification:** Uncovering hidden friction points in warehouse execution and cargo transit.
- **Experimental Design & Validation:** Implementing rigorous hypothesis testing, variance checks, and SciPy statistical validation.
- **Automation & Control Dashboards:** Building real-time data products that eliminate manual reporting friction.
        """
    )

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #6b7280; font-size: 0.85rem;'>© 2026 NG Advisory Co. | Founded & Architected by Guma Adolf | +971 56 123 3978 | guma.adolf.da@gmail.com | Worldwide</div>",
    unsafe_allow_html=True,
)
