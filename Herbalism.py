import streamlit as st
from random import randint
import json
from scripts.sidebar import init_sidebar, TRANSLATION
st.set_page_config(
    page_title="Herbalism",
    page_icon="🌱",
)
init_sidebar()
PLANTS = {}
TERRAIN = {}
TRANSLATION = TRANSLATION[st.session_state["lang"]]
lang_key_words = TRANSLATION["key_words"]
lang_plants = TRANSLATION["plants"]
with open("tables/plants_table_new.json", "r") as j: PLANTS = json.load(j)
with open("tables/terrain_table.json", "r") as j: TERRAIN = json.load(j)

def roll(dice):
    "dice - строка типа \"8d12\", где 8 - количество дайсов, а 12 - тип"
    dice = dice.split("d")
    result = 0
    for i in range(1, int(dice[0])+1):
        result += randint(1, int(dice[1]))
    return str(result)

def terrain_selector(tables_dict):
    terrain_names = []
    for name, table in tables_dict.items():
        if name != "common":
            terrain_names.append(name)
    return st.selectbox(label = lang_key_words["terrain"]["terrain"], options = terrain_names, format_func = lambda terrain_key: lang_key_words["terrain"][terrain_key])

def roll_for_plant(selected_terrain):
    roll_result = int(roll("2d6"))
    #Элементальная вода на 2-4 или 10-12 при 76+ на d100
    if ((roll_result >= 2 and roll_result <= 4) or (roll_result >= 10 and roll_result <= 12)) and int(roll("1d100")) > 75:
        return ["elemental_water"]

    plant_name = TERRAIN[selected_terrain][str(roll_result)]
    if plant_name == "common":
        plant_name = TERRAIN["common"][roll("2d6")]
    return plant_name.split(", ")

def write_plant(plant_name_splited):
    #1 - название, 2 - количество, 3 - дополнительная информация
    plant_name = lang_plants[plant_name_splited[0]]["name"]
    if len(plant_name_splited) > 1:
        quantity = plant_name_splited[1].split("-")
        if len(quantity) > 1:
            quantity = randint(int(quantity[0]), int(quantity[1]))
        else:
            quantity = quantity[0]
        st.success(f"{plant_name} - {quantity} {TRANSLATION['key_words']['units']}")
        if len(plant_name_splited) > 2:
            st.text(plant_name_splited[2])
    else:
        st.success(plant_name)
    
    plant = PLANTS[plant_name_splited[0]]
    plant_desc = TRANSLATION["plants"][plant_name_splited[0]]
    type = plant["type"]
    if "magic" in type: 
        color = "blue"
        type = lang_key_words["potion_type"]["magic"]
    if "potion" in type: 
        color = "red"
        type = lang_key_words["potion_type"]["potion"]
    if "poison" in type: 
        color = "green"
        type = lang_key_words["potion_type"]["poison"]
    if "all" in type:
        color = "orange"
        type = lang_key_words["potion_type"]["all"]
    st.write(f":{color}[{type}]")
    st.error(plant_desc["effect_description"])
    st.warning(plant_desc["description"])
    terrains = (str)(plant["terrain"]).split(", ")
    translated_terrains = []
    for terrain in terrains: translated_terrains.append(lang_key_words["terrain"][terrain])
    st.code(f'{lang_key_words["difficulty"]}: {plant["difficulty"]} \n{lang_key_words["rarity"]["rarity"]}: {lang_key_words["rarity"][plant["rarity"]]} \n{lang_key_words["terrain"]["terrain"]}: {", ".join(translated_terrains)}')

if __name__ == "__main__":
    st.header(TRANSLATION["pages"]["herbalism"])
    st.markdown(f'<details><summary>{TRANSLATION["buttons"]["short_rules"]}</summary>' + TRANSLATION["text"]["herbalism_rule"] + "</details>", unsafe_allow_html=True)
    selected_terrain = terrain_selector(TERRAIN)
    if st.button(TRANSLATION["buttons"]["roll"]):
        plant_name = roll_for_plant(selected_terrain)
        write_plant(plant_name)



    
    
    

