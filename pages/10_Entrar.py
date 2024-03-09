
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pages.sidebars import regular_sidebar, login_sidebar_ASL1, login_sidebar_ASL2, login_sidebar_ASL3, login_sidebar_ASLAtHome2
st.write(st.session_state)
def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):

            option = st.selectbox(
                    '¿Cual clase?',
                    ('ASL 1', 'ASL 2', 'ASL 3', 'ASL En Casa'), key='option')
            st.text_input("Contraseña", type="password", key="password")
            st.form_submit_button("Entrar", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state['password'] == st.secrets['password']:
                st.session_state["password_correct"] = True
        else:
                st.session_state["password_correct"] = False
    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()

    return False

if not check_password():
    st.stop()

if 'option' in st.session_state.keys():
    classoption = st.session_state['option']
else:       
    classoption = ""
    check_password()
if classoption == 'ASL 1':
    st.session_state['password_correct'] = True
    st.session_state['option'] = 'ASL 1'
    login_sidebar_ASL1()
    switch_page("Introducción_a_ASL_1")

elif classoption == 'ASL 2':
    st.session_state['password_correct'] = True
    st.session_state['option'] = 'ASL 2'
    login_sidebar_ASL2()
    switch_page("Introducción_a_ASL_2")
    
elif classoption == 'ASL En Casa':
    st.session_state['password_correct'] = True
    st.session_state['option'] = 'ASL En Casa'
    login_sidebar_ASLAtHome2()
    switch_page("Introduccion_a_ASL_En_Casa")

elif classoption == 'ASL 3':
    st.session_state['password_correct'] = True
    st.session_state['option'] = 'ASL 3'
    login_sidebar_ASL3()
    switch_page("Introducción_a_ASL_3")
else:
    regular_sidebar()
    check_password()
