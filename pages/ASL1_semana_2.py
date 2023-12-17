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
    st.header("Bienvenido a la clase de ASL 1.")
    st.header("Se puede mirar nuestro curriculo aqui:")
    tab5, tab6, tab7, tab8, tab9 = st.tabs([":white[Desayuno Pt 1]", ":white[Desayuno Pt 2]", ":white[Dia de Accion de Gracias]",
                                                                ":white[Contról Pt 1]", ":white[Contról Pt 2]"])

    with tab5:
            cuarta_semana()
    with tab6:
            quinta_semana()
    with tab7:
            holidays.thanksgiving()
    with tab8:
            sexta_semana()
    with tab9:
            septima_semana()

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

def cuarta_semana():
    set_styles()
    st.subheader('Desayuno Pt 1')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Introducción a La Lección</h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://youtu.be/69GxKWg_Sfw')
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicación</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/UITBHk6W-Vg')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversación (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/NpfgnYPpxT0')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversación (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/PdDmd0emQ40')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Cultura Sorda</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/5dW7MzA8hRY')

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
        st.markdown("<a href='https://edpuzzle.com/media/6344a92f0417234125240938' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/6344aa6069e69340e4b26847' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/6344ab67ba3797411f32bb8c' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTFT1lpMkQ8BK-lt6v60NsP5ILZCDlxvaQ-gGrMX_GIEMXmDupalvjNxglS0hS1ar2c97U7Hpm9RLJO/embed?start=false&loop=false&delayms=3000", height=480)

def quinta_semana():
    set_styles()
    st.subheader('Desayuno Pt 2')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/UITBHk6W-Vg')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversación (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/qM8_5FGazmA')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversación (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/6Hxpc-49B3Q')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Gramatica</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/bWqtdt6RMKs')
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Frases</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/8CvFI8d4aKg')
    clms30 = st.columns([1,1])
    with clms30[0]:
        st.title('')
        st.markdown('<h5>Cuento (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms30[1]:    
        st.video('https://youtu.be/V0pH_yLWG00')
    clms31 = st.columns([1,1])
    with clms31[0]:
        st.title('')
        st.markdown('<h5>Cuento (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms31[1]: 
        st.video('https://youtu.be/QLsApezec98')        
    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/Ffrz8E11BtY')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/63dc6ad1fe545641336a03ae' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/63dc7194d3243840f5b1480f' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTSFKvUdTSTKb6VdPLTwvsTT4Pzn0L_DH_lfc6GBTp-mgi3uNN8GZZyL-AnDGrpNkLlFy2K4TfGIqvc/embed?start=false&loop=false&delayms=3000", height=480)

def sexta_semana():
    set_styles()
    st.subheader('¿Dónde está el contról? Pt 1')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms21 = st.columns([1,1])
    with clms21[0]:
        st.title('')
        st.markdown('<h5>Introducción a La Lección</h5>', unsafe_allow_html=True)
    with clms21[1]:
        st.video('https://youtu.be/X0FjuzzV7Cc')
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Repaso y Explicación</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/tfz66mCa1V4')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversación (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/Dkbed5OSVh8')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversación (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/c32td3f85Mc')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Gramatica</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/vas3L7L0Y_I')

    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms27 = st.columns([1,1])
    with clms27[0]:
        st.title('')
        st.markdown('<h5>Vocabulario para la semana que viene</h5>', unsafe_allow_html=True)
    with clms27[1]:
        st.video('https://youtu.be/3KzhHmN2iQQ')
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/63f44c53815430414f6aa6b3' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/63f45261eaf221415bb8ccf3' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRNtQCOLJbGm47vieTI6GLxfSgh-IdCzw5yKa6EArwBS2_rKsnr78pV3r9SksJW2gzF2Fuf7E8jzkzM/embed?start=false&loop=false&delayms=3000", height=480)

def septima_semana():
    set_styles()
    st.subheader('¿Dónde está el contról? Pt 2')
    st.markdown("<h4 style='text-align: center; color: white;'><u>Videos</u></h4>", unsafe_allow_html=True)
    clms23 = st.columns([1,1])
    with clms23[0]:
        st.title('')
        st.markdown('<h5>Vocabulario</h5>', unsafe_allow_html=True)
    with clms23[1]:
        st.video('https://youtu.be/wH6DQEvPg3w')
    clms24 = st.columns([1,1])
    with clms24[0]:
        st.title('')
        st.markdown('<h5>Conversación (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms24[1]:    
        st.video('https://youtu.be/DPWS7MuTJTA')
    clms25 = st.columns([1,1])
    with clms25[0]:
        st.title('')
        st.markdown('<h5>Conversación (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms25[1]: 
        st.video('https://youtu.be/pz2z8UP7We8')
    clms26 = st.columns([1,1])
    with clms26[0]:
        st.title('')
        st.markdown('<h5>Cultura Sorda</h5>', unsafe_allow_html=True)
    with clms26[1]:
        st.video('https://youtu.be/OZu28_eeDq0')
    clms29 = st.columns([1,1])
    with clms29[0]:
        st.title('')
        st.markdown('<h5>Frases</h5>', unsafe_allow_html=True)
    with clms29[1]:
        st.video('https://youtu.be/mKKM5c5B27U')
    clms30 = st.columns([1,1])
    with clms30[0]:
        st.title('')
        st.markdown('<h5>Cuento (sin subtítulos) 🔇</h5>', unsafe_allow_html=True)
    with clms30[1]:    
        st.video('https://youtu.be/qkIXqIf9oNs')
    clms31 = st.columns([1,1])
    with clms31[0]:
        st.title('')
        st.markdown('<h5>Cuento (con subtítulos) 🔈</h5>', unsafe_allow_html=True)
    with clms31[1]: 
        st.video('https://youtu.be/EPMDpOO-lDI')        
    st.divider()

    st.markdown("<h4 style='text-align: center; color: white;'><u>Tarea</u></h4>", unsafe_allow_html=True)
    clms28 = st.columns([1,1])
    with clms28[0]:
        st.title('')
        st.markdown('<h5>Practica</h5>', unsafe_allow_html=True)
    with clms28[1]:
        st.markdown("<a href='https://edpuzzle.com/media/640bd6c89bbb9e42a124866b' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     
        st.markdown("<a href='https://edpuzzle.com/media/640e37f0b6a56042bd07b94c' target='_blank'><img style='float: left;' src='https://raw.githubusercontent.com/celenaaponce/sandbox/main/pages/Images/Screenshot%202023-10-22%20at%203.32.28%20PM.png' width='100' height='100'/></a>", unsafe_allow_html=True)     

    st.divider()
            
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ8stRFQOfu2FuAFsKrcmFSnmB6MZv4hPdR5FLOoKKik-VRNJE8Py2PHiJ-7B2JXBEie2I_CvnwShjR/embed?start=false&loop=false&delayms=3000", height=480)
main()