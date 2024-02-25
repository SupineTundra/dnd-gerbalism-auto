import streamlit as st
import json

TRANSLATION = {}
links = {
    "herbalism": "Herbalism.py",
    "alchemy": "pages/alchemy.py",
    "plant_library": "pages/plant_library.py",
    "potion_randomizer": "pages/potion_randomizer.py",
    "feedback": "pages/feedback.py"
}
with open("tables/translation.json", "r") as j:
    TRANSLATION = json.load(j)

def language_selector():
    if "lang" not in st.query_params.to_dict():
        st.query_params.lang = "ru"
    with st.sidebar:
        col1, col2 = st.columns(2)
        if col1.button("Ru"):
            st.query_params.lang = "ru"
            st.rerun()
        if col2.button("En"):
            st.query_params.lang = "en"
            st.rerun()

def sidebar_pages():
    st.markdown("""<style>div[data-testid="stSidebarNav"] {display: none;}</style>""", unsafe_allow_html=True)
    pages_names = TRANSLATION[st.query_params.lang]["pages"]
    with st.sidebar:
        for name, link in links.items():
            st.page_link(link, label=pages_names[name])

def init_sidebar():
    language_selector()
    sidebar_pages()