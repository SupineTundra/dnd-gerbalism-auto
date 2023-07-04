import streamlit as st
import json
from random import randint

COMMON_TERRAIN_NAME = "Обычные"

with open('terrain_roll_tables.json', encoding='utf-8') as f:
  terrain_roll_tables = json.load(f)


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

tables = {
    "Обычные": {
        2: "Корень Мандрагоры",
        3: "Ртутный лишайник",
        4: "Ртутный лишайник",
        5: "Корень дикого Шалфея",
        6: "Корень дикого Шалфея",
        7: "Кровьтрава",
        8: "Лепестки змееуста",
        9: "Лепестки змееуста",
        10: "Семена Молочая",
        11: "Семена Молочая",
        12: "Корень Мандрагоры"
    },
    "Арктика": {
        2: "Серебряный Гибискус",
        3: "Порошок морплоти",
        4: "Сердце Жлезодрева",
        5: "Замороженные саженцы, 2",
        6: "Обычные",
        7: "Обычные",
        8: "Обычные",
        9: "Арктический плющ, 2",
        10: "Фенхелейвый шёлк",
        11: "Дьявольский плющ",
        12: "Корень пустоты"
    },
    "Берега/Подводная среда": {
        2: "Водополох, 1-2",
        3: "Шляпка мухомора, 1, только на берегу",
        4: "Нектар Гиацинта",
        5: "Хромовая слизь, 1-2",
        6: "Обычные",
        7: "Обычные",
        8: "Обычные",
        9: "Веточка лаванды, 1, только на берегу",
        10: "Синий Кривожаб, 1, только на берегу",
        11: "Зловонная луковица",
        12: "Ко-Глонд, 1-2"
    },
    "Пустыня": {
        2: "Ко-Глонд",
        3: "Корень Стрела",
        4: "Высушенная Эфедра",
        5: "Сок кактуса, 2",
        6: "Обычные",
        7: "Обычные",
        8: "Обычные",
        9: "Цветы Дракуса",
        10: "Бобы Сцили",
        11: "Ягоды Шипоцвета",
        12: "Корень пустоты, 1, Дополнительно находится 1 Элементальная вода"
    },
    "Леса": {
        2: "Листья Харады",
        3: "Ягоды Паслёна",
        4: "Рвоск",
        5: "Вердинская Крапива",
        6: "Обычные",
        7: "Обычные",
        8: "Обычные",
        9: "Корень Стрела",
        10: "Сердце Жлезодрева",
        11: "Синий Кривожаб",
        12: "Стебли Гифломы, 2, Днем перебросить"
    },
    "Луга": {
        2: "Листья Харады",
        3: "Цветы Дракуса",
        4: "Веточка лаванды, 2",
        5: "Корень Стрела",
        6: "Обычные",
        7: "Обычные",
        8: "Обычные",
        9: "Бобы Сцили, 2",
        10: "Сок кактуса",
        11: "Листохвост",
        12: "Нектар Гиацинта"
    },
    "Холмы": {
        2: "Дьявольский кроволист",
        3: "Ягоды Паслёна",
        4: "Листохвост, 2",
        5: "Веточка лаванды",
        6: "Обычные",
        7: "Обычные",
        8: "Обычные",
        9: "Сердце Жлезодрева",
        10: "Кисть Генгкоу",
        11: "аменный вьюн, 2",
        12: "Листья Харады"
    },
    "Горы": {
        2: "Дыхание Василиска",
        3: "Замороженные саженцы, 2",
        4: "Арктический плющ, 2",
        5: "Высушенная Эфедра",
        6: "Обычные",
        7: "Обычные",
        8: "Обычные",
        9: "Цветы Дракуса",
        10: "Сетопыль шляпки, 1, 2 шт в пещерах",
        11: "Каменный вьюн",
        12: "Изначальный бальзам"
    },
    "Болота": {
        2: "Дьявольский кроволист",
        3: "Ягоды шипоцвета",
        4: "Рвоск",
        5: "Шляпка мухомора, 2",
        6: "Обычные",
        7: "Обычные",
        8: "Обычные",
        9: "Синий Кривожаб, 2",
        10: "Зловонная луковица",
        11: "Водополох, 1, 2 шт если дождь",
        12: "Изначальный бальзам"
    },
    "Подземье": {
        2: "Изначальный бальзам, 2",
        3: "Серебряный гибискус",
        4: "Дьявольский кроволист",
        5: "Хромовая слизь",
        6: "Порошок морплоти, 2",
        7: "Фенхелейвый шёлк",
        8: "Дьявольский плющ",
        9: "Кисть Генгкоу",
        10: "Сетопыль шляпки, 2",
        11: "Сияющий синтоцвет",
        12: "Стебли Гифломы"
    }
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
    plant_name = terrain_roll_tables[selected_terrain][roll("2d6")]
    if plant_name == COMMON_TERRAIN_NAME:
        roll = str(randint(1, 6) + randint(1, 6))
        plant_name = terrain_roll_tables[COMMON_TERRAIN_NAME][roll("2d6")]
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
    selected_terrain = terrain_selector(terrain_roll_tables)
    roll_button = st.button("Ролл!")

    if roll_button:
        plant_name = roll_for_plant(selected_terrain)
        write_plant(plant_name)
        write_plant_other_description(plant_name, plants)



    
    
    

