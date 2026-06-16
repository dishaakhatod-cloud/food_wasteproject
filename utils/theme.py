import streamlit as st


def initialize_theme():
    """Initialize the theme if it doesn't exist."""
    if "theme" not in st.session_state:
        st.session_state.theme = "light"


def get_theme():
    """Return the current theme."""
    return st.session_state.theme