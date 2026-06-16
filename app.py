import streamlit as st
from utils.styles import apply_styles
from utils.load_data import load_dashboard_data

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Food Waste Management Dashboard",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_styles()

# ---------------------------------
# Load Data
# ---------------------------------
df = load_dashboard_data()

# ---------------------------------
# Home Page
# ---------------------------------
st.title("🍽️ Food Waste Management Dashboard")

st.markdown("""
Welcome to the **Food Waste Management Analytics Dashboard**.

Use the navigation menu on the left to explore:

- 📊 Dashboard
- 🍽️ Food Listings
- 🏢 Providers
- 🤝 Receivers & Claims
- 📈 Insights
""")

st.divider()

# ---------------------------------
# Quick Statistics
# ---------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Claims",
        f"{df['Claim_ID'].nunique():,}"
    )

with col2:
    st.metric(
        "Unique Providers",
        f"{df['Provider_ID'].nunique():,}"
    )

with col3:
    st.metric(
        "Unique Receivers",
        f"{df['Receiver_ID'].nunique():,}"
    )

st.divider()

# ---------------------------------
# Dataset Preview
# ---------------------------------
st.subheader("Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True,
    hide_index=True,
)