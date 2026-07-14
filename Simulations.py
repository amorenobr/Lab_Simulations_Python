import streamlit as st
from src.lab_simulations_python.i18n import t, language_selector

st.set_page_config(page_title="Physics Lab Simulations", page_icon="assets/LogoUAN.png", layout="wide",)

language_selector()

st.title(t("app_title"))
st.markdown(t("landing_body"))
st.sidebar.success(t("sidebar_select"))

st.divider()
st.caption(t("developed_by"))
