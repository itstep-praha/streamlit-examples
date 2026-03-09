from pathlib import Path
import io, streamlit as st
from page import Page


path = str(Path(__file__).relative_to(Path.cwd()))
page = Page(
    path=path,
    title='Youtube stahovač',
    icon='🎥',
    desc='Jednoduchý nástroj pro ukládání videí a audia přímo do tvého počítače',
)


# Example URLs
url1 = 'https://www.youtube.com/watch?v=hJ-adQhERuE'
url2 = 'https://www.youtube.com/watch?v=D3gHOXg4_Xo'
url3 = 'https://www.youtube.com/watch?v=NcsaZg-j3pI'


def main():
    from pytubefix import YouTube

    with st.expander("Zobrazit příklady URL"):
        st.write("Kliknutím zkopírujete:")
        for item in [url1, url2, url3]:
            st.code(item, language='text')

    url = st.text_input("Youtube URL:", placeholder='Zadejte Youtube video URL')
    submit = st.button("Zpracovat video", use_container_width=True)

    if submit and url:
        try:
            yt = YouTube(url)
            st.write(f"Vybráno: **{yt.title}**")
            
            # Nejvyšší kvalita
            stream = yt.streams.get_highest_resolution()
            
            # Stažení do paměti
            buffer = io.BytesIO()
            with st.spinner("Připravuji soubor..."):
                stream.stream_to_buffer(buffer)
            
            # Tlačítko pro finální stažení ke klientovi
            st.download_button(
                label="💾 Stáhnout MP4",
                data=buffer.getvalue(),
                file_name=f"{yt.title}.mp4",
                mime="video/mp4",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Chyba: {e}")

    elif submit and not url:
        st.warning("Vložte prosím URL adresu.")


if __name__ == '__main__':
    page.render()
    main()
