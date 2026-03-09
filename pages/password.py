from pathlib import Path
import random, string, streamlit as st
from page import Page


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='Generátor Hesel',
    icon='🔐',
    desc='Bezpečné generování silných hesel s nastavitelnou délkou a speciálními znaky'
)


def main():
    # nastavení
    length = st.slider("Délka", 8, 32, 16)
    symbols = string.ascii_letters + string.digits + "!@#$%^&*"

    # generování nového hesla
    password = "".join(random.choice(symbols) for _ in range(length))

    # vykreslení
    st.code(password, language='text')
    if st.button("Generovat heslo", use_container_width=True):
        st.rerun()


if __name__ == '__main__':
    page.render()
    main()


