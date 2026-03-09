from pathlib import Path
import streamlit as st
from page import Page
from pages import currency, password, weather, youtube


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='Streamlit Examples',
    icon='🐍',
    desc='Stramlit Examples created for Workshop',
)


def render_menu():
    cols_per_row = 2
    cols = st.columns(cols_per_row)
    pages = [currency, password, weather, youtube]

    for index, item in enumerate(pages):
        with cols[index % cols_per_row]:
            item.page.render_container()


if __name__ == '__main__':
    page.render()
    render_menu()



