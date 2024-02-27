import streamlit as st
import json

# Effects:
# "dice_type", "effect_addition": "+1" - dice type +1 (1d4 -> 1d6)
# "dice_quantity", "effect_addition": "x2" - dice quantity x2 (4d6 -> 8d6)
# "dice_quantity_nomod", "effect_addition": "x2" - dice quantity x2 (4d6 -> 8d6)
# "dice_quantity_lowduration", "effect_addition": "x2" - dice quantity x2 (4d6 -> 8d6)
# "damage_change" - damage change (have "damage_type") (poison to necrotic) 
# "first_component" - first component
# "last_component" - last component
# "modifier" - modifier
# "base_with_damage" - base with damage (have "damage", "mod", "damage_type" fields)
# "base_static" - base static (can not be altered by other ingridients)
# "base_alterable" - base alterable (can be altered)
TRANSLATION = {}

links = {
    "herbalism": "Herbalism.py",
    "alchemy": "pages/Alchemy.py",
    "plant_library": "pages/Plant_library.py",
    "potion_randomizer": "pages/Potion_randomizer.py",
    "feedback": "pages/feedback.py"
}
with open("tables/translation.json", "r") as j:
    TRANSLATION = json.load(j)

def language_selector():
    if "lang" not in st.session_state:
        st.session_state["lang"] = "ru"
    with st.sidebar:
        col1, col2 = st.columns(2)
        if col1.button("Ru"):
            st.session_state["lang"] = "ru"
            st.rerun()
        if col2.button("En"):
            st.session_state["lang"] = "en"
            st.rerun()

def sidebar_pages():
    st.markdown("""<style>div[data-testid="stSidebarNav"] {display: none;}</style>""", unsafe_allow_html=True)
    pages_names = TRANSLATION[st.session_state["lang"]]["pages"]
    with st.sidebar:
        for name, link in links.items():
            st.page_link(link, label=pages_names[name])

def init_sidebar():
    language_selector()
    sidebar_pages()