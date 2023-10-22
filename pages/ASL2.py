import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from st_pages import Page, Section,show_pages
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
def set_styles():
    st.write("""
        <style>
        .tab {
            display: flex;
            margin-left: 1em;
        }

        </style>
    """, unsafe_allow_html=True)

def primera_semana():
    st.subheader('Primera Semana: Introducción')
    cont_1 = st.container()

    outer_col_1 = st.columns([4, 1])            
    with cont_1:
        
        with outer_col_1[0]:
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
            
            components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ4wlJOjhmNap4RDFiDtqNi1cv2PvEsdZnP4ANcRsVCCDgK0NrpYYLfI5BgwVZzlycwNwmvlwU4qnNt/embed?start=false&loop=false&delayms=3000", height=480)

def segunda_semana():
    set_styles()
    st.markdown("<h2 style='text-align: center; color: white;'><u>Videos</u></h2>", unsafe_allow_html=True)
    clms2 = st.columns([1,1])
    with clms2[0]:
      st.title('')
      st.title('')
      st.subheader('Introducción')
    with clms2[1]:
      st.video('https://youtu.be/c1T1CoU0luo')

    st.markdown("<h3 style='text-align: center; color: white;'><u>Lección 1</u></h3>", unsafe_allow_html=True)
    clms3 = st.columns([1,1])
    with clms3[0]:
      st.title('')
      st.title('')
      st.subheader('Vocabulario y Frases')
    with clms3[1]:
      st.video('https://youtu.be/CD9CUAlcRW4')
    clms4 = st.columns([1,1])
    with clms4[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (sin subtítlos) 🔇')
    with clms4[1]:
      st.video('https://youtu.be/a6bMKje9kOY')
    clms5 = st.columns([1,1])
    with clms5[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (con subtítulos) 🔈')
    with clms5[1]:
      st.video('https://youtu.be/fVmnEqqhlpw')

    clms6 = st.columns([1,1])
    with clms6[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (sin subtítulos) 🔇')
    with clms6[1]:
      st.video('https://youtu.be/tZk1fKC_7hQ')
    clms7 = st.columns([1,1])
    with clms7[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (con subtítulos) 🔈')
    with clms7[1]:
      st.video('https://youtu.be/5gYPPZFOO6M')

    st.markdown("<h4 style='text-align: center; color: white;'><u>Lección 2</u></h4>", unsafe_allow_html=True)
    clms8 = st.columns([1,1])
    with clms8[0]:
        st.title('')
        st.title('')
        st.subheader('Vocabulario y Frases')

    with clms8[1]:
        st.video('https://youtu.be/qxd4OUEOCJg')
    clms9 = st.columns([1,1])
    with clms9[0]:
        st.title('')
        st.title('')
        st.subheader('Diálogo (sin subtítlos) 🔇')  
    with clms9[1]:
        st.video('https://youtu.be/_SDd08h_UEM')
    clms10=st.columns([1,1])
    with clms10[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (con subtítulos) 🔈')
    with clms10[1]:
      st.video('https://youtu.be/KOUtXRQ3kFw')
    clms11=st.columns([1,1])
    with clms11[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (sin subtítulos) 🔇')
    with clms11[1]:
      st.video('https://youtu.be/JHFhfpjI3CE')
    clms12=st.columns([1,1])
    with clms12[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (con subtítulos) 🔈')
    with clms12[1]:
      st.video('https://youtu.be/x494aKUmEKM')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Lección 3</u></h4>", unsafe_allow_html=True)
    clms13=st.columns([1,1])
    with clms13[0]:
      st.title('')
      st.title('')
      st.subheader('Vocabulario')
    with clms13[1]:
      st.video('https://youtu.be/_kva3v4OB2E')
    clms14=st.columns([1,1])
    with clms14[0]:
      st.title('')
      st.title('')
      st.subheader('Frases')
    with clms14[1]:
      st.video('https://youtu.be/IQyhNdrhuR8')
    clms15=st.columns([1,1])
    with clms15[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (sin subtítlos) 🔇')
    with clms15[1]:
      st.video('https://youtu.be/z1EEtsE79-w')
    clms16=st.columns([1,1])
    with clms16[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (con subtítlos) 🔈')
    with clms16[1]:
      st.video('https://youtu.be/5QM2LGdQWvs')
    clms17=st.columns([1,1])
    with clms17[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (sin subtítulos) 🔇')
    with clms17[1]:
      st.video('https://youtu.be/8-9YtAezNAE')
    clms18=st.columns([1,1])
    with clms18[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (con subtítulos) 🔈')
    with clms18[1]:
      st.video('https://youtu.be/XeXLA8-rWyo')
    clms19=st.columns([1,1])
    st.markdown("<h4 style='text-align: center; color: white;'><u>Lección 4</u></h4>", unsafe_allow_html=True)
    clms20=st.columns([1,1])
    with clms20[0]:
      st.title('')
      st.title('')
      st.subheader('Vocabulario y Frases')
    with clms20[1]:
      st.video('https://youtu.be/OZL7UyN6wSw')
    clms22=st.columns([1,1])
    with clms22[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (sin subtítlos) 🔇')
    with clms22[1]:
      st.video('https://youtu.be/ZABG-Zl5qzE')
    clms23=st.columns([1,1])
    with clms23[0]:
      st.title('')
      st.title('')
      st.subheader('Diálogo (con subtítlos)')
    with clms23[1]:
      st.video('https://youtu.be/z1EEtsE79-w')
    clms24=st.columns([1,1])
    with clms24[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (sin subtítulos) 🔇')
    with clms24[1]:
      st.video('https://youtu.be/beZlTXitb0g')
    clms25=st.columns([1,1])
    with clms25[0]:
      st.title('')
      st.title('')
      st.subheader('Conversación (con subtítulos) 🔈')
    with clms25[1]:
      st.video('https://youtu.be/qktiKSw2kpQ')
    st.divider()
    clms26=st.columns([1,1])
    with clms26[0]:
      st.title('')
      st.title('')
      st.subheader('Cultura')
    with clms26[1]:
      st.video('https://youtu.be/t7HzlXNmFJc')
    clms27=st.columns([1,1])
    with clms27[0]:
      st.title('')
      st.title('')
      st.subheader('Gramática')
    with clms27[1]:
      st.video('https://youtu.be/nBCvy22r6bo')
    clms28=st.columns([1,1])
    with clms28[0]:
      st.title('')
      st.title('')
      st.subheader('Cuento (sin subtítulos) 🔇')
    with clms28[1]:
      st.video('https://youtu.be/a0s8Zw6T3Fw')  
    clms29=st.columns([1,1])
    with clms29[0]:
      st.title('')
      st.title('')
      st.subheader('Cuento (con subtítulos) 🔈')
    with clms29[1]:
      st.video('https://youtu.be/GLXz2s5jBAw')    
    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms30=st.columns([1,1])
    with clms30[0]:
      st.title('')
      st.title('')
      st.subheader('Vocabulario para la semana que viene')
    with clms30[1]:
      st.video('https://youtu.be/sVyvzKH_Nsg')  
    st.divider()
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ1DBN424b45UbbrNNEHmSvzFqMDfsnLSR2nLK2eS93kdLU3bdQep_btALoKoWxZu0K644csijPRwuP/embed?start=false&loop=false&delayms=3000", height=480)
