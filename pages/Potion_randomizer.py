import streamlit as st
from random import randint
import requests

POTION_RANDOMIZER_TABLE_URL = "https://raw.githubusercontent.com/Zendelll/dnd-gerbalism-auto/master/tables/potion_randomizer.json"
POTION_RANDOMIZER_TABLE = requests.get(POTION_RANDOMIZER_TABLE_URL).json()

st.set_page_config(
    page_title="Рандомное зелье", 
    page_icon="🧪"
)
st.header("🧪 Рандомное зелье (WIP)")
st.write("Тут можно зароллить свойства зелья для его описания")
st.write("Источник: https://tentaculus.ru/archive/tables/random_potions.html")

def roll(dice):
    "dice - строка типа \"8d12\", где 8 - количество дайсов, а 12 - тип"
    dice = dice.split("d")
    result = 0
    for i in range(1, int(dice[0])+1):
        result += randint(1, int(dice[1]))
    return str(result)

def roll_table(table_name, dice):
    return POTION_RANDOMIZER_TABLE[table_name][roll(dice)]

if __name__ == "__main__":
    roll_button = st.button("Ролл!")
    if roll_button:
        st.write(f'**Форма сосуда**: {roll_table("Форма", "1d12")}')
        st.write(f'**Материал сосуда**: {roll_table("Материал", "1d12")}')
        st.write(f'**Крышка**: {roll_table("Крышка", "1d6")}')
        st.write(f'**Цвет зелья**: {roll_table("Цвет", "1d10")}')
        st.write(f'**Запах**: {roll_table("Запах", "1d12")}')
        st.write(f'**Интенсивность запаха**: {roll_table("Интенсивность запаха", "1d10")}')
        st.write(f'**Вкус**: {roll_table("Вкус", "1d6")}')
        st.write(f'**Ингридиенты**: {roll_table(roll_table("Типы ингридиентов", "1d8"), "1d6")}, {roll_table(roll_table("Типы ингридиентов", "1d8"), "1d6")}, {roll_table(roll_table("Типы ингридиентов", "1d8"), "1d6")}')
        st.write(f'**Алхимическая реакция**: {roll_table("Реакция", "1d20")}')