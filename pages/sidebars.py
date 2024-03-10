from st_pages import Page, show_pages
import streamlit as st

def regular_sidebar():
            st.sidebar.page_link("Pagina_Principal.py", "Pagina Principal")
            st.sidebar.page_link("pages/1_Diccionario.py", "Diccionario")
            st.sidebar.page_link("pages/2_Clases.py", "Clases")
            st.sidebar.page_link("pages/3_Libros.py", "Libros")
            st.sidebar.page_link("pages/4_Recursos.py", "Recursos")
            st.sidebar.page_link("pages/5_Sobre_Yo.py", "Sobre Yo")
            st.sidebar.page_link("pages/6_Diccionario_Completo.py", "Diccionario Completo")
            st.sidebar.page_link("pages/7_Diccionario_por_Letra.py", "Diccionario Por Letra")
            st.sidebar.page_link("pages/8_Diccionario_por_Tema.py", "Diccionario Por Tema")
            st.sidebar.page_link("pages/9_Buscar_Palabra.py", "Buscar Palabra")
            st.sidebar.page_link("pages/10_Entrar.py", "Entrar")
                
def login_sidebar_ASL1():
            st.sidebar.page_link("Pagina_Principal.py", "Pagina Principal")
            st.sidebar.page_link("pages/1_Diccionario.py", "Diccionario")
            st.sidebar.page_link("pages/2_Clases.py", "Clases")
            st.sidebar.page_link("pages/3_Libros.py", "Libros")
            st.sidebar.page_link("pages/4_Recursos.py", "Recursos")
            st.sidebar.page_link("pages/5_Sobre_Yo.py", "Sobre Yo")
            st.sidebar.page_link("pages/6_Diccionario_Completo.py", "Diccionario Completo")
            st.sidebar.page_link("pages/7_Diccionario_por_Letra.py", "Diccionario Por Letra")
            st.sidebar.page_link("pages/8_Diccionario_por_Tema.py", "Diccionario Por Tema")
            st.sidebar.page_link("pages/9_Buscar_Palabra.py", "Buscar Palabra")
            st.sidebar.page_link("pages/10_Entrar.py", "Entrar")
            st.sidebar.page_link("pages/Introduccion_a_ASL_1.py", "Introducción a ASL 1")
            st.sidebar.page_link("pages/Bravo_1.py", "Conocer la Familia Bravo")
            st.sidebar.page_link("pages/holidays_spring.py", "Días Festivos")
        
def login_sidebar_ASL2():
            st.sidebar.page_link("Pagina_Principal.py", "Pagina Principal")
            st.sidebar.page_link("pages/1_Diccionario.py", "Diccionario")
            st.sidebar.page_link("pages/2_Clases.py", "Clases")
            st.sidebar.page_link("pages/3_Libros.py", "Libros")
            st.sidebar.page_link("pages/4_Recursos.py", "Recursos")
            st.sidebar.page_link("pages/5_Sobre_Yo.py", "Sobre Yo")
            st.sidebar.page_link("pages/6_Diccionario_Completo.py", "Diccionario Completo")
            st.sidebar.page_link("pages/7_Diccionario_por_Letra.py", "Diccionario Por Letra")
            st.sidebar.page_link("pages/8_Diccionario_por_Tema.py", "Diccionario Por Tema")
            st.sidebar.page_link("pages/9_Buscar_Palabra.py", "Buscar Palabra")
            st.sidebar.page_link("pages/10_Entrar.py", "Entrar")
            st.sidebar.page_link("pages/Introduccion_a_ASL_2.py", "Introducción a ASL 2")
            st.sidebar.page_link("pages/Bravo_4.py", "Ir de Compras")
            st.sidebar.page_link("pages/holidays_spring_2.py", "Días Festivos")

def login_sidebar_ASL3():
            st.sidebar.page_link("Pagina_Principal.py", "Pagina Principal")
            st.sidebar.page_link("pages/1_Diccionario.py", "Diccionario")
            st.sidebar.page_link("pages/2_Clases.py", "Clases")
            st.sidebar.page_link("pages/3_Libros.py", "Libros")
            st.sidebar.page_link("pages/4_Recursos.py", "Recursos")
            st.sidebar.page_link("pages/5_Sobre_Yo.py", "Sobre Yo")
            st.sidebar.page_link("pages/6_Diccionario_Completo.py", "Diccionario Completo")
            st.sidebar.page_link("pages/7_Diccionario_por_Letra.py", "Diccionario Por Letra")
            st.sidebar.page_link("pages/8_Diccionario_por_Tema.py", "Diccionario Por Tema")
            st.sidebar.page_link("pages/9_Buscar_Palabra.py", "Buscar Palabra")
            st.sidebar.page_link("pages/10_Entrar.py", "Entrar")
            st.sidebar.page_link("pages/Introduccion_a_ASL_3.py", "Introducción a ASL 3")
            st.sidebar.page_link("pages/Bravo_7.py", "Escuela")
            st.sidebar.page_link("pages/holidays_spring_3.py", "Días Festivos")
        
def login_sidebar_ASLAtHome2():
            st.sidebar.page_link("Pagina_Principal.py", "Pagina Principal")
            st.sidebar.page_link("pages/1_Diccionario.py", "Diccionario")
            st.sidebar.page_link("pages/2_Clases.py", "Clases")
            st.sidebar.page_link("pages/3_Libros.py", "Libros")
            st.sidebar.page_link("pages/4_Recursos.py", "Recursos")
            st.sidebar.page_link("pages/5_Sobre_Yo.py", "Sobre Yo")
            st.sidebar.page_link("pages/6_Diccionario_Completo.py", "Diccionario Completo")
            st.sidebar.page_link("pages/7_Diccionario_por_Letra.py", "Diccionario Por Letra")
            st.sidebar.page_link("pages/8_Diccionario_por_Tema.py", "Diccionario Por Tema")
            st.sidebar.page_link("pages/9_Buscar_Palabra.py", "Buscar Palabra")
            st.sidebar.page_link("pages/10_Entrar.py", "Entrar")
            st.sidebar.page_link("pages/Introduccion_a_ASL_En_Casa.py")
            st.sidebar.page_link("pages/holidays_spring_aah.py", "Días Festivos")
        
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
    return htmlstr
    

def set_styles(background_color):
    style_html = f"""
    <style>
    h5 {{
        margin-top: 20px;
        margin-bottom: 20px;
    }}
    a {{
        background-color: {background_color};
    }}
    </style>
"""
    return style_html

