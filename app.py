import streamlit as st
import index
from apps import app_list


nav = st.navigation({
    "": [index.page.get_nav_item()],
    "Aplikace": [app.page.get_nav_item() for app in app_list],
})
nav.run()


with st.sidebar:
    st.page_link("https://github.com/itstep-praha/streamlit-examples", label="GitHub repozitář", icon="💻")
    st.page_link("https://praha.itstep.org/contacts", label="Kontakt", icon="✉️")
