import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Guma Adolf | NG Advisory Co. Platform",
    page_icon="📊",
    layout="wide",
)

# --- OPEN GRAPH META TAGS FOR LINK PREVIEWS ---
st.markdown(
    """
    <head>
        <meta property="og:image" content="https://githubusercontent.com">
        <meta property="og:title" content="Guma Adolf | NG Advisory Co. Platform">
        <meta property="og:description" content="Interactive portfolio, supply chain analytics, and data products platform for NG Advisory Co.">
    </head>
    """,
    unsafe_allow_html=True,
)

# Custom CSS for Elite SaaS Dark Theme Styling
st.markdown(
    """
    <style>
    .stApp { background-color: #0b0f19; color: #f3f4f6; }
    .hero-title { font-size: 2.8rem; font-weight: 800; color: #ffffff; line-height: 1.2; margin-bottom: 20px; }
    .hero-subtitle { font-size: 1.1rem; color: #9ca3af; margin-bottom: 30px; }
    .metric-card { background-color: #111827; border: 1px solid #1f2937; padding: 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
    .metric-value { font-size: 1.8rem; font-weight: 700; color: #38bdf8; }
    .metric-label { font-size: 0.85rem; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.05em; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- SESSION STATE INITIALIZATION ---
if "reviews_list" not in st.session_state:
    st.session_state.reviews_list = [
        {"name": "Supply Chain Director, Global Logistics", "rating": "⭐⭐⭐⭐⭐", "comment": "Guma and NG Advisory Co. provided incredible clarity on our freight delay bottlenecks. Highly recommend their dashboard frameworks!"},
        {"name": "Operations Manager, FCL Freight", "rating": "⭐⭐⭐⭐⭐", "comment": "The automated data pipelines and risk models built for our inventory workflows completely transformed our daily execution."}
    ]

if "client_logged_in" not in st.session_state:
    st.session_state.client_logged_in = False

if "registered_accounts" not in st.session_state:
    st.session_state.registered_accounts = {"guma.adolf.da@gmail.com": "password123"}

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

# Sidebar Navigation containing ALL projects and frameworks
st.sidebar.markdown("### NG Advisory Co.")
section = st.sidebar.radio(
    "Navigation",
    [
        "Home & Overview",
        "UAE NetZero Freight AI (Maritime)",
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
    ],
)

if section == "Home & Overview":
    col_home_img, col_home_text = st.columns([1, 2], gap="medium")
    with col_home_img:
        st.image("Guma_Passport_Photo.JPG", use_container_width=True, caption="Guma Adolf | Founder & Lead Data Architect, NG Advisory Co.")
    with col_home_text:
        st.markdown('<div class="hero-title">Build better business control without overcomplicating operations.</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-subtitle">SOPs, warehouse controls, reporting automation, data products, and statistical modeling for enterprises that need clarity, structure, and execution velocity. Founded & Architected by Guma Adolf.</div>', unsafe_allow_html=True)

    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><div class="metric-label">Logistics Scale Handled</div><div class="metric-value">AED 36M+</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><div class="metric-label">SOP Compliance Target</div><div class="metric-value">92%</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><div class="metric-label">Core Tech Stack</div><div class="metric-value" style="font-size: 1.3rem;">Python • SQL • BI • AI</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Executive Command Center & Professional Gallery")
    st.markdown("Explore the operational environments and professional milestones driving NG Advisory Co.:")

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.image("NG.jpeg", use_container_width=True, caption="NG Advisory Co. Executive Command Center & Strategic Leadership Environment")
        st.markdown("**Field-Tested Logistics Execution & Advisory HQ:** Grounded in global supply chain operations managing AED 36M+ scale, freight handling, and exception resolution.")
    with col_p2:
        st.image("office.jpeg", use_container_width=True, caption="NG Advisory Co. Strategic Leadership & Client Consultation Environment")
        st.markdown("**Client Consultation & Strategic Advisory:** Dedicated workspace tailored for executive sessions, operational audits, and stakeholder alignment.")

    col_p3, col_p4 = st.columns(2)
    with col_p3:
        st.image("MULT.jpeg", use_container_width=True, caption="NG Advisory Co. Enterprise Operations & Team Workspace")
        st.markdown("**Collaborative Intelligence & Execution:** A unified advisory environment integrating enterprise analytics, continuous development, and cross-functional logistics execution.")
    with col_p4:
        st.image("Guma_Passport_Photo.JPG", use_container_width=True, caption="Guma Adolf | Founder & Lead Data Architect, NG Advisory Co.")
        st.markdown("**Vision & Leadership:** Directing enterprise digital transformation, bridging heavy operational logistics with modern predictive data science.")

    st.markdown("---")
    st.markdown("### Live Operational Control Preview")
    st.text("Inventory Accuracy (Target: >85%)")
    st.progress(86)
    st.text("SOP Compliance & Governance")
    st.progress(92)

elif section == "UAE NetZero Freight AI (Maritime)":
    st.markdown('<div class="hero-title">UAE NetZero Freight: Maritime Decarbonization & Supply Chain AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Multi-Source Machine Learning & Generative AI Engine across 15 UAE Ports (43,020 Port-Day Records) | Aligned with UAE Net Zero 2050 & Federal Decree-Law No. 11/2023.</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><div class="metric-label">Projected Annual Fuel ROI</div><div class="metric-value">AED 6.49M</div></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><div class="metric-label">Annual CO₂ Abated</div><div class="metric-value">9,287 Tons</div></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><div class="metric-label">Surge Alert Accuracy</div><div class="metric-value">81.1%</div></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><div class="metric-label">National Forecast MAE</div><div class="metric-value">24,522 Tons</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Interactive UAE Port Decarbonization Simulator")
    st.write("Adjust AI 'Just-in-Time' arrival optimization and marine fuel price to simulate national savings across all 15 UAE ports:")

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
    port_df = pd.DataFrame({
        "UAE Port": ["Port of Fujairah", "Jebel Ali (Dubai)", "Khalifa Port (Abu Dhabi)", "Khor Fakkan", "Sharjah"],
        "Primary Traffic Profile": ["Energy Tankers & Bunkering", "Container Mega-Hub", "Industrial & Container", "Transshipment Container", "General Cargo & Regional"],
        "Predicted Daily Tonnage": ["216,053 tons/day", "59,012 tons/day", "28,450 tons/day", "24,180 tons/day", "15,920 tons/day"],
        "7-Day CO₂ Saved (15% JIT)": ["55.9 tons", "43.7 tons", "14.2 tons", "13.9 tons", "9.4 tons"],
    })
    st.dataframe(port_df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown(
        """
        ### Executive Architecture & Source Repository
        * **Data Integration:** Merged **IMF PortWatch** daily vessel calls, **Bayanat.ae** monthly UAE trade figures (~134.6B AED benchmark), and **DataCo** delay risk benchmarks across **43,020 records**.
        * **Machine Learning & Explainability:** Chronological `RandomForestRegressor` (83% weight on 7-day rolling tonnage + tanker/container calls) paired with an `81.1%` accurate Congestion Surge Classifier.
