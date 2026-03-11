import streamlit as st
from pathlib import Path
from utils.page import Page


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='Generátor Hesel',
    icon='🔐',
    desc='Bezpečné generování silných hesel s nastavitelnou délkou a speciálními znaky'
)


def main():
    from utils.func import generate_password

    # nastavení
    length = st.slider("Délka", 8, 32, 16)

    # generování nového hesla
    password = generate_password(length)

    # vykreslení
    st.code(password, language='text')

    # při stiskntí zavoláme stránku znovu
    if st.button("Generovat heslo", width='stretch'):
        st.rerun()


if __name__ == '__main__':
    page.render()
    main()


