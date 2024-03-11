import streamlit as st
from streamlit import session_state as ss


def regular_sidebar():

            st.sidebar.page_link("Pagina_Principal.py", label="Pagina Principal")
            st.sidebar.page_link("pages/Diccionario.py", label="Diccionario")
            st.sidebar.page_link("pages/Clases.py", label="Clases")
            st.sidebar.page_link("pages/Libros.py", label="Libros")
            st.sidebar.page_link("pages/Recursos.py", label="Recursos")
            st.sidebar.page_link("pages/Sobre_Yo.py", label="Sobre Yo")
            st.sidebar.page_link("pages/Diccionario_Completo.py", label="Diccionario Completo")
            st.sidebar.page_link("pages/Diccionario_por_Letra.py", label="Diccionario Por Letra")
            st.sidebar.page_link("pages/Diccionario_por_Tema.py", label="Diccionario Por Tema")
            st.sidebar.page_link("pages/Buscar_Palabra.py", label="Buscar Palabra")
            st.sidebar.page_link("pages/Entrar.py", label="Entrar")
            
def ASL1_sidebar():
            st.sidebar.page_link("Pagina_Principal.py", label="Pagina Principal")
            st.sidebar.page_link("pages/Diccionario.py", label="Diccionario")
            st.sidebar.page_link("pages/Clases.py", label="Clases")
            st.sidebar.page_link("pages/Libros.py", label="Libros")
            st.sidebar.page_link("pages/Recursos.py", label="Recursos")
            st.sidebar.page_link("pages/Sobre_Yo.py", label="Sobre Yo")
            st.sidebar.page_link("pages/Diccionario_Completo.py", label="Diccionario Completo")
            st.sidebar.page_link("pages/Diccionario_por_Letra.py", label="Diccionario Por Letra")
            st.sidebar.page_link("pages/Diccionario_por_Tema.py", label="Diccionario Por Tema")
            st.sidebar.page_link("pages/Buscar_Palabra.py", label="Buscar Palabra")
            st.sidebar.page_link("pages/Entrar.py", label="Entrar")
            st.sidebar.page_link("pages/Introduccion_a_ASL_1.py", label="Introducción a ASL 1")
            st.sidebar.page_link("pages/Bravo_1.py", label="Conocer la Familia Bravo")
            st.sidebar.page_link("pages/holidays_spring.py", label="Días Festivos")
            st.switch_page('pages/Introduccion_a_ASL_1.py')

def Page1Nav():
    st.sidebar.page_link("pages/page1.py", label="Page 1", icon='✈️')


def Page2Nav():
    st.sidebar.page_link("pages/page2.py", label="Page 2", icon='📚')


def MenuButtons(user_roles=None):
    if user_roles is None:
        user_roles = {}

    if 'authentication_status' not in ss:
        ss.authentication_status = False

    # Always show the home and login navigators.
    regular_sidebar()



# Show page 1 if the username that logged in is an admin.
    if user_roles == 'ASL1':
        ASL1_sidebar()

    
