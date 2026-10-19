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
        "Superstore Supply Chain & Profitability",
        "Global Logistics & Risk Intelligence",
        "Global CO2 Emissions Analytics",
        "Tableau Public Portfolio Suite",
        "UAE Energy Supply & CO Analytics",
        "Remote Case Study: ROA",
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
    st.markdown("### 🖥️ Operational Command Center & Advisory Environment")
    
    col_env1, col_env2 = st.columns(2)
    with col_env1:
        st.image(
            "office.jpeg",
            use_container_width=True,
            caption="NG Advisory Co. Strategic Leadership & Client Consultation Environment[cite: 31]",
        )
    with col_env2:
        st.image(
            "a_Add_even_a_2_screen_.png",
            use_container_width=True,
            caption="Multi-Monitor Data Engineering & Analytics Command Center",
        )

    st.markdown("### 📊 Live Operational Control Preview")
    st.text("Inventory Accuracy (Target: >85%)")
    st.progress(86)
    st.text("SOP Compliance & Governance")
    st.progress(92)

elif section == "Superstore Supply Chain & Profitability":
    st.header("📊 Superstore Supply Chain & Profitability Optimization")
    st.write(
        "**Project Type:** Enterprise Power BI Commercial & Profit Margin Analysis"
    )
    st.write(
        "**Scope:** Granular breakdown of sales revenue by product categories (Furniture, Office Supplies, Technology), segment profitability, regional performance, and shipping mode efficiencies."
    )

    st.markdown("---")
    st.image(
        "Screenshot 2026-07-01 095504.png",
        use_container_width=True,
        caption="Superstore Executive View | Sales Revenue by Category & Profit Margins by Segment[cite: 38]",
    )

    st.markdown("---")
    st.subheader("Key Commercial Insights")
    st.markdown("""
    * **Revenue Concentration:** Analyzed revenue distribution across Furniture, Office Supplies, and Technology product lines[cite: 38].
    * **Segment Margin Review:** Evaluated segment profitability (Consumer vs. Corporate vs. Home Office) to pinpoint high-margin operational sweet spots[cite: 38].
    * **Shipping Efficiency:** Assessed delivery turnaround times across Standard, Second, and First Class shipping modes.
    """)

elif section == "Global Logistics & Risk Intelligence":
    st.header("🌐 Global Logistics & Supply Chain Analysis Dashboard (2026)")
    st.write(
        "**Project Type:** Global Fulfillment Risk & Delivery Optimization Suite"
    )
    st.write(
        "**Scope:** Comprehensive multi-region tracking platform managing AED 36M+ in sales volume, late delivery risk modeling, shipping mode distributions, and global order mapping."
    )

    st.markdown("---")
    st.image(
        "Screenshot 2026-03-12 221148.jpg",
        use_container_width=True,
        caption="Logistics & Supply Chain Analysis Dashboard | Global Order Mapping, Delivery Status Breakdown & Risk Sliders[cite: 36]",
    )

    st.markdown("---")
    st.subheader("Operational Highlights")
    st.markdown("""
    * **Risk Mitigation:** Integrated interactive `late_delivery_risk` slider controls to dynamically filter high-exposure transport corridors[cite: 36].
    * **Delivery Status Breakdown:** Visualized proportions of Advanced Shipping, Late Delivery, Shipping Canceled, and On-Time fulfillment[cite: 36].
    * **Global Geographic Spread:** Mapped order concentration across North America, South America, Europe, Asia, and Australia[cite: 36].
    """)

elif section == "Global CO2 Emissions Analytics":
    st.header("🌍 Global CO2 Emissions & Per Capita Intelligence Dashboard")
    st.write(
        "**Project Type:** Environmental Impact & Macro-Economic Power BI Suite"
    )
    st.write(
        "**Scope:** Cross-country evaluation of historical total CO2 emissions alongside per capita emission rates, featuring dynamic country code filters and search lookup."
    )

    st.markdown("---")
    st.image(
        "Screenshot 2026-06-05 210806.png",
        use_container_width=True,
        caption="CO2 Emissions Executive Overview | Top Historical Countries & Per Capita Rankings[cite: 37]",
    )

    st.markdown("---")
    st.subheader("Key Analytical Takeaways")
    st.markdown("""
    * **Historical Volume Leaders:** Ranked top global economies by total cumulative CO2 output (kt)[cite: 37].
    * **Per Capita Intensity:** Examined per capita metrics highlighting high-intensity regions such as Qatar, UAE, and Kuwait[cite: 37].
    * **Interactive Filtering:** Deployed dynamic search bars and ISO country code slicers (`Country Code`) for targeted geopolitical analysis[cite: 37].
    """)

elif section == "Tableau Public Portfolio Suite":
    st.header("📈 Tableau Public Analytics Portfolio")
    st.write(
        "**Project Type:** Cloud-Published Interactive Vizzes & Spatial Dashboards"
    )
    st.write(
        "**Scope:** Showcasing published Tableau Public works including strike analysis, temporal transit metrics, and global climate visualizations."
    )

    st.markdown("---")
    st.image(
        "WhatsApp Image 2026-09-12 at 8.55.09 AM.jpeg",
        use_container_width=True,
        caption="Tableau Public Creator Profile | GUMA_ADOLF_TABLEAU_PROJECT & CO2 VIZ[cite: 30]",
    )

    st.markdown("---")
    st.subheader("Published Viz Highlights")
    st.markdown("""
    * **GUMA_ADOLF_TABLEAU_PROJECT:** Multi-quarter and multi-year distributional analysis tracking high-volume event metrics[cite: 30].
    * **CO2 VIZ:** Geospatial world map color-coded by per capita emission gradients[cite: 30].
    """)

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
    st.image(
        "California .png",
        use_container_width=True,
        caption="Seaborn Boxplot Analysis | State-Level AQI Distribution & Outlier Detection[cite: 20]",
    )
    st.write(
        "Executed rigorous statistical evaluations using Python and SciPy (`scipy.stats.ttest_ind`) with Welch's t-test adjustments (`equal_var = False`) to account for unequal variances across regional populations (alpha = 0.05)."
    )

elif section == "Foundational BI Suite":
    st.header("📈 Foundational Business Intelligence Suite")
    tab_f1, tab_f2, tab_f3 = st.tabs(
        ["Pharmacy Sales BI", "Logistics Performance BI", "Retail Sales BI"]
    )

    with tab_f1:
        st.subheader("UAE Pharmacy Sales Analysis (Feb 2026)")
        st.image(
            "feb.png",
            use_container_width=True,
            caption="Regional UAE Geographic Mapping & Product Profitability[cite: 13]",
        )

    with tab_f2:
        st.subheader("Logistics Performance Overview (Feb 2026)")
        st.image(
            "WhatsApp Image 2026-09-07 at 10.58.10AM.jpeg",
            use_container_width=True,
            caption="UAE Route Mapping, Freight Costs & Status Tracking",
        )

    with tab_f3:
        st.subheader("Retail Sales Dashboard (Mar 2026)")
        st.image(
            "WhatsApp Image 2026-09-07 at 10.58.22AM.jpeg",
            use_container_width=True,
            caption="AED 456K Total Sales, Category Breakdown & Demographic Slicers",
        )

elif section == "Data Products & Risk Simulation":
    st.header("📦 Featured Data Products & Simulations")
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
