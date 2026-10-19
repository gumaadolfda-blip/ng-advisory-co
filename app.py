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
        "UAE Energy Supply Analytics",
        "Foundational Pharmacy BI",
        "Foundational Logistics BI",
        "Foundational Retail Sales BI",
        "Seoul Bike Rentals Analytics",
        "US Wildlife & Bird Strikes Analytics",
        "Remote Case Study: ROA",
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

elif section == "Foundational Pharmacy BI":
    st.header(
        "📈 Foundational Case Study: UAE Pharmacy Sales Analysis (Power BI)"
    )
    st.write(
        "**Project Type:** Foundational Business Intelligence & Regional Geographic Mapping (February 2026)"
    )
    st.write(
        "**Scope:** Early exploratory reporting mapping out multi-region pharmacy sales performance across the UAE, tracking product-level profitability for key medical commodities, and establishing foundational data visualization frameworks."
    )

    st.markdown("---")
    st.subheader(
        "Pharmacy_Sales_Analysis_FEB2026_Full_Report_2 Dashboard Preview"
    )

    st.image(
        "feb.png",
        use_container_width=True,
        caption=(
            "Foundational Power BI Report (Feb 2026) | Regional UAE Geographic"
            " Mapping & Product Profitability Metrics"
        ),
    )

    st.markdown("---")
    st.subheader("Key Takeaways & Evolution")
    st.markdown("""
    * **Geographic Mapping Foundations:** Utilized built-in Power BI mapping tools to anchor multi-hub performance across UAE coordinates.
    * **Product Profitability Breakdown:** Analyzed sales distribution using clear card visuals, pie charts, and bar distributions to isolate high-performing inventory items.
    * **The Compounding Journey:** Serving as an early milestone in data visualization before scaling into advanced Python automation, SQL querying, and enterprise risk modeling under NG Advisory Co.
    """)

elif section == "Foundational Logistics BI":
    st.header(
        "🚚 Foundational Case Study: UAE Logistics Performance Overview (Power BI)"
    )
    st.write(
        "**Project Type:** Supply Chain Visibility & Route Performance Dashboard (February 2026)"
    )
    st.write(
        "**Scope:** Operational intelligence dashboard tracking multi-hub freight distribution, delivery statuses (Delayed, Delivered, On-Time), and product-category weights across UAE transport routes."
    )

    st.markdown("---")
    st.subheader(
        "Logistics Performance Overview-February 2026 Dashboard Preview"
    )

    st.image(
        "WhatsApp Image 2026-09-07 at 10.58.10AM.jpeg",
        use_container_width=True,
        caption=(
            "Foundational Logistics Report (Feb 2026) | UAE Route Mapping,"
            " Freight Costs & Status Tracking"
        ),
    )

    st.markdown("---")
    st.subheader("Key Takeaways & Operational Value")
    st.markdown("""
    * **Route Status Monitoring:** Visualized live destination tracking to isolate delivery exceptions and operational delays across the UAE.
    * **Weight & Category Allocation:** Evaluated freight distribution across heavy categories like Construction, Electrical, and Pharmacy supply chains.
    * **Operational Foundation:** Demonstrates deep domain familiarity with real-world freight handling before expanding into predictive Python simulation models.
    """)

elif section == "Foundational Retail Sales BI":
    st.header("🛒 Foundational Case Study: Retail Sales Dashboard (Power BI)")
    st.write(
        "**Project Type:** Commercial Retail Analytics & Revenue Intelligence (March 2026)"
    )
    st.write(
        "**Scope:** Early commercial sales report analyzing AED 456,000 in total revenue across product categories (Electronics, Clothing, Beauty) with interactive date slicers and gender demographic filtering."
    )

    st.markdown("---")
    st.subheader("My_First_Retail_Dashboard_Final Dashboard Preview")

    st.image(
        "WhatsApp Image 2026-09-07 at 10.58.22AM.jpeg",
        use_container_width=True,
        caption=(
            "Foundational Retail Sales Report (Mar 2026) | AED 456K Total Sales,"
            " Category Breakdown & Demographic Slicers"
        ),
    )

    st.markdown("---")
    st.subheader("Key Takeaways & Commercial Insights")
    st.markdown("""
    * **Revenue Tracking:** Centralized total sales performance (AED 456,000) using executive KPI card visuals.
    * **Multi-Category Distribution:** Assessed revenue split across Electronics, Clothing, and Beauty sectors via dynamic pie and column charts.
    * **Interactive Slicing:** Integrated date timeline controls (`1/1/2023` to `1/1/2024`) and gender filters to enable targeted commercial data discovery.
    """)

elif section == "Seoul Bike Rentals Analytics":
    st.header("🚲 Tableau Analytics: Seoul Bike Rentals (2018)")
    st.write(
        "**Project Type:** Time-Series & Demand Distribution Analysis (Tableau Public)"
    )
    st.write(
        "**Scope:** Comprehensive temporal exploration of public bike-sharing usage across weekdays, hours, and seasonal variations to identify peak transit windows and low-traffic operational lulls."
    )

    st.markdown("---")
    st.subheader("Weekday & Hourly Demand Patterns")

    st.image(
        "WhatsApp Image 2026-09-07 at 10.58.27 AM.jpeg",
        use_container_width=True,
        caption=(
            "Seoul Average Bike Rentals per Hour on Weekdays (2018) | Peak Commute Hours & Low-Traffic Windows"
        ),
    )

    st.markdown("---")
    st.subheader("Key Analytical Insights")
    st.markdown("""
    * **Commuter Peaks:** Identified sharp morning and evening rental spikes corresponding to weekday transit habits.
    * **Maintenance Windows:** Pinpointed low-demand operational windows (such as 9 AM to 3 PM) ideal for bike redistribution and fleet servicing.
    * **Gradient Visual Encoding:** Utilized color-mapped density bars (`SUM(Rented Bike Count)`) to instantly highlight high-volume hours.
    """)

elif section == "US Wildlife & Bird Strikes Analytics":
    st.header("🦅 Tableau Analytics: US Wildlife & Bird Strikes (2016–2018)")
    st.write(
        "**Project Type:** Spatial Density Mapping & Multi-Year Strike Trend Analysis (Tableau Public)"
    )
    st.write(
        "**Scope:** Large-scale analysis of aviation safety incident records, mapping spatial strike concentrations across US coordinates and examining multi-year volume trajectories."
    )

    st.markdown("---")
    st.subheader("Geographic Density & Multi-Year Incident Trends")

    st.image(
        "WhatsApp Image 2026-09-07 at 10.58.29AM.jpeg",
        use_container_width=True,
        caption=(
            "US Wildlife Strike Density Mapping & Temporal Incident Trends (2016–2018)"
        ),
    )

    st.markdown("---")
    st.subheader("Key Takeaways & Safety Intelligence")
    st.markdown("""
    * **Spatial Risk Mapping:** Deployed density-based geographic maps to identify high-concentration collision zones across regional flight paths.
    * **Longitudinal Trends:** Tracked annual strike fluctuations between 2016 and 2018 to evaluate safety intervention outcomes.
    * **Aviation Logistics Relevance:** Demonstrates advanced capability in handling complex, multi-million record safety datasets for operational risk mitigation.
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
