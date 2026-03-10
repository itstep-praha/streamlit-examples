import streamlit as st
from pathlib import Path
from utils.page import Page


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='Převodník měn',
    icon='💵',
    desc='Přepočet světových měn podle aktuálního kurzu',
)


def main():
    from utils.func import get_rate


if __name__ == '__main__':
    page.render()
    main()
