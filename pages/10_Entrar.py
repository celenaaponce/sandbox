import streamlit_authenticator as stauth
import yaml
import gdown
from yaml.loader import SafeLoader
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
from st_pages import Page, Section,show_pages, add_page_title
from streamlit.source_util import get_pages
import streamlit.components.v1 as components
from pages import ASL2
from pages import ASLAtHome
from pages import holidays
from pages import ASL2_semana_2
from pages import ASLAtHome_semana_2

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
        Page("pages/9_Buscar_Palabra.py", "Buscar Palabra"),
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
        Page("pages/9_Buscar_Palabra.py", "Buscar Palabra"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion.py", "Introducción"),
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
        Page("pages/9_Buscar_Palabra.py", "Buscar Palabra"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion.py", "Introducción"),
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
        Page("pages/9_Buscar_Palabra.py", "Buscar Palabra"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/ASLAtHome.py", "Semana 1-3"),
        Page("pages/ASLAtHome_semana_2.py", "Semana 4-7")
    ]
)
        
def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                }}
            }}
        function goTo(page) {{
        page_links = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li a')
        page_links.forEach((link) => {{
            if (link.text == page) {{
                link.click()
            }}
        }})
    }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

def set_styles():
    st.write("""
        <style>
        a {
            background-color: #94387f;
            color: white;

            }
        </style>
    """, unsafe_allow_html=True)

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
    authenticator.logout('Salir', 'main')
    st.title(f'Bienvenido *{name}*')
    if username in st.secrets.ASL1:
        login_sidebar_ASL1()
        switch_page("Introducción")

    elif username in st.secrets['ASL2']:
        login_sidebar_ASL2()
        st.header("Bienvenido a la clase de ASL 2.")
        st.header("Se puede mirar nuestro curriculo aqui:")
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs([":white[Primera Semana]", ":white[Repaso General]", ":white[Repaso Leccion 1]", ":white[Repaso Leccion 2]", 
                                                                               ":white[Repaso Leccion 3]", ":white[Repaso Leccion 4]", ":white[Halloween/Dia de los Muertos]", 
                                                                               ":white[Colores]", ":white[Deletrear]", ":white[Dia de Accion de Gracias]", ":white[Escuela Pt 1]"])
        with tab1:
             ASL2.primera_semana()
        with tab2:
             ASL2.repaso_general()
        with tab3:
             ASL2.repaso_lecc1()
        with tab4:
             ASL2.repaso_lecc2()
        with tab5:
             ASL2.repaso_lecc3()
        with tab6:
             ASL2.repaso_lecc4()
        with tab7:
             holidays.halloween()
        with tab8:
             ASL2.colores()
        with tab9:
             ASL2_semana_2.deletrear()
        with tab10:
             holidays.thanksgiving()
        with tab11:
             ASL2_semana_2.escuela1()

    else:
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
