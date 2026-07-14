import streamlit as st
from pathlib import Path
from src.lab_simulations_python.i18n import t, language_selector

st.set_page_config(page_title="Physics Lab Simulations", page_icon="assets/LogoUAN.png", layout="wide",)

_logo = Path(__file__).parent / "assets" / "LogoUAN.png"
if _logo.exists():
    st.sidebar.image(str(_logo), width=600)

language_selector()

st.title(t("app_title"))
st.markdown(t("landing_body"))
st.sidebar.success(t("sidebar_select"))
