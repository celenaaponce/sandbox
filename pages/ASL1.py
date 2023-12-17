import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from pages import holidays
from st_pages import Page, Section,show_pages, add_page_title

def main():
    login_sidebar_ASL1()
    st.header("Bienvenido a la clase de ASL 1.")
    st.header("Se puede mirar nuestro curriculo aqui:")
    tab1, tab2, tab3, tab4 = st.tabs([":white[Primera Semana]", ":white[Conocer la Familia Bravo Pt 1]", ":white[Halloween/Dia de los Muertos]", 
                                                        ":white[Conocer la Familia Bravo Pt 2]"])
    with tab1:
            primera_semana()
    with tab2:
            segunda_semana()
    with tab3:
            holidays.halloween()
    with tab4:
            tercera_semana()


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
        Page("pages/ASL1.py", "Semana 1-3"),
        Page("pages/ASL1_semana_2.py", "Semana 4-7")
    ]
)
def set_styles():
    st.write("""
        <style>
        a {
            background-color: #94387f;
            color: white;

            }
        </style>
    """, unsafe_allow_html=True)

def primera_semana():
    set_styles()
    st.subheader('Primera Semana: Introducción')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Recursos</u></h4>", unsafe_allow_html=True)
    clms = st.columns([1,1])
    with clms[0]:
        st.title('')
        st.markdown('<h5>Escuelas para los Sordos en EEUU</h5>', unsafe_allow_html=True)
    with clms[1]:
        st.markdown("<a href='https://www.asd-1817.org/deaf-schools' target='_blank'><img style='float: right;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-20%20at%205.21.38%20PM.png' width= '200' height = '100' /></a>", unsafe_allow_html=True)
    clms31 = st.columns([1,1])
    with clms31[0]:
        st.title('')
        st.markdown('<h5>Alarma de Reloj para personas Sordos</h5>', unsafe_allow_html=True)
    with clms31[1]:
        st.markdown("<a href='https://www.diglo.com/vibrating-clocks-and-watches/alarm-clocks;d=3;c=31;s=311' target='_blank'><img style='float: right;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/clock.jpg' width='200' height='100'/></a>", unsafe_allow_html=True)     
    clms32 = st.columns([1,1])
    with clms32[0]:
        st.title('')
        st.markdown('<h5>Timbre con luz para personas Sordos</h5>', unsafe_allow_html=True)
    with clms32[1]:    
        st.markdown("<a href='https://www.diglo.com/shop-by-alert-trigger/doorbell-and-door-knock;d=3;c=32;s=323' target='_blank'><img style='float: right;' src = 'https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/light.jpg' width = '200' height = '100'/></a>", unsafe_allow_html=True)     
    clms33 = st.columns([1,1])
    with clms33[0]:
        st.title('')
        st.markdown('<h5>Alarma de Incendios para personas Sordos</h5>', unsafe_allow_html=True)
    with clms33[1]:     
        st.markdown("<a href='https://www.diglo.com/shop-by-alert-trigger/smoke-and-fire;d=3;c=32;s=328' target='_blank'><img style='float: right;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/firealarm.webp' width='200' height = '100'/></a>", unsafe_allow_html=True)
    clms34 = st.columns([1,1])
    with clms34[0]:
        st.title('')
        st.markdown('<h5>Teléfono de Vídeo para personas Sordos</h5>', unsafe_allow_html=True)
    with clms34[1]:         
        st.markdown("<a href='https://purplevrs.com/espanol' target='_blank'><img style='float: right;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/vp.png' width='150' height = '100'/></a>", unsafe_allow_html=True)
    clms35 = st.columns([1,1])
    with clms35[0]:
        st.title('')
        st.markdown('<h5>App para aprender para iPhone </h5>', unsafe_allow_html=True)
    with clms35[1]:      
        st.markdown("<a href='https://apps.apple.com/us/app/intersign-asl-learn-now/id1567327543' target='_blank'><img style='float: right;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/is.webp' height='100' width='100'/></a>", unsafe_allow_html=True)
    clms36 = st.columns([1,1])
    with clms36[0]:
        st.title('')
        st.markdown('<h5>App para aprender para Android</h5>', unsafe_allow_html=True)
    with clms36[1]:     
        st.markdown("<a href='https://play.google.com/store/apps/details?id=intersign.learn.asl&hl=en_US&gl=US' target='_blank'><img style='float: right;' src='https://raw.githubusercontent.com/celenaaponce/mobile_practice/main/pages/is.webp' height='100' width='100'/></a>", unsafe_allow_html=True)
    clms37 = st.columns([1,1])
    with clms37[0]:
        st.title('')
        st.markdown('<h5>Historia de ASL</h5>', unsafe_allow_html=True)
    with clms37[1]: 
        st.video('https://youtu.be/Pt2_EjmtUp8')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms38 = st.columns([1,1])
    with clms38[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms38[1]: 
        st.video('https://youtu.be/dJBLpQFhujo')
    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ4wlJOjhmNap4RDFiDtqNi1cv2PvEsdZnP4ANcRsVCCDgK0NrpYYLfI5BgwVZzlycwNwmvlwU4qnNt/embed?start=false&loop=false&delayms=3000", height=480)

def segunda_semana():
    set_styles()
    st.subheader('Conocer La Familia Bravo Pt 1')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Introducción a La Familia (sin subtitlos) 🔇</h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://youtu.be/SITwK-RY11c')
    clms22 = st.columns([1,1])
    with clms22[0]:
        st.title('')
        st.markdown('<h5>Introducción a La Familia (con subtitlos) 🔈</h5>', unsafe_allow_html=True)
    with clms22[1]:
        st.video('https://youtu.be/gK3cUfN1Lfw')
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicación</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/TnwmFK1Odqo')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversación (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/tZk1fKC_7hQ')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversación (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/5gYPPZFOO6M')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Cultura Sorda</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/tKMpJxq7wNk')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/WsoxPTw9j9U')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/633642ed68206040f25bc382' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/633750f5389ee741763d8d57' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/63375bff25e87940d4c32e08' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQd8Y-xcWg9rS517V1gkm3m7O_sEKq_OSo4nQxS2RI2TFew0eR1yjqb1_mhLUfZ9CW1hrApe8mbHNLj/embed?start=false&loop=false&delayms=3000", height=480)

def tercera_semana():
    set_styles()
    st.subheader('Conocer La Familia Bravo Pt 2')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicación</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/35oau3bfsnY')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversación (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/RAoRBgN_BaQ')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversación (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/M9k6WcksVp0')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Gramatica</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/T-69bZ33l90')
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Frases</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/PKULlbXRFic')
    clms30 = st.columns([1,1])
    with clms30[0]:
        st.title('')
        st.markdown('<h5>Cuento (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms30[1]:    
        st.video('https://youtu.be/__ZXhLplISE')
    clms31 = st.columns([1,1])
    with clms31[0]:
        st.title('')
        st.markdown('<h5>Cuento (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms31[1]: 
        st.video('https://youtu.be/NDjz2eiNOv0')        
    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/uGtS3_zEGV8')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/6340a4165be52340dc956cb7' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/6340a73092852240f8ac3087' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTxPJGXEYZG_-N-G7ypLyhScw07aukwDGxidek6zeh1iCQYRaRfuyTZ76xHec4iOGFz9fjTX31aICJ1/embed?start=false&loop=false&delayms=3000", height=480)

main()