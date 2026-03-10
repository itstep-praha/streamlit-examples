import streamlit as st
import index
from apps import app_list


use_apps = (index, *app_list)
nav = st.navigation([app.page.get_nav_item() for app in use_apps])
nav.run()
