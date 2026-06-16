import streamlit as st
from utils.styles import apply_styles
from utils.load_data import load_dashboard_data
from utils.charts import (
    food_type_bar,
    meal_type_donut,
    claim_status_donut,
    quantity_scatter,
)
apply_styles()
# -----------------------------
# Load Data
# -----------------------------


COLORS = [
    "#166534",  # Dark Green
    "#22C55E",  # Green
    "#4ADE80",  # Light Green
    "#86EFAC",  # Mint
    "#A7F3D0",  # Pale Green
    "#65A30D",  # Olive
]

df = load_dashboard_data()

st.title("📊 Executive Dashboard")
st.caption("High-level overview of food listings, providers, receivers, and claims.")

# -----------------------------
# KPI Cards
# -----------------------------

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Total Claims",
        f"{df['Claim_ID'].nunique():,}"
    )

with k2:
    st.metric(
        "Food Listings",
        f"{df['Food_ID'].nunique():,}"
    )

with k3:
    st.metric(
        "Providers",
        f"{df['Provider_ID'].nunique():,}"
    )

with k4:
    st.metric(
        "Receivers",
        f"{df['Receiver_ID'].nunique():,}"
    )

k5, k6, k7, k8 = st.columns(4)

with k5:
    st.metric(
        "Total Quantity",
        f"{int(df['Quantity'].sum()):,}"
    )

with k6:
    st.metric(
        "Average Quantity",
        f"{df['Quantity'].mean():.1f}"
    )

with k7:
    completed = (df["Status"] == "Completed").sum()
    st.metric(
        "Completed Claims",
        f"{completed:,}"
    )

with k8:
    completion_rate = (
        (df["Status"] == "Completed").mean() * 100
    )
    st.metric(
        "Completion Rate",
        f"{completion_rate:.1f}%"
    )

st.divider()

# -----------------------------
# Charts Row 1
# -----------------------------

left, right = st.columns(2)

with left:
    st.subheader("Food Quantity by Category")
    st.plotly_chart(
        food_type_bar(df),
        use_container_width=True
    )

with right:
    st.subheader("Meal Type Distribution")
    st.plotly_chart(
        meal_type_donut(df),
        use_container_width=True
    )

# -----------------------------
# Charts Row 2
# -----------------------------

left, right = st.columns(2)

with left:
    st.subheader("Claim Status")
    st.plotly_chart(
        claim_status_donut(df),
        use_container_width=True
    )

with right:
    st.subheader("Quantity vs Claim Hour")
    st.plotly_chart(
        quantity_scatter(df),
        use_container_width=True
    )

st.divider()

# -----------------------------
# Recent Records
# -----------------------------

st.subheader("Recent Records")

preview_columns = [
    "Food_Name",
    "Quantity",
    "Food_Type",
    "Meal_Type",
    "Provider_Name",
    "Provider_City",
    "Receiver_Name",
    "Receiver_Type",
    "Status",
]

available_columns = [
    col for col in preview_columns if col in df.columns
]

st.dataframe(
    df[available_columns].head(15),
    use_container_width=True,
    hide_index=True,
)