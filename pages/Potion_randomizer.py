import streamlit as st
from random import randint
import requests

POTION_RANDOMIZER_TABLE_URL = "https://raw.githubusercontent.com/Zendelll/dnd-gerbalism-auto/master/tables/plants_table.json"
POTION_RANDOMIZER_TABLE = requests.get(POTION_RANDOMIZER_TABLE_URL).json()

st.set_page_config(
    page_title="Рандомное зелье", 
    page_icon="🧪"
)
st.header("🧪 Рандомное зелье (WIP)")
st.write("Тут можно зароллить свойства зелья для его описание")
st.write("Источник: https://tentaculus.ru/archive/tables/random_potions.html")