import streamlit as st

class StreamlitObject:
    def __init__(self):
        if "isUserLoggedIn" not in st.session_state:
            st.session_state.isUserLoggedIn = False
        self.initialize()

    def initialize(self):
        if not st.session_state.isUserLoggedIn:
            self.sidebar_login()
        else:
            st.write("HELLO WORLD!")

    def sidebar_login(self):
        with st.form("login_form", clear_on_submit=True):
            with st.sidebar:
                st.title("LOGIN")
                self.username = st.text_input("Username")
                self.password = st.text_input("Password")
                self.submit = st.form_submit_button("Login", type="primary")
            self.login()

    def login(self):
        if self.submit:
            if self.username == "admin" and self.password == "pass":
                st.session_state.isUserLoggedIn = True
                st.write("User logged in!")
                st.experimental_rerun()
            else:
                st.write("No user found!")
        else:
            st.write("Not logged in!")


if __name__ == '__main__':
    StreamlitObject()
