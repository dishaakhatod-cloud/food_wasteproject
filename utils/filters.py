import streamlit as st
import pandas as pd


def apply_sidebar_filters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply common sidebar filters and return the filtered DataFrame.
    """



    st.sidebar.header("Filters")

    provider_categories = sorted(df["Provider_Category"].dropna().unique())
    receiver_types = sorted(df["Receiver_Type"].dropna().unique())
    food_types = sorted(df["Food_Type"].dropna().unique())
    meal_types = sorted(df["Meal_Type"].dropna().unique())
    claim_statuses = sorted(df["Status"].dropna().unique())

    selected_provider = st.sidebar.multiselect(
        "Provider Category",
        provider_categories,
        default=provider_categories,
    )

    selected_receiver = st.sidebar.multiselect(
        "Receiver Type",
        receiver_types,
        default=receiver_types,
    )

    selected_food = st.sidebar.multiselect(
        "Food Type",
        food_types,
        default=food_types,
    )

    selected_meal = st.sidebar.multiselect(
        "Meal Type",
        meal_types,
        default=meal_types,
    )

    selected_status = st.sidebar.multiselect(
        "Claim Status",
        claim_statuses,
        default=claim_statuses,
    )

    filtered_df = df[
        (df["Provider_Category"].isin(selected_provider))
        & (df["Receiver_Type"].isin(selected_receiver))
        & (df["Food_Type"].isin(selected_food))
        & (df["Meal_Type"].isin(selected_meal))
        & (df["Status"].isin(selected_status))
    ]

    return filtered_df
