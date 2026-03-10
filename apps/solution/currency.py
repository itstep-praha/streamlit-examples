from pathlib import Path
import requests, streamlit as st
from utils.page import Page


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='Převodník měn',
    icon='💵',
    desc='Přepočet světových měn podle aktuálního kurzu',
)


def main():
    # Vstupy
    amount = st.number_input("Částka", value=1.0)
    base = st.selectbox("Z měny", ["EUR", "USD", "CZK", "GBP"])
    target = st.selectbox("Do měny", ["CZK", "EUR", "USD", "GBP"])

    # Výpočet
    if st.button("Převést", use_container_width=True):
        with st.spinner():
            url = "https://api.frankfurter.app/latest"
            data = requests.get(url, params={"from": base, "to": target}).json()
            rate = data["rates"][target]
            result = amount * rate
            st.success(f"{amount} {base} = {result:.2f} {target}")


if __name__ == '__main__':
    page.render()
    main()
