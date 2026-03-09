import streamlit as st


class Page:
    """ Page helper/wrapper object to reduce code and structure pages """

    def __init__(self, path, title, icon, desc=''):
        self.path = path
        self.title = title
        self.icon = icon
        self.desc = desc

    def render(self):
        """ renders a page header """
        st.title(self.icon + ' ' + self.title)
        st.write(self.desc)
        st.write('')
        st.write('')

    def render_container(self):
        """ renders item as container for menu """
        with st.container(border=True):
            st.markdown(f'### {self.icon} {self.title}')
            if st.button(f'Otevřít {self.title}', key=self.path, use_container_width=True):
                st.switch_page(self.path)

    def get_nav_item(self):
        """ return st.Page object to create side nav item """
        return st.Page(self.path, title=self.title, icon=self.icon)
