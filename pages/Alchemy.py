import streamlit as st
from random import randint
import requests

st.set_page_config(
    page_title="Алхимия", 
    page_icon="⚗️"
)
st.header("⚗️ Алхимия")

POISON_NAME = "Яд"
POTION_NAME = "Зелье"
MAGIC_NAME = "Магическое зелье"
PLANTS_TABLE_URL = "https://raw.githubusercontent.com/Zendelll/dnd-gerbalism-auto/master/tables/plants_table.json"
PLANTS_TABLE = requests.get(PLANTS_TABLE_URL).json()

def get_plants(alchemy_type, type, blacklist = []):
    """alchemy_type - potion, poison или magic
    type - mod или effec
    blacklist - лист трав, которые не надо отображать
    """
    if alchemy_type == "magic":
        magic = [""]
        for name, property in PLANTS_TABLE.items():
            if property["alch_effect"] == "magic" and name != "Элементальная вода" and name not in blacklist:
                magic.append(name)
        return magic
    elif type == "effect": 
        effect = [""]
        for name, property in PLANTS_TABLE.items():
            if property["alch_effect"] == "effect" and (property["alch_type"] == alchemy_type or property["alch_type"] == "all") and name not in blacklist:
                effect.append(name)
        return effect
    else:
        mod = [""]
        for name, property in PLANTS_TABLE.items():
            if property["alch_effect"] == "mod" and (property["alch_type"] == alchemy_type or property["alch_type"] == "all") and name not in blacklist:
                mod.append(name)
        return mod

def write_properties(selected_effect, selected_mod = None, starter_difficulty = 10):
    difficulty = starter_difficulty
    if selected_effect in PLANTS_TABLE:
        st.success(PLANTS_TABLE[selected_effect]["effect"])
        difficulty += PLANTS_TABLE[selected_effect]["difficulty"]
    if selected_mod:
        for name in selected_mod:
            if name in PLANTS_TABLE:
                st.warning(PLANTS_TABLE[name]["effect"])
                difficulty += PLANTS_TABLE[name]["difficulty"]
    st.error(f"Сложность создания - {difficulty}")

if __name__ == "__main__":
    alchemy_type = st.selectbox('Выбери тип:', (POTION_NAME, POISON_NAME, MAGIC_NAME))
    if alchemy_type == POTION_NAME:
        alchemy_type_eng = "potion"
    elif alchemy_type == POISON_NAME:
        alchemy_type_eng = "poison"
    elif alchemy_type == MAGIC_NAME:
        alchemy_type_eng = "magic"

    if alchemy_type_eng == "magic":
        effect = get_plants(alchemy_type_eng, "effect")
        effect.sort()
        st.selectbox('Базовый ингридент:', ["Элементальная вода"])
        selected_effect = st.selectbox('Основной ингридент:', effect)
        write_properties(selected_effect, starter_difficulty=13)
    else:
        effect = get_plants(alchemy_type_eng, "effect")
        effect.sort()
        bloodgrass = None
        if alchemy_type_eng == "potion":
            bloodgrass = st.checkbox("Кровьтрава")
        selected_effect = st.selectbox('Основной ингридент:', effect)
        mod = get_plants(alchemy_type_eng, "mod")
        mod.sort()
        selected_mod = [st.selectbox('Модификатор 1:', mod), st.selectbox('Модификатор 2:', mod), st.selectbox('Модификатор 3:', mod)]
        if bloodgrass: selected_mod.insert(0, 'Кровьтрава')
        write_properties(selected_effect, selected_mod)
