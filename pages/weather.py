from pathlib import Path
import requests, streamlit as st
from page import Page


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='Počasí',
    icon='🌤️',
    desc='Aktuální předpověď a meteorologická data pro vybrané lokality'
)


def main():
    city = st.text_input("Město:", value="Praha")

    if st.button("Zjistit", use_container_width=True):
        with st.spinner():
            # Geocoding
            geo = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name": city, "count": 1}).json()
            
            if "results" in geo:
                res = geo["results"][0]
                # Předpověď
                data = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude": res["latitude"], "longitude": res["longitude"], "current_weather": True}).json()
                
                weather = data["current_weather"]
                
                st.metric(res["name"], f"{weather['temperature']} °C")
                st.write(f"Vítr: {weather['windspeed']} km/h")
            else:
                st.error("Nenalezeno")


if __name__ == '__main__':
    page.render()
    main()

