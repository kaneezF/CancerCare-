import streamlit as st
st.set_page_config(
        page_title="diagnosis system",
                )

from streamlit_option_menu import option_menu

import home , doc  , login , logout , signup , reduce ,lung


if "login" not in st.session_state:
    st.session_state.login = False

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        def is_user_logged_in():
            return st.session_state.login
        #app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Welcome ',
                options=['Home','Lung Cancer ','Brain cancer','Find Hospitals','Sign Up','Login','Logout'],
                icons=['house-fill','bi bi-lungs-fill','bi bi-heart-pulse','bi bi-hospital','bi bi-person-add','person-circle','arrow-right-circle-fill','arrow-left-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0
            )
               

        if app == "Home":
            home.app()

        if app =="Lung Cancer ":
            if is_user_logged_in():
                #st.title(f"Welcome to the {app} section")
                lung.app()
            else:
                st.warning("You need to login first")

        if app == "Find Hospitals":
            if is_user_logged_in():
                #st.title(f"Welcome to the {app} section")
                doc.FindDoctorApp()
            else:
                st.warning("You need to login first")

        if app == 'Brain cancer':
            if is_user_logged_in():
                #st.title(f"Welcome to the {app} section")
                reduce.app()
            else:
                st.warning("You need to login first")

        if app == 'Login':
            login.app()

        if app == 'Logout':
            logout.app()

        if app =='Sign Up':
            signup.app()

    
    run()   