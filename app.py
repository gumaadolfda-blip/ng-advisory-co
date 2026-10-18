import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="NG Advisory Co. | Data Products & Systems",
    page_icon="📊",
    layout="wide",
)

# Header Section
st.title("NG Advisory Co.")
st.subheader("Business Control, Data Products & Practical Systems")
st.write(
    "Engineering high-end logistics data science, predictive risk models, and"
    " robust operational systems for UAE enterprises."
)

st.markdown("---")

# Navigation / Section Selector
section = st.sidebar.selectbox(
    "Navigation",
    ["Home & Overview", "Data Products & Portfolios", "Advisory Framework"],
)

if section == "Home & Overview":
  st.header("Welcome to NG Advisory Co.")
  st.write(
      "We bridge advanced statistical modeling (hypothesis testing, risk"
      " index pipelines) with enterprise business control."
  )

  col1, col2, col3 = st.columns(3)
  with col1:
    st.metric(label="Logistics Scale Handled", value="AED 36M+")
  with col2:
    st.metric(label="Core Stack", value="Python, SQL, Power BI")
  with col3:
    st.metric(label="Domain Expertise", value="Supply Chain & Aviation")

  st.markdown("---")
  st.subheader("Featured Capability")
  st.info(
      "👉 Use the sidebar to explore live data products and our business"
      " control frameworks."
  )

elif section == "Data Products & Portfolios":
  st.header("📦 Featured Data Products")

  st.subheader(
      "1. Global Logistics & Supply Chain Risk & Performance Dashboard"
  )
  st.write(
      "End-to-end Power BI & Python analytics platform analyzing over AED 36M"
      " in global transactions with dynamic `Late_delivery_risk` modeling and"
      " geospatial mapping."
  )

  # Interactive Demo Mockup inside Streamlit
  st.markdown("### Interactive Risk Simulation Preview")
  risk_slider = st.slider(
      "Select Late Delivery Risk Threshold", min_value=0, max_value=1, value=0
  )
  st.success(
      f"Current Risk Filter Active at Level: {risk_slider}. Optimizing"
      " fulfillment pathways..."
  )

elif section == "Advisory Framework":
  st.header("🏛️ Practical Systems & Control")
  st.write(
      "An elite data strategy isn't a luxury; it's the backbone of operational"
      " execution."
  )

  st.markdown("""
    * **Diagnostic Analytics:** Uncovering hidden bottlenecks in warehouse and cargo operations.
    * **Experimental Design:** Implementing rigorous A/B testing, variance checks, and SciPy statistical validation.
    * **Automation:** Building real-time dashboards and data products that eliminate manual friction.
    """)

# Footer
st.markdown("---")
st.markdown(
    "© 2026 NG Advisory Co. | Built by Guma Adolf | Connected across the UAE"
)
