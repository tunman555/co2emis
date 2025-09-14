import streamlit as st
from utils.state import init_state
from datetime import date

st.set_page_config(
    page_title="Comparison between active and deactivated FUA.",
    page_icon="✅",
    layout="wide",
    #menu_items={"About": "Multi-page Streamlit starter."}
)

init_state()  # ensure default keys exist across pages
# -----------------------------
# Sidebar (global filters)
# -----------------------------
#with st.sidebar:
#    st.image("assets/logo.png", use_container_width=True)
#    st.markdown("### Global Filters")
#    st.date_input("Date", key="flt_date")  # unique keys avoid duplicate-ID error
#    st.selectbox("Category", ["All", "A", "B", "C"], key="flt_cat")
#    st.divider()
#    st.caption("Use the sidebar menu (Pages) to navigate.")

# -----------------------------
# Main: Methodology selector
# -----------------------------
st.title("🏠 Benefit of FUA")
st.subheader("Select methodology")

# Initialize method state once
if "methodology" not in st.session_state:
    st.session_state["methodology"] = 'flight_plan'

# Button row to pick methodology
col1, col2 = st.columns(2)

with col1:
    if st.button("📅 Flight Plan", key="btn_fpl"):
        st.session_state["methodology"] = "flight_plan"
with col2:
    if st.button("⬇️ Radar track", key="btn_radar"):
        st.session_state["methodology"] = "radar_track"

# Visual feedback for selection + reset
sel = st.session_state["methodology"]
st.success(f"Selected methodology: **{sel}**")

st.divider()

# -----------------------------
# Conditional widget groups
# -----------------------------
if sel == "flight_plan":
    st.markdown("### 📅 Comparison between flight_plan")
    st.write("This is the comparison between flight_plan.")
    chosen_date = st.date_input("Pick a date", value=date.today(), key="mtd_date")
    if st.button("Use this date", key="mtd_date_submit"):
        st.toast(f"Date selected: {chosen_date}", icon="✅")
        st.session_state["methodology_result"] = {"type": "date", "value": str(chosen_date)}

elif sel == "radar_track":
    st.markdown("### ⬇️ Comparison between flight_plan")
    options = ["Alpha", "Bravo", "Charlie", "Delta"]
    picked = st.selectbox("Choose an option", options, key="mtd_dropdown")
    if st.button("Use this option", key="mtd_dropdown_submit"):
        st.toast(f"Option selected: {picked}", icon="✅")
        st.session_state["methodology_result"] = {"type": "option", "value": picked}


# -----------------------------
# Show current global + method state
# -----------------------------
with st.expander("🔎 Debug / current selections"):
    st.write("Global filters:")
    st.json({
        "flt_date": str(st.session_state.get("flt_date")),
        "flt_cat": st.session_state.get("flt_cat"),
    })
    st.write("Methodology result:")
    st.json(st.session_state.get("methodology_result", {sel}))