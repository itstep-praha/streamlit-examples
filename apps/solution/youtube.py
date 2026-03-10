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

    render_url_examples()

    url = st.text_input("Youtube URL:", placeholder='Zadejte Youtube video URL')
    submit = st.button("Zpracovat video", use_container_width=True)

    if submit and url:
        try:
            with st.spinner("Hledám video..."):
                video = YouTube(url)
            
            render_video_details(video)
            
            with st.spinner("Připravuji soubor..."):
                buffer = get_youtube_stream_data(video)
            
            # Tlačítko pro finální stažení ke klientovi
            st.download_button(
                label="💾 Stáhnout MP4",
                data=buffer,
                file_name=f"{video.title}.mp4",
                mime="video/mp4",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Chyba: {e}")
    
    elif submit and not url:
        st.warning("Vložte prosím URL adresu.")


def render_video_details(video):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(video.thumbnail_url, use_container_width=True)
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
