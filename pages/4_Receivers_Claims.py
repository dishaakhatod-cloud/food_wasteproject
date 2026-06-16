import streamlit as st
import plotly.express as px
from utils.styles import apply_styles
from utils.load_data import load_dashboard_data

# -----------------------------
# Load Data
# -----------------------------
apply_styles()
df = load_dashboard_data()

st.title("🤝 Receivers & Claims Intelligence")
st.caption("Analyze receivers, claim status, and fulfillment patterns.")


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

receiver_types = st.sidebar.multiselect(
    "Receiver Type",
    sorted(df["Receiver_Type"].unique()),
    default=sorted(df["Receiver_Type"].unique())
)

claim_status = st.sidebar.multiselect(
    "Claim Status",
    sorted(df["Status"].unique()),
    default=sorted(df["Status"].unique())
)

filtered = df[
    (df["Receiver_Type"].isin(receiver_types))
    & (df["Status"].isin(claim_status))
]

# -----------------------------
# KPI Cards
# -----------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Receivers",
    filtered["Receiver_ID"].nunique()
)

c2.metric(
    "Claims",
    filtered["Claim_ID"].nunique()
)

c3.metric(
    "Completed",
    (filtered["Status"] == "Completed").sum()
)

c4.metric(
    "Completion %",
    f"{(filtered['Status'] == 'Completed').mean()*100:.1f}%"
)

st.divider()

# -----------------------------
# Charts Row 1
# -----------------------------

left, right = st.columns(2)

with left:

    status_df = (
        filtered["Status"]
        .value_counts()
        .reset_index()
    )

    status_df.columns = ["Status", "Count"]

    fig = px.pie(
        status_df,
        names="Status",
        values="Count",
        hole=0.60,
        color_discrete_sequence=px.colors.qualitative.Set2,
        title="Claim Status Distribution",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:

    receiver_df = (
        filtered["Receiver_Type"]
        .value_counts()
        .reset_index()
    )

    receiver_df.columns = [
        "Receiver_Type",
        "Count",
    ]

    fig = px.bar(
        receiver_df,
        x="Receiver_Type",
        y="Count",
        color="Count",
        color_continuous_scale="Viridis",
        text_auto=True,
        title="Receiver Categories",
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

    hourly = (
        filtered.groupby("Claim_Hour")
        .size()
        .reset_index(name="Claims")
    )

    fig = px.line(
        hourly,
        x="Claim_Hour",
        y="Claims",
        markers=True,
        title="Claims by Hour",
    )

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:

    scatter = px.scatter(
        filtered,
        x="Claim_Hour",
        y="Quantity",
        size="Quantity",
        color="Status",
        hover_name="Receiver_Name",
        title="Claim Hour vs Quantity",
    )

    scatter.update_layout(template="plotly_dark")

    st.plotly_chart(
        scatter,
        use_container_width=True,
    )

st.divider()

# -----------------------------
# Receiver Directory
# -----------------------------

receiver_table = (
    filtered[
        [
            "Receiver_ID",
            "Receiver_Name",
            "Receiver_Type",
            "Receiver_City",
            "Receiver_Contact",
            "Status",
        ]
    ]
    .drop_duplicates()
    .sort_values("Receiver_ID")
)

with st.expander("View Receiver Directory"):

    st.dataframe(
        receiver_table,
        use_container_width=True,
        hide_index=True,
    )