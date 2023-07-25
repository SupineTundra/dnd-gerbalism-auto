import streamlit as st
import requests

PLANTS_TABLE_URL = "https://raw.githubusercontent.com/Zendelll/dnd-gerbalism-auto/master/tables/plants_table.json"
if st.checkbox("Homebrew"):
    PLANTS_TABLE_URL = "https://raw.githubusercontent.com/Zendelll/dnd-gerbalism-auto/master/tables/terrain_roll_tables_homebrew.json"
PLANTS_TABLE = requests.get(PLANTS_TABLE_URL).json()
st.set_page_config(
    page_title="Библиотека", 
    page_icon="🌿"
)
st.header("🌿 Библиотека травника")


if __name__ == "__main__":
    plant_name = st.selectbox('Растение:', dict(sorted(PLANTS_TABLE.items())))
    type = PLANTS_TABLE[plant_name]["alch_type"]
    if type == "magic": 
        color = "blue"
        type = "Магия"
    if type == "potion": 
        color = "red"
        type = "Зелье"
    if type == "poison": 
        color = "green"
        type = "Яд"
    if type == "all":
        color = "orange"
        type = "Любой"
    st.write(f":{color}[{type}]")
    st.success(PLANTS_TABLE[plant_name]["effect"])
    st.warning(PLANTS_TABLE[plant_name]["description"])
    st.code(f'Сложность: {PLANTS_TABLE[plant_name]["difficulty"]} \nРедкость: {PLANTS_TABLE[plant_name]["rarity"]} \nМестности: {PLANTS_TABLE[plant_name]["terrain"]}')
    
