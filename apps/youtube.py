import streamlit as st
from pathlib import Path
from utils.page import Page


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='Youtube stahovač',
    icon='🎥',
    desc='Jednoduchý nástroj pro ukládání videí a audia přímo do tvého počítače',
)


def main():
    from pytubefix import YouTube
    from utils.func import get_youtube_stream_data


def render_video_details(video):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(video.thumbnail_url, width='stretch')
    with col2:
        st.subheader(video.title, anchor=False)
        st.caption(f"Autor: {video.author} | Délka: {video.length}s")


def render_url_examples():
    url1 = 'https://www.youtube.com/watch?v=hJ-adQhERuE'
    url2 = 'https://www.youtube.com/watch?v=D3gHOXg4_Xo'
    url3 = 'https://www.youtube.com/watch?v=NcsaZg-j3pI'

    with st.expander("Zobrazit příklady URL"):
        st.write("Kliknutím zkopírujete:")
        for item in [url1, url2, url3]:
            st.code(item, language='text')


if __name__ == '__main__':
    page.render()
    main()
