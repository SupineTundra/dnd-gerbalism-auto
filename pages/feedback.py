import streamlit as st
import streamlit.components.v1 as components
from scripts.sidebar import init_sidebar
st.set_page_config(
    page_title="Обратная связь",
    page_icon="📖"
)
init_sidebar()
st.header("📖 Обратная связь")
st.success("Я буду очень рада получить фидбек и как-нибудь улучшить приложение. Если есть идеи, то обязательно заполняйте форму!")
st.success("Также можно ознакомиться с задачами, которые планируются, в работе или уже сделаны https://apricot-nape-453.notion.site/e451115dc30649f0bbb1d3f8bd4b8319")
components.iframe("https://forms.yandex.ru/u/6574f103d04688604bcc834d/", width=700, height=800, scrolling=True)