import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Обратная связь",
    page_icon="📖"
)
st.header("📖 Обратная связь")
st.success("Я буду очень рада получить фидбек и как-нибудь улучшить приложение. Если есть идеи, то обязательно заполняйте форму!")
components.iframe("https://forms.yandex.ru/u/6574f103d04688604bcc834d/", width=700, height=800, scrolling=True)