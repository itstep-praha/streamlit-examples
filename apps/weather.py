import streamlit as st
from pathlib import Path
from utils.page import Page


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='Počasí',
    icon='🌤️',
    desc='Aktuální předpověď a meteorologická data pro vybrané lokality'
)


def main():
    from utils.func import get_weather


if __name__ == '__main__':
    page.render()
    main()
