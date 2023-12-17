import auth_custom.streamlit_authenticator as stauth
import yaml
import gdown
from yaml.loader import SafeLoader
import streamlit as st
from switch_page_button import switch_page
from PIL import Image
from st_pages import Page, show_pages
from pages import ASLAtHome
from pages import holidays
from pages import ASLAtHome_semana_2
from pages import Introduccion

def regular_sidebar():
        show_pages(
    [
        Page("Pagina_Principal.py", "Pagina Principal"),
        Page("pages/1_Diccionario.py", "Diccionario"),
        Page("pages/2_Clases.py", "Clases"),
        Page("pages/3_Libros.py", "Libros"),
        Page("pages/4_Recursos.py", "Recursos"),
        Page("pages/5_Sobre_Yo.py", "Sobre Yo"),
        Page("pages/6_Diccionario_Completo.py", "Diccionario Completo"),
        Page("pages/7_Diccionario_por_Letra.py", "Diccionario Por Letra"),
        Page("pages/8_Diccionario_por_Tema.py", "Diccionario Por Tema"),
        Page("pages/9_Buscar_Palabra.py", "Buscar Palabra_reg"),
        Page("pages/10_Entrar.py", "Entrar")
    ])
        
def login_sidebar_ASL1():
        show_pages(
    [
        Page("Pagina_Principal.py", "Pagina Principal"),
        Page("pages/1_Diccionario.py", "Diccionario"),
        Page("pages/2_Clases.py", "Clases"),
        Page("pages/3_Libros.py", "Libros"),
        Page("pages/4_Recursos.py", "Recursos"),
        Page("pages/5_Sobre_Yo.py", "Sobre Yo"),
        Page("pages/6_Diccionario_Completo.py", "Diccionario Completo"),
        Page("pages/7_Diccionario_por_Letra.py", "Diccionario Por Letra"),
        Page("pages/8_Diccionario_por_Tema.py", "Diccionario Por Tema"),
        Page("pages/9_Buscar_Palabra.py", "Buscar Palabra_asl1"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion.py", "Introducción a ASL 1"),
        Page("pages/Bravo_1.py", "Conocer la Familia Bravo"),
        Page("pages/Bravo_2.py", "Desayuno"),
        Page("pages/Bravo_3.py", "¿Dónde está el contról?"),
        Page("pages/holidays.py", "Días Festivos")
    ]
)
        
def login_sidebar_ASL2():
        show_pages(
    [
        Page("Pagina_Principal.py", "Pagina Principal"),
        Page("pages/1_Diccionario.py", "Diccionario"),
        Page("pages/2_Clases.py", "Clases"),
        Page("pages/3_Libros.py", "Libros"),
        Page("pages/4_Recursos.py", "Recursos"),
        Page("pages/5_Sobre_Yo.py", "Sobre Yo"),
        Page("pages/6_Diccionario_Completo.py", "Diccionario Completo"),
        Page("pages/7_Diccionario_por_Letra.py", "Diccionario Por Letra"),
        Page("pages/8_Diccionario_por_Tema.py", "Diccionario Por Tema"),
        Page("pages/9_Buscar_Palabra.py", "Buscar Palabra_asl2"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion_2.py", "Introducción a ASL 2"),
        Page("pages/Bravo_5.py", "Repaso"),
        Page("pages/Bravo_6.py", "Colores y Deletrear"),
        Page("pages/Bravo_7.py", "Escuela"),
        Page("pages/holidays.py", "Días Festivos")
    ]
)
        
def login_sidebar_ASLAtHome2():
        show_pages(
    [
        Page("Pagina_Principal.py", "Pagina Principal"),
        Page("pages/1_Diccionario.py", "Diccionario"),
        Page("pages/2_Clases.py", "Clases"),
        Page("pages/3_Libros.py", "Libros"),
        Page("pages/4_Recursos.py", "Recursos"),
        Page("pages/5_Sobre_Yo.py", "Sobre Yo"),
        Page("pages/6_Diccionario_Completo.py", "Diccionario Completo"),
        Page("pages/7_Diccionario_por_Letra.py", "Diccionario Por Letra"),
        Page("pages/8_Diccionario_por_Tema.py", "Diccionario Por Tema"),
        Page("pages/9_Buscar_Palabra.py", "Buscar Palabra_aslah"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/ASLAtHome.py", "Semana 1-3"),
        Page("pages/ASLAtHome_semana_2.py", "Semana 4-7")
    ]
)

@st.cache_data
def download_yaml():
        file_id = st.secrets['yaml']
        url = f'https://drive.google.com/uc?id={file_id}'
        gdown.download(url, 'info.yaml', quiet=False)
        with open('info.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)
        return config

config = download_yaml()
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Entrar', 'main')
if authentication_status:
    if username in st.secrets.ASL1:
        st.title(f'Bienvenido *{name}*')
        login_sidebar_ASL1()
        Introduccion.main(authenticator)
        switch_page("Introducción_a_ASL_1")

    elif username in st.secrets['ASL2']:
        authenticator.logout('Salir', 'main')
        st.title(f'Bienvenido *{name}*')
        login_sidebar_ASL2()
        switch_page("Introducción_a_ASL_2")
        
    else:
        authenticator.logout('Salir', 'main')
        st.title(f'Bienvenido *{name}*')
        login_sidebar_ASLAtHome2()
        st.header("Bienvenido a la clase de ASL En Casa.")
        st.header("Se puede mirar nuestro curriculo aqui:")
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([":white[Primera Semana]", ":white[Capitulo 1 Pt 1]", ":white[Halloween/Dia de los Muertos]", 
                                                            ":white[Capitulo 1 Pt 2]", ":white[Capitulo 2 Pt 1]", ":white[Capitulo 2 Pt 2]", ":white[Dia de Accion de Gracias]"])
        with tab1:
             ASLAtHome.primera_semana()
        with tab2:
             ASLAtHome.segunda_semana()
        with tab3:
             holidays.halloween()
        with tab4:
             ASLAtHome.tercera_semana()
        with tab5:
             ASLAtHome_semana_2.cuarta_semana()
        with tab6:
             ASLAtHome_semana_2.quinta_semana()
        with tab7:
            holidays.thanksgiving()

elif authentication_status == False:
    st.error('Nombre/contraseña es mal')
    regular_sidebar()
elif authentication_status == None:
    st.warning('Escriba su nombre de usario y contraseña.')
    regular_sidebar()
