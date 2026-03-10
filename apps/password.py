from pathlib import Path
import random, string, streamlit as st
from utils.page import Page


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='Generátor Hesel',
    icon='🔐',
    desc='Bezpečné generování silných hesel s nastavitelnou délkou a speciálními znaky'
)


def main():
    pass


if __name__ == '__main__':
    page.render()
    main()


