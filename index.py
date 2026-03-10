import streamlit as st
from pathlib import Path
from utils.page import Page
from apps import app_list


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='IT Step Workshop Examples',
    icon='🐍',
    desc='Streamlit Examples created for Workshop',
)


def render_menu():
    cols_per_row = 2
    cols = st.columns(cols_per_row)

    for index, app in enumerate(app_list):
        with cols[index % cols_per_row]:
            app.page.render_container()


if __name__ == '__main__':
    page.render()
    render_menu()



