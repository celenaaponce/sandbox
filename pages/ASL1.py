import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components

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
    cont_2 = st.container()

    outer_col_2 = st.columns([4, 1])            
    with cont_2:
        
        with outer_col_2[0]:
            st.markdown("<h4 style='text-align: center; color: white;'><u>Recursos</u></h4>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://www.asd-1817.org/deaf-schools' target='_blank'><img src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-20%20at%205.21.38%20PM.png' width= '200' height = '100' /></a>Escuelas para los Sordos en EEUU </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://www.diglo.com/vibrating-clocks-and-watches/alarm-clocks;d=3;c=31;s=311' target='_blank'><img src='https://m.media-amazon.com/images/I/7100+aehKvL._AC_SY300_SX300_.jpg' width='200' height='100'/></a>Alarma de Reloj para personas Sordos </h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://www.diglo.com/shop-by-alert-trigger/doorbell-and-door-knock;d=3;c=32;s=323' target='_blank'><img src = 'https://m.media-amazon.com/images/I/310R2UqXt0L._AC_.jpg' width = '200' height = '100/></a>Timbre con luz para personas Sordos </h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://www.diglo.com/shop-by-alert-trigger/smoke-and-fire;d=3;c=32;s=328' target='_blank'><img src='https://m.media-amazon.com/images/I/41JvpGHNyKL.__AC_SX300_SY300_QL70_FMwebp_.jpg' width='200' height = '100/></a>Alarma de Incendios para personas Sordos </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://purplevrs.com/espanol' target='_blank'><img src='https://www.purplevrs.com/media/1282/video-quality-slide-v2-450x450.png' width='150' height = '100'/></a>Teléfono de Vídeo para personas Sordos </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://apps.apple.com/us/app/intersign-asl-learn-now/id1567327543' target='_blank'><img src='https://is1-ssl.mzstatic.com/image/thumb/Purple116/v4/25/02/e4/2502e491-82e5-8ee1-b462-78f521e117f1/AppIcon-1x_U007emarketing-0-7-0-85-220.png/460x0w.webp' height='100' width='100'/></a>App para aprender para iPhone </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://play.google.com/store/apps/details?id=intersign.learn.asl&hl=en_US&gl=US' target='_blank'><img src='https://is1-ssl.mzstatic.com/image/thumb/Purple116/v4/25/02/e4/2502e491-82e5-8ee1-b462-78f521e117f1/AppIcon-1x_U007emarketing-0-7-0-85-220.png/460x0w.webp' height='100' width='100'/></a>App para aprender para Android </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/Pt2_EjmtUp8' target='_blank'><img src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-20%20at%204.59.14%20PM.png' width='200' height='100'/></a>Historia de ASL</h5>", unsafe_allow_html=True)

            st.divider()

            st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
        
            st.markdown("<h5> <a href='https://youtu.be/dJBLpQFhujo' target='_blank'>Vocabulario</a> para la semana que viene</h5>", unsafe_allow_html=True)
            st.divider()
            
            components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ4wlJOjhmNap4RDFiDtqNi1cv2PvEsdZnP4ANcRsVCCDgK0NrpYYLfI5BgwVZzlycwNwmvlwU4qnNt/embed?start=false&loop=false&delayms=3000", height=480)

def segunda_semana():
    set_styles()
    st.subheader('Segunda Semana: Conocer La Familia Bravo')
    cont_2 = st.container()

    outer_col_2 = st.columns([4, 1])            
    with cont_2:
        
        with outer_col_2[0]:
            st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/SITwK-RY11c' target='_blank'>Introduccion a La Familia (sin subtitlos)</a></h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/gK3cUfN1Lfw' target='_blank'>Introduccion a La Familia (con subtitlos)</a></h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/TnwmFK1Odqo' target='_blank'>Repaso y Explicacion</a></h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://youtu.be/tZk1fKC_7hQ' target='_blank'>Conversacion (sin subtitulos)</a> </h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://youtu.be/5gYPPZFOO6M' target='_blank'>Conversacion (con subtitulos)</a> </h5>", unsafe_allow_html=True)  
            st.markdown("<h5> <a href='https://youtu.be/tKMpJxq7wNk' target='_blank'>Cultura Sorda</a> </h5>", unsafe_allow_html=True)

            st.divider()

            st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
        
            st.markdown("<h5> <a href='https://youtu.be/WsoxPTw9j9U' target='_blank'>Vocabulario</a> para la semana que viene</h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://edpuzzle.com/media/633642ed68206040f25bc382' target='_blank'>Practica 1</a></h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://edpuzzle.com/media/633750f5389ee741763d8d57' target='_blank'>Practica 2</a></h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://edpuzzle.com/media/63375bff25e87940d4c32e08' target='_blank'>Practica 3</a></h5>", unsafe_allow_html=True)
            st.divider()
            
            components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQd8Y-xcWg9rS517V1gkm3m7O_sEKq_OSo4nQxS2RI2TFew0eR1yjqb1_mhLUfZ9CW1hrApe8mbHNLj/embed?start=false&loop=false&delayms=3000", height=480)
