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


def render_image_safe(path: str, caption: str):
    """Render an image cleanly without crashing if a local asset is missing."""
    try:
        st.image(path, use_container_width=True, caption=caption)
    except Exception:
        st.warning(f"Image asset not found: `{path}` — check exact filename and casing in the repository.")


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
    "Commercial & Apparel Supply Chain BI",
    "Global Freight & Carbon Operations",
    "UAE Logistics & Operations Capabilities",
    "Warehouse & Lead-Time Optimization",
    "UAE NetZero Freight AI (Maritime)",
    "Data Products & Risk Simulation",
    "Client Portal & Feedback",
    "Advisory Framework",
]

section = st.sidebar.radio("Navigation", NAV_ITEMS)

if section == "Home & Overview":
    col_home_img, col_home_text = st.columns([1, 2], gap="medium")
    with col_home_img:
        render_image_safe(
            "NG logo.jpeg",
            "NG Advisory Co. | Guma Adolf, Founder & Lead Data Architect",
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
                <div class="metric-value" style="font-size: 1.3rem;">Python • SQL • BI • AI</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### Featured Project Visuals & Deep-Dive Summaries")
    st.markdown("Each dashboard and report below represents a distinct analytics focus area:")

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        render_image_safe(
            "NG pro1.jpeg",
            "Project 1: Logistics & Supply Chain Performance Dashboard (Jan–Jun 2024)",
        )
        st.markdown(
            """
            **Commercial Revenue, Brand Mix & Fulfillment Visibility:**
            * Tracks **$77M total sales** (+2.1% MoM), **$6.49M returns** (+1.5% MoM across 4K return events), and **Jacket** as the top category ($16.6M), followed by Abaya ($16.2M) and Dress ($10.9M).
            * Breaks down brand performance across **Pharaoh Denim ($20.8M)**, **Luxor Co. ($19.2M)**, and **Nile Wear ($16.0M)**, alongside regional sales led by **North America ($28.7M)** and **Middle East ($19.6M)**.
            * Monitors operational execution with **6.2x inventory turnover**, **3.6-day average delivery time**, **96.1% order fulfillment**, **4.6/5 supplier rating**, **8.7% logistics cost share**, and transport spend split across Road ($45.2M / 58.7%), Sea ($18.6M / 24.1%), Air ($8.9M / 11.6%), and Rail ($4.1M / 5.3%).
            """
        )

    with col_p2:
        render_image_safe(
            "NG PRO2.jpeg",
            "Project 2: Logistics & Supply Chain Dashboard (18.4K Shipments & CO₂ Tracking)",
        )
        st.markdown(
            """
            **Shipment Flow, Carrier Routes & Emissions Monitoring:**
            * Covers **18.4K shipments** (+12.5%), **$5.2M total logistics cost** (-8.3%), **92.6% on-time delivery** (+4.8%), **1.8% returns** (-0.6%), and **1,245 tons of CO₂ emissions** (-10.2%).
            * Maps regional shipment volumes across **Asia (6.1K)**, **North America (4.8K)**, **Europe (3.9K)**, **South America (1.8K)**, **Africa (1.2K)**, and **Oceania (0.6K)**, with end-to-end flow metrics from Suppliers (98% on-time) through Warehouses (96% in-stock), Transportation (92% on-time), and Customers (94% on-time).
            * Evaluates category inventory levels (**Apparel 8.2M**, **Electronics 6.5M**, **Home & Living 5.1M**), top suppliers such as Pharaoh Denim (4,812 orders, 96.4% on-time), key trade corridors like Shanghai → Los Angeles and Mumbai → Dubai, and mode costs (Road 40%, Sea 28%, Air 20%, Rail 8%, Other 4%).
            """
        )

    col_p3, col_p4 = st.columns(2)
    with col_p3:
        render_image_safe(
            "NG PRO3.jpeg",
            "Project 3: UAE Logistics & Operations Capabilities Overview (Fujairah, UAE)",
        )
        st.markdown(
            """
            **UAE Regional Operations & Workflow Automation Scorecard:**
            * Highlights **1,388 total transactions**, **11m average delivery lead time**, **96% on-time delivery rate**, and **98.5% inventory accuracy** with interactive filters for Sector, Emirate, and KPI Type.
            * Compares 12-month operational transaction growth against process accuracy trends and benchmarks delivery performance across **Fujairah, Dubai, Abu Dhabi, and Sharjah**.
            * Summarizes core project outcomes—**Fujairah Port Fuel Analytics** (15% lead time reduction via Python), **Logistics Cost Optimization** (12% cost savings via SQL), and **Warehouse Automation** (20% efficiency increase via Power BI)—alongside tool adoption (Python 22%, SQL 22%, Power BI 15%, Excel 12%) and manual vs. automated workflow bottlenecks.
            """
        )

    with col_p4:
        render_image_safe(
            "NG PRO4.jpeg",
            "Project 4: Logistics Supply Chain Optimization Trend (12-Month Trajectory)",
        )
        st.markdown(
            """
            **Multi-Month Stock Accuracy vs. Turnaround Compression:**
            * Tracks **stock accuracy climbing steadily from 88% in Month 1 to 98.5% by Month 12** (reaching 98% at Month 4 and 99% around Month 11) while **delivery turnaround time drops from 5 days down to 1.9 days (optimized)**.
            * Visualizes how disciplined inventory visibility and cycle-time compression reinforce one another over a full 12-month operational cycle.
            * Highlights four core operational outcomes at the base: **increased stock visibility**, **reduced order cycle time**, **enhanced data-driven decision making**, and **improved customer satisfaction**.
            """
        )

    st.markdown("---")
    st.markdown("### Live Operational Control Preview")
    st.text("Inventory Accuracy (Target: >85%)")
    st.progress(86)
    st.text("SOP Compliance & Governance")
    st.progress(92)

elif section == "Commercial & Apparel Supply Chain BI":
    st.header("Commercial & Apparel Supply Chain Performance (Jan–Jun 2024)")
    render_image_safe(
        "NG pro1.jpeg",
        "Logistics & Supply Chain Performance Dashboard — Commercial & Fulfillment View",
    )
    st.markdown(
        """
        ### In-Depth Breakdown
        * **Commercial Scale:** Generates **$77M in total sales** (+2.1% vs. previous period) with **$6.49M in returns** (+1.5% across **4K returns**), led by **Jacket** ($16.6M), **Abaya** ($16.2M), and **Dress** ($10.9M).
        * **Brand & Regional Mix:** Top brands include **Pharaoh Denim** ($20.8M), **Luxor Co.** ($19.2M), and **Nile Wear** ($16.0M), while regional sales are strongest in **North America** ($28.7M, +8.2%) and the **Middle East** ($19.6M, +4.1%).
        * **Fulfillment & Cost Efficiency:** Delivers a **6.2x inventory turnover**, **3.6-day average delivery time**, **96.1% order fulfillment rate**, **5.2% return rate**, **4.6/5 supplier performance**, and **8.7% logistics cost ratio**, with transport volume concentrated in **Road ($45.2M)** and **Sea ($18.6M)**.
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
        ### In-Depth Breakdown
        * **Headline KPIs:** Tracks **18.4K shipments** (+12.5%), **$5.2M logistics cost** (-8.3%), **92.6% on-time delivery** (+4.8%), **1.8% returns** (-0.6%), and **1,245 tons of CO₂ emissions** (-10.2%) across Jan–Jun 2024.
        * **End-to-End Supply Chain Flow:** Connects **Suppliers** (98% on-time supply), **Warehouses** (96% in-stock rate), **Transportation** (92% on-time transit), and **Customers** (94% on-time delivery), with **72.3% delivered**, **18.1% in transit**, **5.4% pending**, **2.9% delayed**, and **1.3% cancelled**.
        * **Corridors, Categories & Modes:** Highlights **Asia (6.1K)** and **North America (4.8K)** shipment volumes, **Apparel (8.2M)** and **Electronics (6.5M)** stock levels, key routes such as **Shanghai → Los Angeles** (2,184 shipments, 95.2% on-time) and **Mumbai → Dubai** (1,084 shipments, 90.3% on-time), and transport cost share led by **Road (40%)** and **Sea (28%)**.
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
        ### In-Depth Breakdown
        * **Operational KPIs:** Captures **1,388 total transactions**, **11m average delivery lead time**, **96% on-time delivery rate**, and **98.5% inventory accuracy**, paired with interactive filters for Sector, Emirate, and KPI Type.
        * **Emirate & Monthly Trends:** Displays 12-month operational transaction growth alongside process accuracy rates and compares delivery execution across **Fujairah, Dubai, Abu Dhabi, and Sharjah**.
        * **Impact & Automation:** Documents measurable results from **Fujairah Port Fuel Analytics** (15% lead time reduction via Python), **Logistics Cost Optimization** (12% cost savings via SQL), and **Warehouse Automation** (20% efficiency increase via Power BI), alongside tool adoption (**Python 22%**, **SQL 22%**, **Power BI 15%**, **Excel 12%**) and workflow bottleneck diagnostics.
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
        ### In-Depth Breakdown
        * **Accuracy vs. Turnaround Trajectory:** Shows **stock accuracy rising from 88% in Month 1 to 98.5% in Month 12** (peaking near 98% at Month 4 and 99% around Month 11) while **delivery turnaround time improves from 5 days to 1.9 days (optimized)**.
        * **Operational Takeaways:** Demonstrates how tighter stock visibility and streamlined dispatch/turnaround cycles reduce cycle delays over a full year.
        * **Strategic Outcomes:** Anchored by four core pillars—**increased stock visibility**, **reduced order cycle time**, **enhanced data-driven decision making**, and **improved customer satisfaction**.
        """
    )

elif section == "UAE NetZero Freight AI (Maritime)":
    st.markdown(
        '<div class="hero-title">UAE NetZero Freight: Maritime Decarbonization & Supply Chain AI</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hero-subtitle">Multi-Source Machine Learning & Generative AI Engine across 15 UAE Ports (43,110 Port-Day Records) | Aligned with UAE Net Zero 2050 & Federal Decree-Law No. 11/2023.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><div class="metric-label">Projected Annual Fuel ROI</div><div class="metric-value">AED 65.93M</div></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><div class="metric-label">Annual CO₂ Abated</div><div class="metric-value">94,395.7 Tons</div></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><div class="metric-label">JIT Idling Reduction</div><div class="metric-value">15%</div></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><div class="metric-label">UAE Ports Analyzed</div><div class="metric-value">15 Ports</div></div>', unsafe_allow_html=True)

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
    st.subheader("Top UAE Maritime Carbon & Throughput Hotspots")
    port_df = pd.DataFrame(
        {
            "UAE Port": ["Port of Fujairah", "Jebel Ali (Dubai)", "Khalifa Port (Abu Dhabi)", "Khor Fakkan", "Sharjah"],
            "Primary Traffic Profile": ["Energy Tankers & Bunkering", "Container Mega-Hub", "Industrial & Container", "Transshipment Container", "General Cargo & Regional"],
            "Predicted Daily Tonnage": ["216,053 tons/day", "59,012 tons/day", "28,450 tons/day", "24,180 tons/day", "15,920 tons/day"],
            "7-Day CO₂ Saved (15% JIT)": ["55.9 tons", "43.7 tons", "14.2 tons", "13.9 tons", "9.4 tons"],
        }
    )
    st.dataframe(port_df, use_container_width=True, hide_index=True)

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
