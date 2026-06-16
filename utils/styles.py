import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>
        
        /* Reduce top spacing */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
}

/* Remove extra top margin from the main container */
.main > div {
    padding-top: 0rem !important;
}

        /* ===================================================
           GLOBAL BACKGROUND
        =================================================== */

        .stApp,
        [data-testid="stAppViewContainer"],
        .main {
            background: #F7FAF7 !important;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        /* ===================================================
           SIDEBAR
        =================================================== */

        section[data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #14532D 0%,
                #166534 100%
            ) !important;
        }

        section[data-testid="stSidebar"] * {
            color: white !important;
        }

        section[data-testid="stSidebar"] hr {
            background: rgba(255,255,255,0.15);
        }

        /* ===================================================
   HEADINGS
=================================================== */

h1,
h1 span,
[data-testid="stMarkdownContainer"] h1 {
    color: #1F2937 !important;   /* Dark charcoal */
    font-size: 2.8rem !important;
    font-weight: 800 !important;
}

h2,
h3,
h4 {
    color: #14532D !important;
    font-weight: 700 !important;
}

p,
li,
label {
    color: #374151 !important;
}

        /* ===================================================
           KPI CARDS
        =================================================== */

        div[data-testid="metric-container"] {

            background: #FFFFFF !important;

            border: 1px solid #BBF7D0 !important;

            border-radius: 16px !important;

            padding: 18px !important;

            box-shadow: 0px 4px 14px rgba(0,0,0,0.06);

            transition: 0.25s;

        }

        div[data-testid="metric-container"]:hover {

            transform: translateY(-3px);

            border-color: #22C55E !important;

            box-shadow: 0px 8px 22px rgba(34,197,94,0.18);

        }

        div[data-testid="metric-container"] label {

            color: #15803D !important;

            font-weight: 700 !important;

        }

        div[data-testid="metric-container"] div {

            color: #14532D !important;

        }

        /* ===================================================
           DATAFRAMES
        =================================================== */

        .stDataFrame {

            border-radius: 14px;

            overflow: hidden;

            border: 1px solid #D1FAE5;

        }

        /* ===================================================
           BUTTONS
        =================================================== */

        .stButton > button {

            background: #22C55E !important;

            color: white !important;

            border-radius: 10px;

            border: none;

            font-weight: 700;

        }

        .stButton > button:hover {

            background: #16A34A !important;

        }

        /* ===================================================
           MULTISELECT / SELECTBOX FIX
        =================================================== */

        div[data-baseweb="select"] {

            background: white !important;

            border-radius: 10px !important;

            color: #14532D !important;

        }

        div[data-baseweb="select"] > div {

            background: white !important;

            color: #14532D !important;

        }

        div[role="listbox"] {

            background: white !important;

        }

        div[role="option"] {

            background: white !important;

            color: #14532D !important;

        }

        div[role="option"]:hover {

            background: #DCFCE7 !important;

        }

        /* ===================================================
           MULTISELECT TAGS
        =================================================== */

        span[data-baseweb="tag"] {

            background: #DCFCE7 !important;

            border: 1px solid #86EFAC !important;

            color: #166534 !important;

        }

        span[data-baseweb="tag"] * {

            color: #166534 !important;

            fill: #166534 !important;

            font-weight: 600 !important;

        }

        /* ===================================================
           INPUTS
        =================================================== */

        input,
        textarea {

            background: white !important;

            color: #14532D !important;

        }

        /* ===================================================
           HR
        =================================================== */

        hr {

            border: none;

            height: 1px;

            background: #D1FAE5;

        }

        /* ===================================================
           SCROLLBAR
        =================================================== */

        ::-webkit-scrollbar {

            width: 8px;

        }

        ::-webkit-scrollbar-thumb {

            background: #86EFAC;

            border-radius: 8px;

        }

        </style>
        """,
        unsafe_allow_html=True,
    )