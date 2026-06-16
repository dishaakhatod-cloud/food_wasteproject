import streamlit as st
import plotly.express as px
from utils.styles import apply_styles
from utils.load_data import load_dashboard_data

# -----------------------------
# Load Data
# -----------------------------
apply_styles()
df = load_dashboard_data()

st.title("🏢 Provider Intelligence")
st.caption("Analyze provider activity, categories, cities, and food contributions.")


COLORS = [
    "#166534",  # Dark Green
    "#22C55E",  # Green
    "#4ADE80",  # Light Green
    "#86EFAC",  # Mint
    "#A7F3D0",  # Pale Green
    "#65A30D",  # Olive
]
# -----------------------------
# Sidebar Filters
# -----------------------------

provider_categories = st.sidebar.multiselect(
    "Provider Category",
    sorted(df["Provider_Category"].unique()),
    default=sorted(df["Provider_Category"].unique()),
)

filtered = df[
    df["Provider_Category"].isin(provider_categories)
]

# -----------------------------
# KPI Cards
# -----------------------------

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Providers",
    filtered["Provider_ID"].nunique()
)

k2.metric(
    "Cities",
    filtered["Provider_City"].nunique()
)

k3.metric(
    "Total Quantity",
    int(filtered["Quantity"].sum())
)

k4.metric(
    "Avg Quantity",
    round(filtered["Quantity"].mean(), 2)
)

st.divider()

# -----------------------------
# Charts Row 1
# -----------------------------

left, right = st.columns(2)

with left:

    provider_type = (
        filtered["Provider_Category"]
        .value_counts()
        .reset_index()
    )

    provider_type.columns = [
        "Provider_Category",
        "Count",
    ]

    fig = px.pie(
        provider_type,
        names="Provider_Category",
        values="Count",
        hole=0.55,
        color_discrete_sequence=px.colors.qualitative.Bold,
        title="Provider Category Distribution",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:

    top = (
        filtered.groupby("Provider_Name")["Quantity"]
        .sum()
        .nlargest(10)
        .reset_index()
    )

    fig = px.bar(
        top,
        x="Quantity",
        y="Provider_Name",
        orientation="h",
        color="Quantity",
        color_continuous_scale="Turbo",
        text_auto=True,
        title="Top Providers by Quantity",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

# -----------------------------
# Charts Row 2
# -----------------------------

left, right = st.columns(2)

with left:

    city = (
        filtered.groupby("Provider_City")["Quantity"]
        .sum()
        .nlargest(10)
        .reset_index()
    )

    fig = px.bar(
        city,
        x="Provider_City",
        y="Quantity",
        color="Quantity",
        color_continuous_scale="Viridis",
        text_auto=True,
        title="Top Cities by Quantity",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:

    fig = px.box(
        filtered,
        x="Provider_Category",
        y="Quantity",
        color="Provider_Category",
        title="Quantity Distribution by Provider Category",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.divider()

# -----------------------------
# Provider Directory
# -----------------------------

provider_table = (
    filtered[
        [
            "Provider_ID",
            "Provider_Name",
            "Provider_Category",
            "Provider_City",
            "Provider_Contact",
        ]
    ]
    .drop_duplicates()
    .sort_values("Provider_ID")
)

with st.expander("View Provider Directory"):

    st.dataframe(
        provider_table,
        use_container_width=True,
        hide_index=True,
    )