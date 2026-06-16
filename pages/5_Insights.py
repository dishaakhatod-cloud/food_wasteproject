import streamlit as st
import plotly.express as px
from utils.styles import apply_styles
from utils.load_data import load_dashboard_data

# ---------------------------------
# Load Data
# ---------------------------------
apply_styles()
df = load_dashboard_data()

st.title("📈 Advanced Insights")
st.caption("Executive analytics and high-level trends across the food waste ecosystem.")


COLORS = [
    "#166534",  # Dark Green
    "#22C55E",  # Green
    "#4ADE80",  # Light Green
    "#86EFAC",  # Mint
    "#A7F3D0",  # Pale Green
    "#65A30D",  # Olive
]
# ---------------------------------
# KPIs
# ---------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Quantity", f"{int(df['Quantity'].sum()):,}")
c2.metric("Avg Quantity", f"{df['Quantity'].mean():.2f}")
c3.metric("Food Types", df["Food_Type"].nunique())
c4.metric("Meal Types", df["Meal_Type"].nunique())

st.divider()

# ---------------------------------
# Row 1
# ---------------------------------

left, right = st.columns(2)

with left:

    city = (
        df.groupby("Provider_City")["Quantity"]
        .sum()
        .nlargest(10)
        .reset_index()
    )

    fig = px.bar(
        city,
        x="Provider_City",
        y="Quantity",
        color="Quantity",
        color_continuous_scale="Turbo",
        title="Top 10 Cities by Quantity",
        text_auto=True,
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig, use_container_width=True)

with right:

    provider = (
        df.groupby("Provider_Name")["Quantity"]
        .sum()
        .nlargest(10)
        .reset_index()
    )

    fig = px.bar(
        provider,
        x="Quantity",
        y="Provider_Name",
        orientation="h",
        color="Quantity",
        color_continuous_scale="Viridis",
        title="Top 10 Providers",
        text_auto=True,
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------
# Row 2
# ---------------------------------

left, right = st.columns(2)

with left:

    tree = (
        df.groupby(
            ["Food_Type", "Meal_Type"]
        )["Quantity"]
        .sum()
        .reset_index()
    )

    fig = px.treemap(
        tree,
        path=["Food_Type", "Meal_Type"],
        values="Quantity",
        color="Quantity",
        color_continuous_scale="RdBu",
        title="Food & Meal Hierarchy",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.box(
        df,
        x="Food_Type",
        y="Quantity",
        color="Food_Type",
        title="Food Quantity Distribution",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------
# Row 3
# ---------------------------------

left, right = st.columns(2)

with left:

    fig = px.scatter(
        df,
        x="Claim_Hour",
        y="Quantity",
        size="Quantity",
        color="Food_Type",
        hover_name="Provider_Name",
        title="Claim Hour vs Quantity",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig, use_container_width=True)

with right:

    monthly = (
        df.groupby("Claim_Day")
        .size()
        .reset_index(name="Claims")
    )

    fig = px.area(
        monthly,
        x="Claim_Day",
        y="Claims",
        title="Claims by Day",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------------------------
# Executive Summary
# ---------------------------------

with st.expander("📄 Executive Summary"):

    st.markdown(f"""
### Key Highlights

- **Total food quantity managed:** **{int(df['Quantity'].sum()):,}**
- **Unique providers:** **{df['Provider_ID'].nunique()}**
- **Unique receivers:** **{df['Receiver_ID'].nunique()}**
- **Unique food categories:** **{df['Food_Type'].nunique()}**
- **Completed claims:** **{(df['Status']=='Completed').sum()}**
- **Pending claims:** **{(df['Status']=='Pending').sum()}**
- **Cancelled claims:** **{(df['Status']=='Cancelled').sum()}**

This dashboard provides a consolidated view of food listings, provider participation,
receiver activity, and claim performance to support operational decision-making.
""")