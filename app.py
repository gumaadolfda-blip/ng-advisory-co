import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Guma Adolf | NG Advisory Co. - Portfolio",
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
        font-size: 3.0rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1.2;
        margin-bottom: 20px;
    }
    .hero-subtitle {
        font-size: 1.15rem;
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

# Sidebar Navigation
st.sidebar.markdown("### 🧭 NG Advisory Co.")
section = st.sidebar.radio(
    "Navigation",
    [
        "Overview & Systems",
        "Remote Client Engagement: ROA",
        "Data Products & Demos",
        "Advisory Framework",
    ],
)

if section == "Overview & Systems":
  st.markdown(
      '<div class="hero-title">Build better business control without'
      " overcomplicating operations.</div>",
      unsafe_allow_html=True,
  )
  st.markdown(
      '<div class="hero-subtitle">SOPs, warehouse controls, reporting'
      " automation, data products, and statistical modeling for enterprises"
      " that need clarity, structure, and execution velocity. Founded &"
      " Architected by Guma Adolf.</div>",
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
            <div class="metric-label">Statistical Significance</div>
            <div class="metric-value">alpha = 0.05</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
  with col3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Core Tech Stack</div>
            <div class="metric-value" style="font-size: 1.3rem;">Python • SciPy • SQL</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif section == "Remote Client Engagement: ROA":
  st.header("🌍 Remote Client Engagement: Repair Our Air (ROA)")
  st.write(
      "**Role:** Lead Remote Data Scientist & Statistical Consultant (NG"
      " Advisory Co.)"
  )
  st.write(
      "**Client Profile:** Environmental think tank formulating national policy"
      " recommendations using EPA Air Quality Index (AQI) data."
  )

  st.markdown("---")
  st.subheader("Executive Summary & Hypothesis Testing Pipeline")
  st.write(
      "Executed rigorous statistical evaluations using Python and SciPy"
      " (`scipy.stats.ttest_ind`) with Welch's t-test adjustments (`equal_var ="
      " False`) to account for unequal variances across regional populations"
      " at a default 5% level of significance (alpha = 0.05)."
  )

  # Three core analytical deliverables from the project
  tab1, tab2, tab3 = st.tabs(
      ["1. California Metro Focus", "2. Regional Office Site Selection", "3. Regulatory Policy Test"]
  )

  with tab1:
    st.markdown("### California Metropolitan Disparity Analysis")
    st.write(
        "**Objective:** Determine if the mean AQI in Los Angeles County is"
        " statistically different from the rest of California to guide"
        " metropolitan-focused policy intervention."
    )
    st.info(
        "**Methodology:** Two-sample Welch's t-test comparing LA County AQI"
        " distribution against California non-metro distribution. Assessed p-value"
        " against alpha = 0.05."
    )
    st.success(
        "**Strategic Recommendation:** Deployed targeted urban mitigation"
        " strategies for LA County based on verified statistical divergence."
    )

  with tab2:
    st.markdown("### Regional Office Site Selection (New York vs. Ohio)")
    st.write(
        "**Objective:** With limited resources, ROA had to choose between New"
        " York and Ohio for their next regional office. Does New York have a"
        " lower AQI than Ohio?"
    )
    st.info(
        "**Methodology:** One-tailed or two-tailed independent t-test evaluating"
        " mean AQI differences between NY and OH datasets using SciPy."
    )
    st.success(
        "**Strategic Recommendation:** Provided data-backed site selection"
        " guidance to optimize operational placement and resource allocation."
    )

  with tab3:
    st.markdown("### State Regulatory Compliance (Michigan)")
    st.write(
        "**Objective:** Assess whether Michigan's air quality meets or exceeds"
        " the federal threshold of a mean AQI of 10 or greater to determine"
        " policy enforceability."
    )
    st.info(
        "**Methodology:** Hypothesis testing evaluating sample mean AQI against"
        " the threshold value of 10 under a 95% confidence interval."
    )
    st.success(
        "**Strategic Recommendation:** Delivered clear compliance impact"
        " reports for state-level environmental policy enforcement."
    )

elif section == "Data Products & Demos":
  st.header("📦 Featured Data Products & Simulations")
  st.write(
      "Interactive analytics engines built to optimize fulfillment pathways"
      " and reduce late delivery risks."
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
        f"⚠️ High Risk Threshold ({risk_slider}): Rerouting logistics"
        " bottlenecks and triggering automated exception alerts."
    )
  else:
    st.success(
        f"✅ Optimal Risk Threshold ({risk_slider}): Fulfillment operations"
        " running smoothly within target thresholds."
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
    "<div style='text-align: center; color: #6b7280; font-size: 0.85rem;'>© 2026"
    " NG Advisory Co. | Founded & Architected by Guma Adolf | Connected"
    " across the UAE</div>",
    unsafe_allow_html=True,
)
