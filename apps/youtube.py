from pathlib import Path
import io, streamlit as st
from utils.page import Page


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='Youtube stahovač',
    icon='🎥',
    desc='Jednoduchý nástroj pro ukládání videí a audia přímo do tvého počítače',
)


# Příklady URLs
url1 = 'https://www.youtube.com/watch?v=hJ-adQhERuE'
url2 = 'https://www.youtube.com/watch?v=D3gHOXg4_Xo'
url3 = 'https://www.youtube.com/watch?v=NcsaZg-j3pI'


def main():
    pass


if __name__ == '__main__':
    page.render()
    main()
