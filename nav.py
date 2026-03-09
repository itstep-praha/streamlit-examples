import streamlit as st


class Page:
    """ wrapper for page definition """
    def __init__(self, path, title, icon, desc='', is_index=False):
        self.path = path
        self.title = title
        self.icon = icon
        self.desc = desc
        self.is_index = is_index
    
    def get_st_page(self):
        """ returns st Page instance for navigation """
        return st.Page(self.path, title=self.title, icon=self.icon)


PAGES = [
    Page("index.py", title="Streamlit Examples", icon="🐍", is_index=True),
    Page("pages/currency.py", title="Převodník měn", icon="💵", desc='Přepočet světových měn podle aktuálního kurzu'),
    Page("pages/weather.py", title="Počasí", icon="🌤️", desc='Aktuální předpověď a meteorologická data pro vybrané lokality'),
    Page("pages/youtube.py", title="Youtube stahovač", icon="🎥", desc='Jednoduchý nástroj pro ukládání videí a audia přímo do tvého počítače'),
    Page("pages/password.py", title="Generátor Hesel", icon="🔐", desc='Bezpečné generování silných hesel s nastavitelnou délkou a speciálními znaky'),
]
