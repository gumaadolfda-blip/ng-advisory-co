import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Guma Adolf | NG Advisory Co. - Platform",
    page_icon="📊",
    layout="wide",
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
st.sidebar.markdown("*Founder, NG Advisory Co.*")
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
        "UAE Energy Supply Analytics",
        "Remote Case Study: ROA",
        "Data Products & Risk Simulation",
        "Advisory Framework",
    ],
)

if section == "Home & Overview":
    # --- HERO COMMAND CENTER IMAGE (.png) ---
    st.image(
        "a_Add_even_a_2_screen_.png",
        use_container_width=True,
        caption=(
            "NG Advisory Co. Operational Command Center | Multi-Monitor Data"
            " Engineering & Analytics Environment"
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

    st.markdown("### 📊 Live Operational Control Preview")
    st.text("Inventory Accuracy (Target: >85%)")
    st.progress(86)
    st.text("SOP Compliance & Governance")
    st.progress(92)

elif section == "UAE Energy Supply Analytics":
    st.header("⚡ UAE Energy Supply Evolution & Sector Analytics (2008–2021)")
    st.write(
        "**Project Type:** Exploratory Data Analysis & Python Data Engineering Pipeline"
    )
    st.write(
        "**Scope:** Comprehensive multi-sector examination of energy commodities across the United Arab Emirates using Pandas, NumPy, Seaborn, and Matplotlib."
    )

    st.markdown("---")
    st.subheader("Key Analytical Findings & Methodology")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            **1. Data Hygiene & Cleaning Pipeline**
            * Methodically standardized column names and removed trailing whitespaces.
            * Handled missing value imputation and isolated summary rows by filtering `df.dropna(subset=['Year'])`.
            * Converted historical date indicators into clean integer time-series arrays.
            """)
    with col2:
        st.markdown("""
            **2. Advanced Statistical Visualization**
            * Deployed Seaborn boxplots with `hue` parameter mapping to profile distribution spreads and outliers.
            * Utilized faceted multi-panel line plots (`sns.relplot`) with independent Y-axes (`sharey=False`) to clearly isolate sector-specific trajectories.
            """)

    st.markdown("---")
    st.subheader("Sector Breakdown & Insights")

    tab1, tab2, tab3 = st.tabs(
        [
            "Gross Electricity & Gas",
            "Renewable Energy Surge",
            "Crude Oil & NGLs",
        ]
    )

    with tab1:
        st.markdown("### Gross Generated Electricity & Natural Gas")
        st.write(
            "These sectors operate on a massive national scale, driving industrial and urban power generation across Emirates like Abu Dhabi. The boxplot distribution confirms steady, high-volume baseload supply over the 13-year timeline."
        )

    with tab2:
        st.markdown("### Electricity Produced by Renewable Energy")
        st.success(
            "🚀 **Key Growth Trend:** Highlighting a dramatic upward inflection curve starting around 2017–2018, scaling past 6,000 GWh by 2021 as the UAE accelerated its clean energy transition."
        )

    with tab3:
        st.markdown("### Crude Oil & Natural Gas Liquids (NGLs)")
        st.write(
            "Examined extraction and supply stability across reporting entities, validating structural integrity and cyclical adjustments through independent Y-axis scaling."
        )

elif section == "Remote Case Study: ROA":
    st.header("🌍 Remote Client Engagement: Repair Our Air (ROA)")
    st.write(
        "**Role:** Lead Remote Data Scientist & Statistical Consultant (NG Advisory Co.)"
    )
    st.write(
        "**Client Profile:** Environmental think tank formulating national policy recommendations using EPA Air Quality Index (AQI) data."
    )

    st.markdown("---")
    st.subheader("Executive Summary & Hypothesis Testing Pipeline")
    st.write(
        "Executed rigorous statistical evaluations using Python and SciPy (`scipy.stats.ttest_ind`) with Welch's t-test adjustments (`equal_var = False`) to account for unequal variances across regional populations at a 5% level of significance (alpha = 0.05)."
    )

    tab_roa1, tab_roa2, tab_roa3 = st.tabs(
        [
            "1. California Metro Focus",
            "2. Regional Office Site Selection",
            "3. Regulatory Policy Test",
        ]
    )

    with tab_roa1:
        st.markdown("### California Metropolitan Disparity Analysis")
        st.write(
            "**Objective:** Determine if the mean AQI in Los Angeles County is statistically different from the rest of California."
        )
        st.info(
            "**Methodology:** Two-sample Welch's t-test comparing LA County against non-metro California (alpha = 0.05)."
        )
        st.success(
            "**Strategic Recommendation:** Deployed targeted urban mitigation strategies for LA County based on verified statistical divergence."
        )

    with tab_roa2:
        st.markdown("### Regional Office Site Selection (New York vs. Ohio)")
        st.write(
            "**Objective:** Does New York have a lower AQI than Ohio for ROA's next regional hub under resource constraints?"
        )
        st.info(
            "**Methodology:** Independent t-test evaluating mean AQI differences between NY and OH datasets."
        )
        st.success(
            "**Strategic Recommendation:** Provided data-backed site selection guidance for optimal operational placement."
        )

    with tab_roa3:
        st.markdown("### State Regulatory Compliance (Michigan)")
        st.write(
            "**Objective:** Assess whether Michigan's air quality meets or exceeds the federal threshold of a mean AQI of 10 or greater."
        )
        st.info(
            "**Methodology:** Hypothesis testing evaluating sample mean AQI against threshold value under a 95% confidence interval."
        )
        st.success(
            "**Strategic Recommendation:** Delivered compliance impact reports for state-level environmental policy enforcement."
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

    # --- FOCUSED EXECUTION IMAGE (.png) ---
    st.image(
        "a_Change_the_words_on_.png",
        use_container_width=True,
        caption=(
            "Guma Adolf | Focused Analytical Execution & Strategic"
            " Engineering"
        ),
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
