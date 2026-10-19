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

# Bulletproof helper function that checks all common extensions automatically
def display_image_safely(base_names, caption=""):
    found = False
    if isinstance(base_names, str):
        base_names = [base_names]
        
    for base in base_names:
        name_no_ext = os.path.splitext(base)[0]
        extensions = ['.png', '.PNG', '.jpg', '.JPG', '.jpeg', '.JPEG']
        variations = [name_no_ext + ext for ext in extensions] + [base]
        
        for filename in variations:
            if os.path.exists(filename):
                st.image(filename, caption=caption, use_container_width=True)
                found = True
                break
        if found:
            break
            
    if not found:
        if os.path.exists("office.jpeg"):
            st.image("office.jpeg", caption=caption, use_container_width=True)
        elif os.path.exists("Guma_Passport_Photo.JPG"):
            st.image("Guma_Passport_Photo.JPG", caption=caption, use_container_width=True)

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
    col_img, col_text = st.columns([1, 2.5], gap="medium")
    
    with col_img:
        display_image_safely("Guma_Passport_Photo.JPG", caption="Guma Adolf | Founder & Data Scientist")
            
    with col_text:
        st.markdown("""
        # NG Advisory Co.
        ### *Bridging Heavy Operations & Predictive Data Science*
        
        Welcome to the digital command center of **NG Advisory Co.** Founded on the front lines of UAE logistics and supply chain execution (AED 36M+ scale), our mission is simple: **move beyond static reporting into predictive risk and proactive operational control.**
        """)
    
    st.markdown("---")
    
    st.markdown("### 🖥️ Executive Command Center & Professional Gallery")
    st.markdown("Explore the operational environments and professional milestones driving NG Advisory Co.:")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        display_image_safely("a_Add_even_a_2_screen_.png", caption="Dual-Monitor Command Center & Advanced Analytics Setup")
        st.markdown("**Dual-Screen Execution:** Integrating multi-table SQL queries, Jupyter Notebook Python pipelines, and executive Power BI reporting in real-time.")
        
    with col_p2:
        display_image_safely("a_Change_the_words_on_.png", caption="Analytical Workspace & Data Science Studies")
        st.markdown("**Rigorous Continuous Learning:** Mastering advanced statistics, Bayes' theorem, hypothesis testing, and machine learning architectures from foundational data science coursework.")

    col_p3, col_p4 = st.columns(2)
    with col_p3:
        display_image_safely("office.jpeg", caption="Office Logistics & Operations Environment")
        st.markdown("**Field-Tested Logistics Expertise:** Grounded in heavy UAE supply chain operations managing AED 36M+ scale, freight handling, and exception resolution.")
        
    with col_p4:
        display_image_safely(["California .png", "feb.png"], caption="Environmental & Commercial BI Deliverables")
        st.markdown("**Data-Driven Client Value:** Converting raw datasets (EPA AQI, retail sales, pharmacy records) into actionable executive dashboards and predictive risk models.")

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
    
    display_image_safely("California .png", caption="Seaborn Boxplot: Los Angeles vs. Rest of California AQI")
        
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
    display_image_safely(["chart.png", "plot.png"], caption="Global Carbon Emissions & Country-Level Slicers")

# ==========================================
# 5. UAE ENERGY & CARBON MONOXIDE
# ==========================================
elif menu_selection == "⚡ UAE Energy & Carbon Monoxide":
    st.title("⚡ UAE Energy & Carbon Monoxide Engineering")
    st.markdown("Engineering telemetry analysis covering regional air quality indices, emissions monitoring, and industrial safety thresholds across the Emirates.")
    display_image_safely(["09-10 at 10.36.28 AM.jpeg", "chart.png"], caption="UAE Energy Telemetry & Carbon Monoxide Monitoring")

# ==========================================
# 6. FOUNDATIONAL BI SUITE
# ==========================================
elif menu_selection == "📈 Foundational BI Suite (Retail, Pharmacy, Logistics)":
    st.title("📈 Foundational Business Intelligence Suite")
    st.markdown("Core commercial reporting milestones establishing the bedrock of NG Advisory Co.'s analytical frameworks.")
    
    display_image_safely("feb.png", caption="Early Commercial Retail & Logistics Record Analysis")
        
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
    display_image_safely(["final.png", "my.png"], caption="Tableau Public Wildlife Safety & Spatial Incident Dashboard")

# ==========================================
# 8. WEATHER & LIGHTNING RISK
# ==========================================
elif menu_selection == "🌦️ Weather & Lightning Risk":
    st.title("🌦️ Weather & Lightning Risk Intelligence")
    st.markdown("Predictive analytics mapping environmental hazards against transit schedules to preemptively divert logistics operations.")
    display_image_safely(["Screenshot 2026-02-28 091817.png", "Screenshot proje2.png"], caption="Weather Hazard & Transit Route Risk Mapping")

# ==========================================
# 9. ADVISORY FRAMEWORK & DATA PRODUCTS
# ==========================================
elif menu_selection == "💡 Advisory Framework & Data Products":
    st.title("💡 NG Advisory Framework & Data Products")
    st.markdown("""
    ### Strategic Consulting Methodologies
    NG Advisory Co. helps organizations transition from reactive reporting to proactive operational control.
    """)
    display_image_safely(["a_Change_the_words_on_.png", "Screenshot 2026-03-12 221148.png"], caption="NG Advisory Strategy & Consulting Framework")
    st.markdown("""
    * **Audit & Assess:** Comprehensive evaluation of enterprise data pipelines.
    * **Model & Predict:** Deploying Python-backed statistical risk engines.
    * **Execute & Control:** Closing the loop between insights and ground-level operational execution.
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2026 NG Advisory Co. All Rights Reserved.")
