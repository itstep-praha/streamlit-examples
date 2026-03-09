import streamlit as st
from nav import PAGES


st.title('🐍 Stramlit Examples')
st.write("Stramlit Examples created for Workshop")
st.write("")
st.write("")


def create_card(title, description, icon, page_path):
    with st.container(border=True):
        st.subheader(f"{icon} {title}")
        st.write(description)
        if st.button(f"Otevřít {title}", key=page_path):
            st.switch_page(page_path)


cols_per_row = 2
cols = st.columns(cols_per_row)
page_enum = enumerate(p for p in PAGES if not p.is_index)

for index, page in page_enum:
    with cols[index % cols_per_row]:
        with st.container(border=True):
            st.markdown(f"### {page.icon} {page.title}")
            if st.button(f"Otevřít {page.title}", key=page.path, use_container_width=True):
                st.switch_page(page.path)
