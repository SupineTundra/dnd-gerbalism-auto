import streamlit as st
from random import randint
import requests

st.set_page_config(
    page_title="Гербализм",
    page_icon="🌱",
)
st.header("🌱 Гербализм")
if (st.button("Короткие правила")):
    st.write("Игрок должен пройти проверку Гербализма сложностью 15")
    st.write("Модификатор Гербализма = **МДР / ИНТ + Профессиональный бонус**, если используется набор Гербалиста.")
    st.write("Результат успешной добычи указывается ДМом, броском кубика 1d4 как много ингредиентов добыл игрок в этой местности в соответствии с Экосистемами.")

TERRAIN_ROLL_TABLES_URL = "https://raw.githubusercontent.com/Zendelll/dnd-gerbalism-auto/master/terrain_roll_tables.json"
PLANTS_TABLE_URL = "https://raw.githubusercontent.com/Zendelll/dnd-gerbalism-auto/master/plants_table.json"
COMMON_TERRAIN_NAME = "Обычные"

TERRAIN_ROLL_TABLES = requests.get(TERRAIN_ROLL_TABLES_URL).json()
PLANTS_TABLE = requests.get(PLANTS_TABLE_URL).json()

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
        if name != COMMON_TERRAIN_NAME:
            terrain_names.append(name)
    return st.selectbox('Местность', terrain_names)

def roll_for_plant(selected_terrain):
    roll_result = int(roll("2d6"))
    #Элементальная вода на 2-4 или 10-12 при 76+ на d100
    if ((roll_result >= 2 and roll_result <= 4) or (roll_result >= 10 and roll_result <= 12)) and int(roll("1d100")) > 75:
        return "Элементальная вода".split(", ")

    plant_name = TERRAIN_ROLL_TABLES[selected_terrain][str(roll_result)]
    if plant_name == COMMON_TERRAIN_NAME:
        plant_name = TERRAIN_ROLL_TABLES[COMMON_TERRAIN_NAME][roll("2d6")]
    return plant_name.split(", ")

def write_plant(plant_name_splited):
    #1 - название, 2 - количество, 3 - дополнительная информация
    if len(plant_name_splited) > 1:
        quantity = plant_name_splited[1].split("-")
        if len(quantity) > 1:
            quantity = randint(int(quantity[0]), int(quantity[1]))
        else:
            quantity = quantity[0]
        st.success(f"{plant_name_splited[0]} {quantity}шт")
        if len(plant_name_splited) > 2:
            st.text(plant_name_splited[2])
    else:
        st.success(plant_name_splited[0])

def write_plant_other_description(plant_name_splited, plants_db):
    if (plant_name_splited[0] in plants_db):
        plant = PLANTS_TABLE[plant_name_splited[0]]
        st.header("Описание")
        st.write(plant["description"])
        st.header("Эффект")
        st.write(plant["effect"])
        st.write(f'Сложность - {plant["difficulty"]}')
        st.write(f'Редкость - {plant["rarity"]}')
        st.write(f'Местности - {plant["terrain"]}')



if __name__ == "__main__":
    selected_terrain = terrain_selector(TERRAIN_ROLL_TABLES)
    roll_button = st.button("Ролл!")

    if roll_button:
        plant_name = roll_for_plant(selected_terrain)
        write_plant(plant_name)
        write_plant_other_description(plant_name, PLANTS_TABLE)



    
    
    

