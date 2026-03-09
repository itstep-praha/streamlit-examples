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
    # settings
    length = st.slider("Délka", 8, 32, 16)
    symbols = string.ascii_letters + string.digits + "!@#$%^&*"

    # new password
    password = "".join(random.choice(symbols) for _ in range(length))

    # render as code element
    st.code(password)
    if st.button("Generate new"):
        st.rerun()


if __name__ == '__main__':
    page.render()
    main()


