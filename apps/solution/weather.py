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

    # Vstup a tlačítko
    city = st.text_input("Město:", value="Praha")
    button = st.button("Zjistit", use_container_width=True)

    # Kontrola zadání města
    if not city.strip():
        st.error('Zadejte město')
        st.stop()

    if button:
        with st.spinner():
            # získání dat
            weather = get_weather(city)

            if weather:
                # vykreslení výsledků
                st.metric(weather['place'], f"{weather['temperature']} °C")
                st.write(f"Vítr: {weather['windspeed']} km/h")
            else:
                st.error("Nenalezeno")


if __name__ == '__main__':
    page.render()
    main()
