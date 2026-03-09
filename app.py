import streamlit as st
from nav import PAGES


nav = st.navigation([p.get_st_page() for p in PAGES])
nav.run()
