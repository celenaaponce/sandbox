from st_pages import Page, show_pages
import streamlit as st

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
                Page("pages/10_Entrar.py", "Entrar"),
                Page("pages/11_Form.py", "Registrar para Clases")
            ])
                
def login_sidebar_ASL1():
        if st.session_state['option'] == "ASL 1":
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
                Page("pages/11_Form.py", "Registrar para Clases"),
                Page("pages/10_Entrar.py", "Entrar"),
                Page("pages/Introduccion_a_ASL_1.py", "Introducción a ASL 1"),
                Page("pages/Bravo_1.py", "Conocer la Familia Bravo"),
                Page("pages/holidays_spring.py", "Días Festivos")
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
        Page("pages/11_Form.py", "Registrar para Clases"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion_a_ASL_2.py", "Introducción a ASL 2"),
        Page("pages/Bravo_4.py", "Ir de Compras"),
        Page("pages/holidays_spring_2.py", "Días Festivos")
    ]
)

def login_sidebar_ASL3():
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
        Page("pages/11_Form.py", "Registrar para Clases"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion_a_ASL_3.py", "Introducción a ASL 3"),
        Page("pages/Bravo_7.py", "Escuela"),
        Page("pages/holidays_spring_3.py", "Días Festivos")
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
        Page("pages/11_Form.py", "Registrar para Clases"),
        Page("pages/10_Entrar.py", "Entrar"),
        Page("pages/Introduccion_a_ASL_En_Casa.py"),
        Page("pages/holidays_spring_aah.py", "Días Festivos")
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

