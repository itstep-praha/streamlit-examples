import streamlit as st
import index
from pages import currency, password, weather, youtube


pages = [index, currency, password, weather, youtube]
pages = [item.page.get_nav_item() for item in pages]

nav = st.navigation(pages)
nav.run()
