import streamlit as st
import json
from scripts.sidebar import init_sidebar, TRANSLATION
st.set_page_config(
    page_title="Library", 
    page_icon="🌿"
)
init_sidebar()
PLANTS = {}
TRANSLATION = TRANSLATION[st.session_state["lang"]]
lang_key_words = TRANSLATION["key_words"]
lang_plants = TRANSLATION["plants"]
with open("tables/plants_table_new.json", "r") as j:
    PLANTS = json.load(j)

if __name__ == "__main__":
    st.header(TRANSLATION["pages"]["plant_library"])
    plant_name = st.selectbox(lang_key_words["plant"], dict(sorted(PLANTS.items())), format_func=lambda plant_key: lang_plants[plant_key]["name"])
    plant = PLANTS[plant_name]
    type = plant["type"]
    if "magic" in type: 
        color = "blue"
        type = TRANSLATION["key_words"]["potion_type"]["magic"]
    if "potion" in type: 
        color = "red"
        type = TRANSLATION["key_words"]["potion_type"]["potion"]
    if "poison" in type: 
        color = "green"
        type = TRANSLATION["key_words"]["potion_type"]["poison"]
    if "all" in type:
        color = "orange"
        type = TRANSLATION["key_words"]["potion_type"]["all"]
    st.write(f":{color}[{type}]")
    st.success(lang_plants[plant_name]["effect_description"])
    st.warning(lang_plants[plant_name]["description"])
    terrains = (str)(plant["terrain"]).split(", ")
    translated_terrains = []
    for terrain in terrains: translated_terrains.append(TRANSLATION["key_words"]["terrain"][terrain])
    st.code(f'{TRANSLATION["key_words"]["difficulty"]}: {plant["difficulty"]} \n{TRANSLATION["key_words"]["rarity"]["rarity"]}: {TRANSLATION["key_words"]["rarity"][plant["rarity"]]} \n{TRANSLATION["key_words"]["terrain"]["terrain"]}: {", ".join(translated_terrains)}')
    
