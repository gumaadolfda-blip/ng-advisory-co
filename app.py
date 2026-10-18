import streamlit as st

# Page Configuration
st.set_page_config(
     page_title="Guma Adolf | NG Advisory Co.",
    page_icon="📊",
    layout="wide",
)

# Custom CSS for Elite SaaS Dark Theme Styling
st.markdown(
    """
    <style>
    /* Main Background & Font */
    .stApp {
        background-color: #0b0f19;
        color: #f3f4f6;
    }
    
    /* Hero Title Styling */
    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1.2;
        margin-bottom: 20px;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #9ca3af;
        margin-bottom: 30px;
    }

    /* Metric Card Styling */
    .metric-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #38bdf8;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Sidebar Styling */
    css-1d391kg {
        background-color: #0f172a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.markdown("### 🧭 NG Advisory Co.")
section = st.sidebar.radio(
    "Navigation",
    ["Overview & Systems", "Data Products & Demos", "Advisory Framework"],
)

if section == "Overview & Systems":
  # Hero Section
  st.markdown(
      '<div class="hero-title">Build better business control without'
      " overcomplicating operations.</div>",
      unsafe_allow_html=True,
  )
  st.markdown(
      '<div class="hero-subtitle">SOPs, warehouse controls, reporting'
      " automation, data products, and lightweight applications for growing"
      " businesses that need clarity, structure, and execution velocity. Led"
      " by Guma Adolf.</div>",
      unsafe_allow_html=True,
  )

  st.markdown("---")

  # SaaS Metric Grid matching executive standards
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
            <div class="metric-value" style="font-size: 1.5rem;">Python • SQL • BI</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown("### 📊 Live Operational Control Preview")
  st.write(
      "Real-time pipeline monitoring simulating inventory accuracy and"
      " automated action tracking across UAE supply chains."
  )

  # Progress indicators simulating the reference design
  st.text("Inventory Accuracy (Target: >85%)")
  st.progress(86)

  st.text("SOP Compliance & Governance")
  st.progress(92)

elif section == "Data Products & Demos":
  st.header("📦 Featured Data Products & Simulations")
  st.write(
      "Interactive analytics engines built to optimize fulfillment pathways"
      " and reduce late delivery risks."
  )

  st.markdown("---")
  st.subheader("Interactive Risk Threshold Simulation")
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
  st.write(
      "An elite data strategy isn't a theoretical exercise—it is the operational"
      " backbone of scalable enterprises."
  )

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
