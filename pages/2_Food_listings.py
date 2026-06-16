import streamlit as st
import plotly.express as px
from utils.styles import apply_styles
from utils.load_data import load_dashboard_data
apply_styles()

COLORS = [
    "#166534",  # Dark Green
    "#22C55E",  # Green
    "#4ADE80",  # Light Green
    "#86EFAC",  # Mint
    "#A7F3D0",  # Pale Green
    "#65A30D",  # Olive
]

st.set_page_config(
    page_title="Food Listings",
    page_icon="🍽️",
    layout="wide",
)

# -----------------------------
# Load Data
# -----------------------------

df = load_dashboard_data()

st.title("🍽️ Food Listings Analytics")
st.caption("Explore food inventory, quantities, categories, and meal distributions.")

# -----------------------------
# Sidebar Filters
# -----------------------------

food_types = st.sidebar.multiselect(
    "Food Type",
    sorted(df["Food_Type"].unique()),
    default=sorted(df["Food_Type"].unique()),
)

meal_types = st.sidebar.multiselect(
    "Meal Type",
    sorted(df["Meal_Type"].unique()),
    default=sorted(df["Meal_Type"].unique()),
)

filtered = df[
    (df["Food_Type"].isin(food_types))
    & (df["Meal_Type"].isin(meal_types))
]

# -----------------------------
# KPI Cards
# -----------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Unique Foods",
        filtered["Food_Name"].nunique()
    )

with c2:
    st.metric(
        "Total Quantity",
        int(filtered["Quantity"].sum())
    )

with c3:
    st.metric(
        "Average Quantity",
        round(filtered["Quantity"].mean(), 2)
    )

with c4:
    st.metric(
        "Food Categories",
        filtered["Food_Type"].nunique()
    )

st.divider()

# -----------------------------
# Charts
# -----------------------------

left, right = st.columns(2)

with left:

    quantity_chart = (
        filtered.groupby("Food_Name")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        quantity_chart,
        x="Food_Name",
        y="Quantity",
        color="Quantity",
        color_continuous_scale="viridis",
        title="Food Quantity by Item",
        text_auto=True,
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:

    pie = (
        filtered.groupby("Food_Type")["Quantity"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        pie,
        names="Food_Type",
        values="Quantity",
        hole=0.55,
        title="Food Type Distribution",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

# -----------------------------

left, right = st.columns(2)

with left:

    meal = (
        filtered.groupby("Meal_Type")["Quantity"]
        .sum()
        .reset_index()
    )

    fig = px.treemap(
        meal,
        path=["Meal_Type"],
        values="Quantity",
        color="Quantity",
        color_continuous_scale="Blues",
        title="Meal Type Treemap",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:

    fig = px.box(
        filtered,
        x="Food_Type",
        y="Quantity",
        color="Food_Type",
        title="Quantity Distribution",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.divider()

# -----------------------------
# Data Table
# -----------------------------

st.subheader("Food Listings")

display_cols = [
    "Food_Name",
    "Quantity",
    "Food_Type",
    "Meal_Type",
    "Provider_Name",
    "Provider_City",
    "Expiry_Date",
]

display_cols = [c for c in display_cols if c in filtered.columns]

st.dataframe(
    filtered[display_cols],
    use_container_width=True,
    hide_index=True,
)