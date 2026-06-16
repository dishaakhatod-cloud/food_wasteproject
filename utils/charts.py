import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# -----------------------------
# Global Theme
# -----------------------------

COLORS = [
    "#166534",  # Dark Green
    "#22C55E",  # Green
    "#4ADE80",  # Light Green
    "#86EFAC",  # Mint
    "#A7F3D0",  # Pale Green
    "#65A30D",  # Olive
]

PLOT_LAYOUT = dict(
    template="plotly_dark",
    paper_bgcolor="#0F172A",
    plot_bgcolor="#0F172A",
    font=dict(
        family="Arial",
        size=14,
        color="white"
    ),
    margin=dict(l=30, r=30, t=60, b=30),
)


def style_figure(fig):
    fig.update_layout(**PLOT_LAYOUT)
    return fig


# ---------------------------------------------------
# Food Quantity by Food Type
# ---------------------------------------------------

def food_type_bar(df):

    data = (
        df.groupby("Food_Type")["Quantity"]
        .sum()
        .reset_index()
        .sort_values("Quantity", ascending=False)
    )

    fig = px.bar(
        data,
        x="Food_Type",
        y="Quantity",
        color="Quantity",
        color_continuous_scale="Blues",
        text_auto=True,
    )

    return style_figure(fig)


# ---------------------------------------------------
# Meal Type Donut
# ---------------------------------------------------

def meal_type_donut(df):

    data = (
        df.groupby("Meal_Type")["Quantity"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        data,
        names="Meal_Type",
        values="Quantity",
        hole=0.60,
        color_discrete_sequence=COLORS,
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
    )

    return style_figure(fig)


# ---------------------------------------------------
# Claim Status Donut
# ---------------------------------------------------

def claim_status_donut(df):

    status = (
        df["Status"]
        .value_counts()
        .reset_index()
    )

    status.columns = ["Status", "Count"]

    fig = px.pie(
        status,
        names="Status",
        values="Count",
        hole=0.55,
        color_discrete_sequence=[
            "#10B981",
            "#F59E0B",
            "#EF4444",
        ],
    )

    return style_figure(fig)


# ---------------------------------------------------
# Top Providers
# ---------------------------------------------------

def top_providers(df):

    data = (
        df.groupby("Provider_Name")["Quantity"]
        .sum()
        .nlargest(10)
        .sort_values()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="Quantity",
        y="Provider_Name",
        orientation="h",
        color="Quantity",
        color_continuous_scale="Viridis",
        text_auto=True,
    )

    return style_figure(fig)


# ---------------------------------------------------
# Receiver Types
# ---------------------------------------------------

def receiver_types(df):

    data = (
        df["Receiver_Type"]
        .value_counts()
        .reset_index()
    )

    data.columns = ["Receiver_Type", "Count"]

    fig = px.bar(
        data,
        x="Receiver_Type",
        y="Count",
        color="Count",
        color_continuous_scale="Tealgrn",
        text_auto=True,
    )

    return style_figure(fig)


# ---------------------------------------------------
# Quantity Distribution
# ---------------------------------------------------

def quantity_box(df):

    fig = px.box(
        df,
        x="Food_Type",
        y="Quantity",
        color="Food_Type",
        color_discrete_sequence=COLORS,
        points="outliers",
    )

    return style_figure(fig)


# ---------------------------------------------------
# Scatter Plot
# ---------------------------------------------------

def quantity_scatter(df):

    fig = px.scatter(
        df,
        x="Claim_Hour",
        y="Quantity",
        size="Quantity",
        color="Food_Type",
        hover_data=[
            "Food_Name",
            "Provider_Name",
        ],
        color_discrete_sequence=COLORS,
    )

    return style_figure(fig)


# ---------------------------------------------------
# Treemap
# ---------------------------------------------------

def food_treemap(df):

    data = (
        df.groupby(
            ["Food_Type", "Meal_Type"]
        )["Quantity"]
        .sum()
        .reset_index()
    )

    fig = px.treemap(
        data,
        path=["Food_Type", "Meal_Type"],
        values="Quantity",
        color="Quantity",
        color_continuous_scale="RdBu",
    )

    return style_figure(fig)


# ---------------------------------------------------
# Claims by Hour
# ---------------------------------------------------

def hourly_line(df):

    data = (
        df.groupby("Claim_Hour")
        .size()
        .reset_index(name="Claims")
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data["Claim_Hour"],
            y=data["Claims"],
            mode="lines+markers",
            line=dict(
                width=4,
                color="#3B82F6"
            ),
        )
    )

    return style_figure(fig)