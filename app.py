import streamlit as st
from random import randint
import requests

TERRAIN_ROLL_TABLES_URL = "https://raw.githubusercontent.com/Zendelll/dnd-gerbalism-auto/master/terrain_roll_tables.json"
PLANTS_TABLE_URL = ""
COMMON_TERRAIN_NAME = "Обычные"

TERRAIN_ROLL_TABLES = requests.get(TERRAIN_ROLL_TABLES_URL).json()
PLANTS_TABLE = requests.get(PLANTS_TABLE_URL).json()


plants = {
    "Кровьтрава": dict(
        description = "",
        rarity = "Обычный",
        effect = "**Специальный (Эффект зелья):** Может быть смешано с любым другим ингредиентом содержащим Эффект Зелья, что бы стать источником еды на 1 день. Не может быть заменён другими ингредиентами.",
        difficulty = 0,
        alch_effect = "effect",
        alch_type = "potion",
        terrain = "Повсеместно"
    ),
    "Хромовая слизь": dict(
        description = "",
        rarity = "Редкий",
        effect = "Специальный (Мод. Зелья & Токсина): Итоговый Эффект после всех вычислений становится абсолютно противоположным. Это зависит от ДМ, относительно каждого зелья/яда.",
        difficulty = 4,
        alch_effect = "mod",
        alch_type = "all",
        terrain = "Берега, Подъземье"
    ),
    "Сушеная Эфедра": dict(
        description = "",
        rarity = "Необычный",
        effect = "Мод. Зелья: Увеличивает тип кости на 1 за любой исцеляющий эффект.",
        difficulty = 2,
        alch_effect = "mod",
        alch_type = "potion",
        terrain = "Пустыни, Горы"
    ),
    "Рвоск": dict(
        description = "",
        rarity = "Обычный",
        effect = "Специальный (Мод. Зелья & Токсина): Задерживает Эффект действия ингредиентов на 1к6 раундов.",
        difficulty = 1,
        alch_effect = "mod",
        alch_type = "all",
        terrain = "Леса, Болота"
    ),
    "Фенхелейвый шелк": dict(
        description = "",
        rarity = "Обычный",
        effect = "Эффект зелья: Стабилизирует температуру тела, что бы выдержать холод или влажность на 1 час. Не может быть заменён другими ингредиентами.",
        difficulty = 2,
        alch_effect = "effect",
        alch_type = "potion",
        terrain = "Арктика, Подземье"
    ),
    "Кисть Генгкоу": dict(
        description = "",
        rarity = "Необычный",
        effect = "Мод. Зелья: Удваивает кол-во костей при броске любого исцеляющего Эффекта, но делит общее кол-во исцеления на 2 (округляя); Затем, разделите получившееся кол-во исцеления за раунд на 2 раунда.",
        difficulty = 2,
        alch_effect = "mod",
        alch_type = "potion",
        terrain = "Холмы, Подземье"
    ),
    "Нектар Гиацинта": dict(
        description = "",
        rarity = "Обычный",
        effect = "Эффект зелья: Уменьшает на 1к6 раундов эффект яда на цели, однако не может убрать его полностью, один раунд всё равно будет нанесён урон от яда.",
        difficulty = 1,
        alch_effect = "effect",
        alch_type = "potion",
        terrain = "Берега, Луга"
    ),
    "Веточка лаванды": dict(
        description = "",
        rarity = "Обычный",
        effect = "Специальный (Мод. Зелья & Токсина): Делает зелье или токсин более стабильный для его безопасного создания .",
        difficulty = -2,
        alch_effect = "mod",
        alch_type = "all",
        terrain = "Берега, Луга, Холмы"
    ),
    "Корень Мандрагоры": dict(
        description = "",
        rarity = "Обычный",
        effect = "Эффект зелья: Ослабляет любую болезнь или яд наполовину в течении 2к12 часов. Препятствует только уже существующим ядам или заболеваниям.Не может быть заменён другими ингредиентами",
        difficulty = 0,
        alch_effect = "effect",
        alch_type = "potion",
        terrain = "Повсеместно"
    ),
    "Корень дикого Шалфея": dict(
        description = "",
        rarity = "Обычный",
        effect = "Эффект Зелья: Исцеляет 2к4+ Мод. Алхимии.",
        difficulty = 0,
        alch_effect = "effect",
        alch_type = "potion",
        terrain = "Повсеместно"
    ),
    "Арктический плющ": dict(
        description = "",
        rarity = "Обычный",
        effect = "Мод. Токсина: Заменяет урон ядом на холод или урон некротической энергией; цель всё еще отравлена на 1 мин. при провале Спас. броска ТЕЛ; Этот токсин всё еще наносит урон ядом при сверке с другими ингредиентами.",
        difficulty = 2,
        alch_effect = "mod",
        alch_type = "poison",
        terrain = "Арктика, Горы"
    ),
    "Шляпка мухомора": dict(
        description = "",
        rarity = "Обычный",
        effect = "Мод. Токсина: Меняет любой эффект яда на не летальный, цель падает без сознания.",
        difficulty = 1,
        alch_effect = "mod",
        alch_type = "poison",
        terrain = "Берега, Болота"
    ),
    "": dict(
        description = "",
        rarity = "",
        effect = "",
        difficulty = 0,
        alch_effect = "mod effect",
        alch_type = "potion poison",
        terrain = ""
    ),
    "": dict(
        description = "",
        rarity = "",
        effect = "",
        difficulty = 0,
        alch_effect = "mod effect",
        alch_type = "potion poison",
        terrain = ""
    ),
    "": dict(
        description = "",
        rarity = "",
        effect = "",
        difficulty = 0,
        alch_effect = "mod effect",
        alch_type = "potion poison",
        terrain = ""
    ),
    "": dict(
        description = "",
        rarity = "",
        effect = "",
        difficulty = 0,
        alch_effect = "mod effect",
        alch_type = "potion poison",
        terrain = ""
    ),
    "": dict(
        description = "",
        rarity = "",
        effect = "",
        difficulty = 0,
        alch_effect = "mod effect",
        alch_type = "potion poison",
        terrain = ""
    ),
    "": dict(
        description = "",
        rarity = "",
        effect = "",
        difficulty = 0,
        alch_effect = "mod effect",
        alch_type = "potion poison",
        terrain = ""
    ),
}

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

    plant_name = TERRAIN_ROLL_TABLES[selected_terrain][str(roll)]
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
        st.text(f"{plant_name_splited[0]} {quantity}шт")
        if len(plant_name_splited) > 2:
            st.text(plant_name_splited[2])
    else:
        st.text(plant_name_splited[0])

def write_plant_other_description(plant_name_splited, plants_db):
    if (plant_name_splited[0] in plants_db):
        plant = plants[plant_name_splited[0]]
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
        write_plant_other_description(plant_name, plants)



    
    
    

