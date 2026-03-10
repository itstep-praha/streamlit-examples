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

    # Vstupy
    amount = st.number_input("Částka", value=1.0, min_value=0.0)
    from_currency = st.selectbox("Z měny", ["EUR", "USD", "CZK", "GBP"])
    to_currency = st.selectbox("Do měny", ["CZK", "EUR", "USD", "GBP"])
    button = st.button("Převést", use_container_width=True)
    
    if button:
        with st.spinner():
            # Výpočet
            rate = get_rate(from_currency, to_currency)
            result = amount * rate

            # Zobrazení výsledku
            st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")


if __name__ == '__main__':
    page.render()
    main()
