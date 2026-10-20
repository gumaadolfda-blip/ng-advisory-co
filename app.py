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
        <meta property="og:image" content="https://raw.githubusercontent.com/gumaadolfda-blip/ng-advisory-co/main/Guma_Passport_Photo.JPG">
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
        st.image(
            "Guma_Passport_Photo.JPG",
            use_container_width=True,
            caption="Guma Adolf | Founder & Lead Data Architect, NG Advisory Co.",
        )
    with col_home_text:
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
    st.markdown("### Executive Command Center & Professional Gallery")
    st.markdown("Explore the operational environments and professional milestones driving NG Advisory Co.:")

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.image(
            "NG.jpeg",
            use_container_width=True,
            caption="NG Advisory Co. Executive Command Center & Strategic Leadership Environment",
        )
        st.markdown("**Field-Tested Logistics Execution & Advisory HQ:** Grounded in global supply chain operations managing AED 36M+ scale, freight handling, and exception resolution.")

    with col_p2:
        st.image(
            "office.jpeg",
            use_container_width=True,
            caption="NG Advisory Co. Strategic Leadership & Client Consultation Environment",
        )
        st.markdown("**Client Consultation & Strategic Advisory:** Dedicated workspace tailored for executive sessions, operational audits, and stakeholder alignment.")

    col_p3, col_p4 = st.columns(2)
    with col_p3:
        st.image(
            "MULT.jpeg",
            use_container_width=True,
            caption="NG Advisory Co. Enterprise Operations & Team Workspace",
        )
        st.markdown("**Collaborative Intelligence & Execution:** A unified advisory environment integrating enterprise analytics, continuous development, and cross-functional logistics execution.")

    with col_p4:
        st.image(
            "Guma_Passport_Photo.JPG",
            use_container_width=True,
            caption="Guma Adolf | Founder & Lead Data Architect, NG Advisory Co.",
        )
        st.markdown("**Vision & Leadership:** Directing enterprise digital transformation, bridging heavy operational logistics with modern predictive data science.")

    st.markdown("---")
    st.markdown("### Live Operational Control Preview")
    st.text("Inventory Accuracy (Target: >85%)")
    st.progress(86)
    st.text("SOP Compliance & Governance")
    st.progress(92)

elif section == "Superstore Supply Chain & Profitability":
    st.header("Superstore Supply Chain & Profitability Optimization")
    st.write(
        "**Project Type:** Enterprise Power BI Commercial & Profit Margin Analysis"
    )
    st.write(
        "**Scope:** Granular breakdown of sales revenue by product categories, segment profitability, regional performance, and shipping mode efficiencies."
    )

    st.markdown("---")
    col_sup1, col_sup2 = st.columns(2)
    with col_sup1:
        st.image(
            "Screenshot 2026-07-01 095504.png",
            use_container_width=True,
            caption="Superstore Executive View | Sales Revenue & Segment Margins",
        )
    with col_sup2:
        st.image(
            "Screenshot 2026-07-01 095527.png",
            use_container_width=True,
            caption="Average Days to Ship by Ship Mode",
        )

    st.markdown("---")
    st.subheader("Product Performance Breakdown")
    st.image(
        "Screenshot 2026-02-27 071707.png",
        use_container_width=True,
        caption="Sum of Price, Total Revenue, and Units by Product Category",
    )

elif section == "Global Logistics & Risk Intelligence":
    st.header("Global Logistics & Supply Chain Analysis Dashboard (2026)")
    st.write(
        "**Project Type:** Global Fulfillment Risk & Delivery Optimization Suite"
    )
    st.write(
        "**Scope:** Comprehensive multi-region tracking platform managing AED 36M+ in sales volume, late delivery risk modeling, shipping mode distributions, and global order mapping."
    )

    st.markdown("---")
    col_log1, col_log2 = st.columns(2)
    with col_log1:
        st.image(
            "Screenshot 2026-03-12 221148.png",
            use_container_width=True,
            caption="Global Supply Chain Dashboard with Risk Slider & Mapping",
        )
    with col_log2:
        st.image(
            "powerbi.png",
            use_container_width=True,
            caption="Shipment Performance Dashboard | Geospatial Risk & Route Analysis",
        )

    st.markdown("---")
    st.subheader("Foundational Logistics Views & Route Mapping")
    col_lsub1, col_lsub2 = st.columns(2)
    with col_lsub1:
        st.image(
            "logistics.png",
            use_container_width=True,
            caption="Logistics Performance Overview (Feb 2026)",
        )
    with col_lsub2:
        st.image(
            "Screenshot 2026-02-28 093719.jpg",
            use_container_width=True,
            caption="Detailed Freight Cost & Status Breakdown",
        )

elif section == "Global CO2 Emissions Analytics":
    st.header("Global CO2 Emissions & Per Capita Intelligence Dashboard")
    st.write(
        "**Project Type:** Environmental Impact & Macro-Economic Power BI Suite"
    )
    st.write(
        "**Scope:** Cross-country evaluation of historical total CO2 emissions alongside per capita emission rates, featuring dynamic country code filters."
    )

    st.markdown("---")
    st.image(
        "Screenshot 2026-06-05 210806.png",
        use_container_width=True,
        caption="CO2 Emissions Executive Overview | Top Historical Countries & Per Capita Rankings",
    )

elif section == "UAE Energy & Carbon Monoxide Engineering":
    st.header("Energy Commodities & Carbon Monoxide Analytics")
    st.write(
        "**Project Type:** Python Data Engineering & Power BI Executive Dashboard Suite"
    )
    st.write(
        "**Scope:** Comprehensive multi-sector examination of energy commodities and historical Carbon Monoxide (CO) concentration trends across locations."
    )

    st.markdown("---")
    st.subheader("1. Power BI Executive Dashboards")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.image(
            "Screenshot proje1.png",
            use_container_width=True,
            caption="Energy Commodities Dashboard - Executive Overview",
        )
    with col_e2:
        st.image(
            "Screenshot proje2.png",
            use_container_width=True,
            caption="Energy Sector Commodity Deep Dive & Geographic Mapping",
        )

    st.markdown("---")
    st.subheader("2. Python Jupyter Notebook Analysis (CO Concentrations)")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.image(
            "chart.png",
            use_container_width=True,
            caption="Average CO Concentration Trend (2006–2016)",
        )
        st.image(
            "plot.png",
            use_container_width=True,
            caption="Annual Average Carbon Monoxide Trends",
        )
    with col_c2:
        st.image(
            "final.png",
            use_container_width=True,
            caption="Average CO Concentration by Location Type",
        )
        st.image(
            "plot2.png",
            use_container_width=True,
            caption="Statistical Summary Table: CO by Location Type",
        )

elif section == "Remote Case Study: ROA":
    st.header("Remote Client Engagement: Repair Our Air (ROA)")
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
        caption="Seaborn Boxplot Analysis | State-Level AQI Distribution & Outlier Detection",
    )
    st.write(
        "Executed rigorous statistical evaluations using Python and SciPy (`scipy.stats.ttest_ind`) with Welch's t-test adjustments (`equal_var = False`) to account for unequal variances across regional populations (alpha = 0.05)."
    )

elif section == "Tableau Public & Wildlife Analytics":
    st.header("Tableau Public Portfolio & Wildlife Incident Analytics")
    st.write(
        "**Project Type:** Cloud-Published Interactive Vizzes & Spatial Aviation Safety Analysis"
    )
    st.write(
        "**Scope:** Published Tableau Public vizzes (`GUMA_ADOLF_TABLEAU_PROJECT`, `CO2 VIZ`) alongside multi-year US bird strikes and wildlife incident density mapping."
    )

    st.markdown("---")
    st.image(
        "WhatsApp Image 2026-09-12 at 8.55.09 AM.jpeg",
        use_container_width=True,
        caption="Tableau Public Creator Profile | Published Vizzes Showcase",
    )

    st.markdown("---")
    st.subheader("US Wildlife & Bird Strikes Analytics Suite")
    col_wld1, col_wld2 = st.columns(2)
    with col_wld1:
        st.image(
            "WhatsApp Image 2026-09-07 at 10.58.27 AM.jpeg",
            use_container_width=True,
            caption="Wildlife Strike Frequency Bins (Tableau)",
        )
        st.image(
            "WhatsApp Image 2026-09-07.jpeg",
            use_container_width=True,
            caption="Sum of Number of Strikes Trend Line (2016–2018)",
        )
    with col_wld2:
        st.image(
            "WhatsApp Image 2026-09-07 at 10.58.29AM.jpeg",
            use_container_width=True,
            caption="US Spatial Density Incident Mapping",
        )
        st.image(
            "09-10 at 10.36.28 AM.jpeg",
            use_container_width=True,
            caption="Seoul Bike Rentals Time-Series Analysis",
        )

elif section == "Weather & Lightning Risk Analysis":
    st.header("Environmental Risk: Weather & Lightning Strike Analytics")
    st.write(
        "**Project Type:** Exploratory Time-Series & Statistical Distribution Analysis"
    )
    st.write(
        "**Scope:** Examining temporal weather volatility, weekday distributions, and seasonal percentage concentrations of lightning and storm strikes."
    )

    st.markdown("---")
    col_ltg1, col_ltg2 = st.columns(2)
    with col_ltg1:
        st.image(
            "Screenshot 2026-08-23 081053[1].png",
            use_container_width=True,
            caption="Lightning Distribution per Weekday (2018)",
        )
    with col_ltg2:
        st.image(
            "Screenshot 2026-08-23 081139[2].png",
            use_container_width=True,
            caption="Monthly Percentage Concentration of Lightning Strikes (2016–2018)",
        )

elif section == "Foundational BI Suite (Pharmacy & Retail)":
    st.header("Foundational Business Intelligence Suite")
    st.write(
        "**Project Type:** Early Commercial, Pharmacy, and Logistics Power BI Reports"
    )

    tab_f1, tab_f2, tab_f3 = st.tabs(
        ["Pharmacy Sales BI", "Retail Sales BI", "Logistics Milestones"]
    )

    with tab_f1:
        st.subheader("Pharmacy Sales Analysis")
        st.image(
            "feb.png",
            use_container_width=True,
            caption="Geographic Mapping & Product Profitability",
        )
        st.image(
            "Screenshot 2026-02-27 073605.png",
            use_container_width=True,
            caption="Pharmacy Sales Dashboard Detailed View",
        )

    with tab_f2:
        st.subheader("Retail Sales Dashboard")
        st.image(
            "my.png",
            use_container_width=True,
            caption="AED 456K Total Sales, Category Breakdown & Demographic Slicers",
        )
        st.image(
            "WhatsApp Image 2026-09-07 at 10.58.22AM.jpeg",
            use_container_width=True,
            caption="Retail Sales Distribution & Date Filtering",
        )

    with tab_f3:
        st.subheader("Early Logistics & Transport Reports")
        st.image(
            "WhatsApp Image 2026-09-07 at 10.58.10AM.jpeg",
            use_container_width=True,
            caption="Logistics Performance Overview Map & Weights",
        )

elif section == "Data Products & Risk Simulation":
    st.header("Featured Data Products & Simulations")
    st.write(
        "Interactive analytics engines built to optimize fulfillment pathways and reduce late delivery risks."
    )

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
        "Contact Us"
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
            # Create Account Form
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
        st.markdown("""
        * **Founder & Lead Data Architect:** Guma Adolf
        * **Direct Mobile / WhatsApp:** +971 56 123 3978
        * **Official Email:** guma.adolf.da@gmail.com
        * **Global Network:** LinkedIn (`https://www.linkedin.com/in/gumadolf`)
        """)
        st.info("We respond to all global client inquiries within 24 hours.")

elif section == "Advisory Framework":
    st.header("Practical Systems & Business Control")
    st.markdown("""
    * **Diagnostic Analytics & Bottleneck Identification:** Uncovering hidden friction points in warehouse execution and cargo transit.
    * **Experimental Design & Validation:** Implementing rigorous hypothesis testing, variance checks, and SciPy statistical validation.
    * **Automation & Control Dashboards:** Building real-time data products that eliminate manual reporting friction.
    """)

# Footer with updated contact info, year 2026, and Worldwide branding
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #6b7280; font-size: 0.85rem;'>© 2026 NG Advisory Co. | Founded & Architected by Guma Adolf | +971 56 123 3978 | guma.adolf.da@gmail.com | Worldwide</div>",
    unsafe_allow_html=True,
)
