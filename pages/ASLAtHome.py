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
            st.markdown("<h5> <a href='https://www.asd-1817.org/deaf-schools' target='_blank'>Escuelas para los Sordos</a> en EEUU </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://www.diglo.com/vibrating-clocks-and-watches/alarm-clocks;d=3;c=31;s=311' target='_blank'>Alarma de Reloj</a> para personas Sordos </h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://www.diglo.com/shop-by-alert-trigger/doorbell-and-door-knock;d=3;c=32;s=323' target='_blank'>Timbre</a> con luz para personas Sordos </h5>", unsafe_allow_html=True)     
            st.markdown("<h5> <a href='https://www.diglo.com/shop-by-alert-trigger/smoke-and-fire;d=3;c=32;s=328' target='_blank'>Alarma de Incendios</a> para personas Sordos </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://purplevrs.com/espanol' target='_blank'>Telefono de Video</a> para personas Sordos </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://apps.apple.com/us/app/intersign-asl-learn-now/id1567327543' target='_blank'>App para aprender</a> para iPhone </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://play.google.com/store/apps/details?id=intersign.learn.asl&hl=en_US&gl=US' target='_blank'>App para aprender</a> para Android </h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/Pt2_EjmtUp8' target='_blank'>Historia de ASL</a></h5>", unsafe_allow_html=True)

            st.divider()

            st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
        
            st.markdown("<h5> <a href='https://youtu.be/dJBLpQFhujo' target='_blank'>Vocabulario</a> para la semana que viene</h5>", unsafe_allow_html=True)
            st.divider()
            
            components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ4wlJOjhmNap4RDFiDtqNi1cv2PvEsdZnP4ANcRsVCCDgK0NrpYYLfI5BgwVZzlycwNwmvlwU4qnNt/embed?start=false&loop=false&delayms=3000", height=480)

def segunda_semana():
    st.subheader('Segunda Semana: Capitulo 1')
    cont_2 = st.container()

    outer_col_2 = st.columns([4, 1])            
    with cont_2:
        
        with outer_col_2[0]:
            st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/F_TOHsNTfwo' target='_blank'><img src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/Dictionary-amico.png' alt='Vocabulario' width='100' height='100'/>Vocabulario</a></h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/UaxbOjwRDDw' target='_blank'><img src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Screenshot%202023-10-18%20at%209.41.36%20PM.png' alt='Libro' width='100' height='100'/>Libro</a></h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/kLiRtHD1Oqc' target='_blank'><img src='https://i9.ytimg.com/vi_webp/kLiRtHD1Oqc/mq2.webp?sqp=CKDmwqkG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLDSgFEAmOs8OJ_grJt-IdKgsHcy1A' width='200' height='100'/>Vocabulario Extra</a></h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/YzButzmbrTw' target='_blank'><img src='https://i9.ytimg.com/vi_webp/YzButzmbrTw/mq2.webp?sqp=CMzowqkG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLBo6eI6xaMrO7VsrdaCzwEXvKmZwg' width='200' height='100'/>Conversación (sin subtítlos)</a></h5>", unsafe_allow_html=True)
            st.markdown("<h5> <a href='https://youtu.be/BtEIgRvVGg8' target='_blank'><img src='https://i9.ytimg.com/vi_webp/YzButzmbrTw/mq2.webp?sqp=CMzowqkG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLBo6eI6xaMrO7VsrdaCzwEXvKmZwg' width='200' height='100'/>Conversación (con subtítulos)</a></h5>", unsafe_allow_html=True)


            st.divider()

            st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
        
            st.markdown("<h5> <a href='https://youtu.be/F_TOHsNTfwo' target='_blank'>Practicar Vocabulario</a> para la semana que viene</h5>", unsafe_allow_html=True)
            st.divider()
            
            components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSb2QAbLy6AheIEJ30YPF-RYjE5gw1Yt7Ovw2wO8Mz2XFUc_MGg2P-8E2i4tlHoiwxXYPGFRE3y1HQn/embed?start=false&loop=false&delayms=3000", height=480)
