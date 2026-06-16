import streamlit as st
import pandas as pd
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directory
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed_data"


@st.cache_data(show_spinner=False)
def load_dashboard_data() -> pd.DataFrame:
    """
    Load the main dashboard dataset.
    """
    file_path = PROCESSED_DATA_DIR / "dashboard_data.csv"
    return pd.read_csv(
        file_path,
        parse_dates=["Timestamp", "Expiry_Date"]
    )


@st.cache_data(show_spinner=False)
def load_food_master() -> pd.DataFrame:
    """
    Load the processed food listings dataset.
    """
    file_path = PROCESSED_DATA_DIR / "food_master.csv"
    return pd.read_csv(
        file_path,
        parse_dates=["Expiry_Date"]
    )


@st.cache_data(show_spinner=False)
def load_claims_master() -> pd.DataFrame:
    """
    Load the processed claim dataset.
    """
    file_path = PROCESSED_DATA_DIR / "claims_master.csv"
    return pd.read_csv(
        file_path,
        parse_dates=["Timestamp"]
    )