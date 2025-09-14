import streamlit as st
from datetime import date

def init_state():
    defaults = {
        "flt_date": date.today(),
        "flt_cat": "All",
        "rows_per_page_browser": 25,
        "default_category_setting": "All",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v