import streamlit as st

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
        <meta property="og:image" content="https://raw.githubusercontent.com/gumaadolfda-blip/ng-advisory-co/main/a_Change_the_words_on_.png">
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

# --- SIDEBAR CONTACT & ADVISORY ---
st.sidebar.markdown("---")
st.sidebar.subheader("📬 Contact & Advisory")
st.sidebar.markdown("**Guma Adolf**")
st.sidebar.markdown("*Founder & Data Scientist, NG Advisory Co.*")
st.sidebar.markdown("📧 [guma.adolf.da@email.com](mailto:guma.adolf.da@email.com)")
st.sidebar.markdown("📱 +971 56 123 3978")
st.sidebar.markdown("🔗 [LinkedIn Profile](https://www.linkedin.com/in/gumadolf)")
st.sidebar.markdown("---")

# Sidebar Navigation containing ALL projects and frameworks
st.sidebar.markdown("### 🧭 NG Advisory Co.")
section = st.sidebar.radio(
    "Navigation",
    [
        "Home & Overview",
        "UAE Energy Supply & CO Analytics",
        "Shipment Performance & Risk BI",
        "Remote Case Study: ROA",
        "Weather & Lightning Risk Analysis",
        "Foundational BI Suite",
        "Data Products & Risk Simulation",
        "Advisory Framework",
    ],
)

if section == "Home & Overview":
    # --- PERSONAL PORTRAIT AT THE TOP (Drives LinkedIn Preview) ---
    st.image(
        "a_Change_the_words_on_.png",
        use_container_width=True,
        caption=(
            "Guma Adolf | Founder & Lead Data Architect, NG Advisory Co."
        ),
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
                <div class="metric-value" style="font-size: 1.3rem;">Python • SQL • BI</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 🖥️ Operational Command Center Environment")
    st.image(
        "a_Add_even_a_2_screen_.png",
        use_container_width=True,
        caption="Multi-Monitor Data Engineering & Analytics Environment",
    )

    st.markdown("### 📊 Live Operational Control Preview")
    st.text("Inventory Accuracy (Target: >85%)")
    st.progress(86)
    st.text("SOP Compliance & Governance")
    st.progress(92)

elif section == "UAE Energy Supply & CO Analytics":
    st.header("⚡ UAE Energy Commodities & Carbon Monoxide Analytics")
    st.write(
        "**Project Type:** Python Data Engineering & Power BI Executive Dashboard Suite"
    )
    st.write(
        "**Scope:** Comprehensive multi-sector examination of UAE energy commodities and historical Carbon Monoxide (CO) concentration trends across emirates and location types (2006–2021)."
    )

    st.markdown("---")
    st.subheader("1. Power BI Executive Overview & Commodity Deep Dive")

    col1, col2 = st.columns(2)
    with col1:
        st.image(
            "Screenshot proje1.png",
            use_container_width=True,
            caption="UAE Energy Commodities Dashboard - Executive Overview[cite: 28]",
        )
    with col2:
        st.image(
            "Screenshot proje2.png",
            use_container_width=True,
            caption="UAE Energy Sector Commodity Deep Dive & Geographic Mapping[cite: 29]",
        )

    st.markdown("---")
    st.subheader("2. Python Jupyter Notebook: Carbon Monoxide (CO) Analysis")

    col_py1, col_py2 = st.columns(2)
    with col_py1:
        st.image(
            "chart.png",
            use_container_width=True,
            caption="Average CO Concentration by Emirate (2006–2016)[cite: 21]",
        )
    with col_py2:
        st.image(
            "final.png",
            use_container_width=True,
            caption=(
                "Average CO Concentration by Location Type (Beside Road vs."
                " Industrial)[cite: 22]"
            ),
        )

elif section == "Shipment Performance & Risk BI":
    st.header("📦 Enterprise Shipment Performance & Risk Intelligence")
    st.write(
        "**Project Type:** Advanced Power BI Supply Chain Control Dashboard"
    )
    st.write(
        "**Scope:** Multi-tab analytics engine tracking shipment status, transit times, origin/destination country flows, and automated late-delivery risk scores."
    )

    st.markdown("---")
    st.image(
        "powerbi.png",
        use_container_width=True,
        caption=(
            "Shipment Performance Dashboard | Executive Overview, Geospatial"
            " Risk Mapping & Route Analysis[cite: 25]"
        ),
    )

    st.markdown("---")
    st.subheader("Core Operational Metrics")
    st.markdown("""
    * **Transit Time Optimization:** Tracking average transit duration (15.38 days) to identify route bottlenecks[cite: 25].
    * **Risk Flagging:** Automated risk scoring and late-shipment monitoring across international corridors (USA, Germany, Japan, China, Brazil, UK)[cite: 25].
    * **Transport Mode Distribution:** Splitting logistics volume across Air, Sea, and Land transport channels[cite: 25].
    """)

elif section == "Remote Case Study: ROA":
    st.header("🌍 Remote Client Engagement: Repair Our Air (ROA)")
    st.write(
        "**Role:** Lead Remote Data Scientist & Statistical Consultant (NG Advisory Co.)"
    )
    st.write(
        "**Client Profile:** Environmental think tank formulating national policy recommendations using EPA Air Quality Index (AQI) data."
    )

    st.markdown("---")
    st.subheader("Exploratory Data Analysis: State-Level AQI Distribution")
    st.write(
        "Utilized Seaborn boxplots (`sns.boxplot`) to profile AQI distributions, isolate skewness, and flag extreme metropolitan outliers across key state jurisdictions prior to formal Welch's t-test evaluations."
    )

    st.image(
        "California .png",
        use_container_width=True,
        caption=(
            "Seaborn Boxplot Analysis | State-Level AQI Distribution, Spread,"
            " and Outlier Detection (California vs. National Peers)[cite: 20]"
        ),
    )

    st.markdown("---")
    st.subheader(
        "Executive Summary & Hypothesis Testing Pipeline (alpha = 0.05)"
    )
    st.write(
        "Executed rigorous statistical evaluations using Python and SciPy (`scipy.stats.ttest_ind`) with Welch's t-test adjustments (`equal_var = False`) to account for unequal variances across regional populations."
    )

elif section == "Weather & Lightning Risk Analysis":
    st.header("⚡ Environmental Risk: Weather & Lightning Strike Analytics")
    st.write(
        "**Project Type:** Exploratory Time-Series & Statistical Distribution Analysis"
    )
    st.write(
        "**Scope:** Examining temporal weather volatility, weekday distributions, and seasonal percentage concentrations of lightning and storm strikes."
    )

    st.markdown("---")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.image(
            "Screenshot 2026-08-23 081053[1].png",
            use_container_width=True,
            caption="Lightning Distribution per Weekday (2018)[cite: 26]",
        )
    with col_w2:
        st.image(
            "Screenshot 2026-08-23 081139[2].png",
            use_container_width=True,
            caption=(
                "Monthly Percentage Concentration of Lightning Strikes"
                " (2016–2018)[cite: 27]"
            ),
        )

elif section == "Foundational BI Suite":
    st.header("📈 Foundational Business Intelligence Suite")
    st.write(
        "**Project Type:** Early Commercial, Pharmacy, and Logistics Power BI Reports"
    )
    st.write(
        "**Scope:** Milestone reporting establishing core competencies in data modeling, DAX measures, geospatial mapping, and commercial dashboard design."
    )

    tab_f1, tab_f2, tab_f3 = st.tabs(
        ["Pharmacy Sales BI", "Logistics Performance BI", "Retail Sales BI"]
    )

    with tab_f1:
        st.subheader("UAE Pharmacy Sales Analysis (Feb 2026)")
        st.image(
            "feb.png",
            use_container_width=True,
            caption="Regional UAE Geographic Mapping & Product Profitability",
        )

    with tab_f2:
        st.subheader("Logistics Performance Overview (Feb 2026)")
        st.image(
            "logistics .png",
            use_container_width=True,
            caption="UAE Route Mapping, Freight Costs & Status Tracking",
        )

    with tab_f3:
        st.subheader("Retail Sales Dashboard (Mar 2026)")
        st.image(
            "my.png",
            use_container_width=True,
            caption=(
                "AED 456K Total Sales, Category Breakdown & Demographic Slicers"
            ),
        )

elif section == "Data Products & Risk Simulation":
    st.header("📦 Featured Data Products & Simulations")
    st.write(
        "Interactive analytics engines built to optimize fulfillment pathways and reduce late delivery risks."
    )

    st.markdown("---")
    st.subheader("Interactive Late Delivery Risk Simulation")
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

elif section == "Advisory Framework":
    st.header("🏛️ Practical Systems & Business Control")
    st.write(
        "An elite data strategy isn't a theoretical exercise—it is the operational backbone of scalable enterprises."
    )
    st.markdown("""
    * **Diagnostic Analytics & Bottleneck Identification:** Uncovering hidden friction points in warehouse execution and cargo transit.
    * **Experimental Design & Validation:** Implementing rigorous hypothesis testing, variance checks, and SciPy statistical validation.
    * **Automation & Control Dashboards:** Building real-time data products that eliminate manual reporting friction.
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #6b7280; font-size: 0.85rem;'>© 2026 NG Advisory Co. | Founded & Architected by Guma Adolf | Connected across the UAE</div>",
    unsafe_allow_html=True,
)
