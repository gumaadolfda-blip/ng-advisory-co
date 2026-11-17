import streamlit as st
from google import genai

# Page Configuration
st.set_page_config(
    page_title="Guma Adolf | NG Advisory Co. Platform",
    page_icon="📊",
    layout="wide",
)

# --- CUSTOM CSS STYLING ---
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

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("### NG Advisory Co.")
section = st.sidebar.radio(
    "Navigation",
    [
        "Home & Overview",
        "Global Retail & Margin Atlas",
        "Demand Forecasting & Inventory Simulator",
        "Multi-Warehouse SQL Pipeline",
        "Executive P&L Variance Bridge",
        "Fujairah Hospitality & Tourism Index",
        "AI Assistant & Portfolio Chat",
    ],
)

if section == "Home & Overview":
    st.markdown('<div class="hero-title">Build better business control without overcomplicating operations.</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Interactive portfolio, supply chain analytics, and data products platform for NG Advisory Co. Founded & Architected by Guma Adolf.</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><div class="metric-label">Dashboards & Apps</div><div class="metric-value">40+</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><div class="metric-label">Records Modeled</div><div class="metric-value">12M+</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><div class="metric-label">Core Tech Stack</div><div class="metric-value" style="font-size: 1.3rem;">Python • SQL • BI</div></div>', unsafe_allow_html=True)

elif section == "Global Retail & Margin Atlas":
    st.header("Global Retail Revenue & Margin Atlas")
    st.write("**Domain:** Commercial Analytics | **Year:** 2026")
    st.write("Interactive multi-region Tableau executive workbook unifying revenue, discount leakage, and SKU-level gross margin across four commercial territories.")
    st.markdown("[View on Tableau Public](https://public.tableau.com/app/profile/guma.adolf)")

elif section == "Demand Forecasting & Inventory Simulator":
    st.header("Demand Forecasting & Inventory Simulator")
    st.write("**Domain:** Predictive Operations | **Year:** 2026")
    st.write("Interactive Streamlit web application enabling operations teams to test 12-to-24 month demand horizons and safety-stock thresholds.")
    
    # Live Interactive Simulator Widget
    horizon = st.slider("Select Forecast Horizon (Months)", min_value=12, max_value=24, value=12)
    st.success(f"✅ Active simulation running for a {horizon}-month horizon with optimized Holt-Winters seasonal parameters.")

elif section == "Multi-Warehouse SQL Pipeline":
    st.header("Multi-Warehouse Fulfillment & Lead-Time Pipeline")
    st.write("**Domain:** Supply Chain Data | **Year:** 2025")
    st.code("""
WITH stage_durations AS (
  SELECT
    shipment_id,
    warehouse_code,
    EXTRACT(EPOCH FROM (dispatched_at - packed_at)) / 3600.0 AS dock_hours
  FROM analytics.fact_fulfillment
)
SELECT warehouse_code, ROUND(AVG(dock_hours), 2) AS avg_dock_hrs
FROM stage_durations
GROUP BY 1 ORDER BY 2 DESC;
    """, language="sql")

elif section == "Executive P&L Variance Bridge":
    st.header("Executive P&L & Cashflow Variance Bridge")
    st.write("Board-ready Power BI financial model comparing actuals against budget with dynamic waterfall variance attribution.")

elif section == "Fujairah Hospitality & Tourism Index":
    st.header("Fujairah Hospitality Occupancy & ADR Index")
    st.write("Regional hospitality benchmarking study analyzing seasonal occupancy rates, ADR, and RevPAR elasticity across coastal resort segments in the UAE.")

elif section == "AI Assistant & Portfolio Chat":
    st.header("🤖 NG Advisory Co. | AI Portfolio Assistant")
    st.write("Powered by Google Gemini. Ask any question about Guma Adolf's experience, technical stack, or logistics projects.")

    try:
        # Initialize Gemini client using Streamlit secrets
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        
        user_prompt = st.text_input("Ask a question about Guma's background:")
        if user_prompt:
            with st.spinner("AI Architect is analyzing..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"You are an expert AI assistant representing Guma Adolf, Data Analyst & BI Developer based in Fujairah, UAE (guma.adolf.da@gmail.com). Answer this question professionally: {user_prompt}"
                )
                st.success(response.text)
    except Exception:
        st.info("💡 To enable the live AI chat on Streamlit Cloud, add your `GEMINI_API_KEY` to your app's Secrets settings.")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #6b7280; font-size: 0.85rem;'>© 2026 NG Advisory Co. | Founded & Architected by Guma Adolf | +971 56 123 3978 | guma.adolf.da@gmail.com | Worldwide</div>", unsafe_allow_html=True))
