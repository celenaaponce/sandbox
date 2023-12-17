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

def cuarta_semana():
    st.subheader('Capitulo 2 Pt 1')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)

    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://youtu.be/7361Wr6W9p4')
    clms11 = st.columns([1,1])
    with clms11[0]:
        st.title('')
        st.markdown('<h5>Libro de Hora de Bañarse</h5>', unsafe_allow_html=True)
    with clms11[1]:  
        st.video('https://youtu.be/4TmdTAaPYdA')
    clms12 = st.columns([1,1])
    with clms12[0]:
        st.title('')
        st.markdown('<h5>Vocabulario Extra</h5>', unsafe_allow_html=True)
    with clms12[1]: 
        st.video('https://youtu.be/gxGKiFP7G0U')
    st.divider()
    clms13 = st.columns([1,1])
    with clms13[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para de la Cabeza a los Pies</h5>', unsafe_allow_html=True)
    with clms13[1]: 
        st.video('https://youtu.be/UV-SadXiTh0')
    clms14 = st.columns([1,1])
    with clms14[0]:
        st.title('')
        st.markdown('<h5>Libro de la Cabeza a los Pies</h5>', unsafe_allow_html=True)
    with clms14[1]: 
        st.video('https://youtu.be/tvyr6wu4dL4')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms15 = st.columns([1,1])
    with clms15[0]:
        st.title('')
        st.markdown('<h5>Practicar Vocabulario</h5>', unsafe_allow_html=True)
    with clms15[1]:
        st.video('https://youtu.be/7361Wr6W9p4')
    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vS9kBtF4zqp1dtQBzaNHIxG22c8cTTME6K5xL09JldgZ3zX2ONGkYVX52FT0XL22vLjwWM23j0brXyk/embed?start=false&loop=false&delayms=3000", height=480)

def quinta_semana():
    st.subheader('Capitulo 2 Pt 2')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)

    clms1 = st.columns([1,1])
    with clms1[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms1[1]:
        st.video('https://youtu.be/7361Wr6W9p4')
    clms11 = st.columns([1,1])
    with clms11[0]:
        st.title('')
        st.markdown('<h5>Frases</h5>', unsafe_allow_html=True)
    with clms11[1]:  
        st.video('https://youtu.be/LHKtYB_w_RU?si=FwGdPZ9eCoId1TVQ')
    clms12 = st.columns([1,1])
    with clms12[0]:
        st.title('')
        st.markdown('<h5>Más Frases</h5>', unsafe_allow_html=True)
    with clms12[1]: 
        st.video('https://youtu.be/rp3AMCdKxdI?si=mVT9zedbk_dRI2Gj')
    clms13 = st.columns([1,1])
    with clms13[0]:
        st.title('')
        st.markdown('<h5>Aun Más Frases</h5>', unsafe_allow_html=True)
    with clms13[1]: 
        st.video('https://youtu.be/ldSbwWtKf6A?si=QSiW_7Rc-mJXZCHM')
    clms14 = st.columns([1,1])
    with clms14[0]:
        st.title('')
        st.markdown('<h5>Libro</h5>', unsafe_allow_html=True)
    with clms14[1]: 
        st.video('https://youtu.be/BlPrDMZUzkY')    
    clms15 = st.columns([1,1])
    with clms15[0]:
        st.title('')
        st.markdown('<h5>Otra Frases</h5>', unsafe_allow_html=True)
    with clms15[1]: 
        st.video('https://youtu.be/CcxmBTfDlMo')   
    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms15 = st.columns([1,1])
    with clms15[0]:
        st.title('')
        st.markdown('<h5>Nuevo Vocabulario</h5>', unsafe_allow_html=True)
    with clms15[1]:
        st.video('https://youtu.be/9q4e_fQB6No')
    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQDz2mgnEZK_yCCscpVGqeYxXX1ZYHPER5m1VkECKBv_IPBkdw-RHUf-0kLOI2gBkwx94Cj0reBjJ4W/embed?start=false&loop=false&delayms=3000", height=480)