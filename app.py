import streamlit as st
import os

# ==========================================
# PAGE CONFIGURATION & GLOBAL STYLING
# ==========================================
st.set_page_config(
    page_title="NG Advisory Co. | Enterprise Command Center",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stSidebar { background-color: #161b22; }
    h1, h2, h3 { color: #58a6ff; }
    </style>
""", unsafe_allow_html=True)

# Helper function to find images securely using exact repository filenames
def display_image_safely(possible_filenames, caption=""):
    found = False
    for filename in possible_filenames:
        if os.path.exists(filename):
            st.image(filename, caption=caption, use_container_width=True)
            found = True
            break
    if not found:
        st.info(f"💡 *Image asset pending: looking for one of {possible_filenames} in repository root.*")

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.image("https://img.icons8.com/color/96/combo-chart--v1.png", width=80)
st.sidebar.title("NG Advisory Co.")
st.sidebar.markdown("**Founder & Data Scientist:** Guma Adolf")
st.sidebar.markdown("---")

menu_selection = st.sidebar.radio(
    "Navigation Suite",
    [
        "🏠 Home / Overview",
        "📦 Supply Chain & Global Logistics",
        "🧪 Advanced Python & SciPy (ROA AQI)",
        "🌍 Global CO2 Emissions Dashboard",
        "⚡ UAE Energy & Carbon Monoxide",
        "📈 Foundational BI Suite (Retail, Pharmacy, Logistics)",
        "🗺️ Tableau Public & Wildlife Safety",
        "🌦️ Weather & Lightning Risk",
        "💡 Advisory Framework & Data Products"
    ]
)

# ==========================================
# 1. HOME / OVERVIEW SECTION
# ==========================================
if menu_selection == "🏠 Home / Overview":
    # Hero Command Center Banner
    display_image_safely(["a_Add_even_a_2_screen_.jpg", "office.jpeg"], caption="NG Advisory Co. Command Center | Guma Adolf")
    
    st.markdown("""
    # NG Advisory Co.
    ### *Bridging Heavy Operations & Predictive Data Science*
    
    Welcome to the digital command center of **NG Advisory Co.** Founded on the front lines of UAE logistics and supply chain execution (AED 36M+ scale), our mission is simple: **move beyond static reporting into predictive risk and proactive operational control.**
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🚀 The NG Advisory Methodology: From Coursework to Control
    Every analytical framework we build—whether through advanced Python pipelines, statistical modeling, or business intelligence—is engineered to solve real-world operational bottlenecks:
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        #### 📊 1. Operational Data Auditing
        * **From EDA to Data Integrity:** Cleaning, structuring, and auditing raw multi-source datasets.
        * **Load & Variance Profiling:** Mapping distributions, skewness, and transit delays before they impact margins.
        """)
    with col2:
        st.markdown("""
        #### 🧪 2. Rigorous Hypothesis Testing
        * **Inferential Statistics:** Deploying Welch’s t-tests, $p$-values, and significance thresholds ($\alpha = 0.05$).
        * **Separating Signal from Noise:** Isolating nuisance factors to ensure decisions are backed by empirical data, not intuition.
        """)
    with col3:
        st.markdown("""
        #### 🔮 3. Predictive Risk & Bayesian Logic
        * **Bayes' Theorem in Action:** Continuously updating probability estimates as live environmental and route data streams in.
        * **Closing the Loop:** Translating insights directly into routing, load balancing, and exception handling.
        """)

    st.markdown("---")
    st.markdown("""
    ### 📂 Explore the Live Platform Suite
    Use the sidebar navigation to explore our end-to-end capabilities:
    * **Supply Chain & Global Logistics:** Superstore analytics, weather-related delay risk, and maritime intelligence.
    * **Advanced Python & SciPy Pipelines:** AQI environmental case studies, hypothesis testing, and Seaborn visual asset mapping.
    * **Foundational BI Suite:** Commercial retail sales, pharmacy records, and core executive Power BI dashboards.
    * **Advisory Frameworks:** Strategic consulting methodologies designed to close the gap between insight and execution.
    """)
    st.info("💡 **Operational Philosophy:** *Reporting tells you what happened; predictive risk tells you what to do next. The ones who close the loop to control win.*")

# ==========================================
# 2. SUPPLY CHAIN & GLOBAL LOGISTICS
# ==========================================
elif menu_selection == "📦 Supply Chain & Global Logistics":
    st.title("📦 Supply Chain & Global Logistics Intelligence")
    st.markdown("Analyzing transport throughput, freight handling, and route optimization across UAE and global networks (AED 36M+ commercial scale).")
    
    display_image_safely(["office.jpeg", "logistics .png"], caption="Command Center & Logistics Operations")
        
    col1, col2, col3 = st.columns(3)
    col1.metric("Managed Scale", "AED 36M+", "+14% YoY")
    col2.metric("Exception Resolution", "99.2%", "Optimized")
    col3.metric("Data Pipeline Latency", "Real-Time", "Automated")
    
    st.markdown("### Core Capabilities")
    st.write("- Multi-table SQL data joining in Google BigQuery.")
    st.write("- Folium geospatial mapping for transit risk evaluation.")
    st.write("- Power BI dashboards tracking shipment delays and exception handling.")

# ==========================================
# 3. ADVANCED PYTHON & SCIPY (ROA AQI)
# ==========================================
elif menu_selection == "🧪 Advanced Python & SciPy (ROA AQI)":
    st.title("🧪 Advanced Python & Inferential Statistics")
    st.markdown("### Repair Our Air (ROA) Environmental Case Study\nExecuting hypothesis tests, handling variance with Welch's t-tests (`scipy.stats.ttest_ind`), and analyzing air quality index (AQI) distributions across metropolitan areas.")
    
    display_image_safely(["California .png"], caption="Seaborn Boxplot: Los Angeles vs. Rest of California AQI")
        
    st.markdown("""
    ### Key Statistical Milestones:
    * **Nuisance Factors & Experimental Design:** Controlling confounding variables in analytical pipelines.
    * **Inferential Validation:** Using $p$-values against significance levels ($\alpha = 0.05$) to reject or fail to reject null hypotheses.
    * **Bayesian Inference:** Continuously updating probabilistic risk models with live environmental data.
    """)

# ==========================================
# 4. GLOBAL CO2 EMISSIONS DASHBOARD
# ==========================================
elif menu_selection == "🌍 Global CO2 Emissions Dashboard":
    st.title("🌍 Global CO2 Emissions & Sustainability Analytics")
    st.markdown("Interactive dark-theme analytics tracking global carbon output, country-level slicers, and emissions reduction trajectories.")
    display_image_safely(["chart.png", "plot.png"])

# ==========================================
# 5. UAE ENERGY & CARBON MONOXIDE
# ==========================================
elif menu_selection == "⚡ UAE Energy & Carbon Monoxide":
    st.title("⚡ UAE Energy & Carbon Monoxide Engineering")
    st.markdown("Engineering telemetry analysis covering regional air quality indices, emissions monitoring, and industrial safety thresholds across the Emirates.")

# ==========================================
# 6. FOUNDATIONAL BI SUITE
# ==========================================
elif menu_selection == "📈 Foundational BI Suite (Retail, Pharmacy, Logistics)":
    st.title("📈 Foundational Business Intelligence Suite")
    st.markdown("Core commercial reporting milestones establishing the bedrock of NG Advisory Co.'s analytical frameworks.")
    
    display_image_safely(["feb.png"], caption="Early Commercial Retail & Logistics Record Analysis")
        
    st.markdown("""
    * **Pharmacy Reporting:** Inventory turnover and stockout risk analysis.
    * **Retail Sales Dashboards:** SUMIF, XLOOKUP, and Power Query M-code data standardization.
    * **Logistics Milestones:** Transactional freight audits and exception logging.
    """)

# ==========================================
# 7. TABLEAU PUBLIC & WILDLIFE SAFETY
# ==========================================
elif menu_selection == "🗺️ Tableau Public & Wildlife Safety":
    st.title("🗺️ Tableau Public & Wildlife Safety Analytics")
    st.markdown("Visual storytelling dashboards hosted on Tableau Public, integrating spatial safety metrics and incident risk mapping.")
    display_image_safely(["final.png", "my.png"])

# ==========================================
# 8. WEATHER & LIGHTNING RISK
# ==========================================
elif menu_selection == "🌦️ Weather & Lightning Risk":
    st.title("🌦️ Weather & Lightning Risk Intelligence")
    st.markdown("Predictive analytics mapping environmental hazards against transit schedules to preemptively divert logistics operations.")

# ==========================================
# 9. ADVISORY FRAMEWORK & DATA PRODUCTS
# ==========================================
elif menu_selection == "💡 Advisory Framework & Data Products":
    st.title("💡 NG Advisory Framework & Data Products")
    st.markdown("""
    ### Strategic Consulting Methodologies
    NG Advisory Co. helps organizations transition from reactive reporting to proactive operational control.
    
    * **Audit & Assess:** Comprehensive evaluation of enterprise data pipelines.
    * **Model & Predict:** Deploying Python-backed statistical risk engines.
    * **Execute & Control:** Closing the loop between insights and ground-level operational execution.
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2026 NG Advisory Co. All Rights Reserved.")
