import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from streamlit.components.v1 import html
from st_pages import Page,show_pages
import csv
from email.mime.multipart import MIMEMultipart
import mimetypes
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from PIL import Image
import smtplib
from pydub import AudioSegment
from pydub.playback import play
import time

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
    Page("pages/11_Form.py", "Formulario")
])

def set_styles():
    st.write("""
        <style>
        h5 {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        a {
            background-color: #92E3A9;

            }
            audio::-webkit-media-controls-timeline,
            video::-webkit-media-controls-timeline {
                display: none;
            }
            audio::-webkit-media-controls-current-time-display,
            audio::-webkit-media-controls-time-remaining-display {
                display: none;
            }
            audio::-webkit-media-controls-panel {
              max-width: 20%;
            }
            audio::-webkit-media-controls-timeline-container {
                max-width: 20%;
            }
            audio::-webkit-media-controls-volume-slider-container {
                max-width: 20%;
            }

        </style>
    """, unsafe_allow_html=True)


github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/nombre.m4a"

# Display the image using raw HTML
image_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/play.png"  # Replace with the URL of your image

# JavaScript code for playing audio on image click
audio_code = f"""
<audio id="myAudio" src="{github_audio_url}" height="5"></audio>
<script>
    function playAudio() {{
        var audio = document.getElementById('myAudio');
        audio.play();
    }}
</script>
"""

# Display the image and attach the JavaScript code

def send_email(sender, password, receiver, smtp_server, smtp_port, email_message, subject, attachments=None):
    
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender, password)
    text = email_message.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()
    
if __name__ == '__main__':
    set_styles()
    message = ""
    img5pm = Image.open('5pm.jpeg')
    img6pm = Image.open('6pm.jpeg')
    img7pm = Image.open('7pm.jpeg')
    img730pm = Image.open('730pm.jpeg')
    img11am = Image.open('11am.jpeg')
    img12pm = Image.open('12pm.jpeg')
    img1pm = Image.open('1pm.jpeg')
    img10am = Image.open('10am.jpeg')
    with st.form("Tomar clase de ASL"):
        st.header("¿Como se llama usted?") 

        github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/nombre.m4a"
        html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50"/></div>{audio_code}', height=50)
        nombre = st.text_input(label = "", placeholder = "Entrar su nombre", label_visibility= "collapsed")
        col1, col2, col3= st.columns([.5, .2, .3])
        with col1:
            st.header("¿Cual es su correo electronico?")
        with col2:
            st.audio('email.m4a')
        email = st.text_input(label = "", placeholder = "Entrar su correo electronico", label_visibility= "collapsed")

        col1, col2, col3= st.columns([.5, .2, .3])
        with col1:
            st.header("¿Cual es su número de teléfono?")
        with col2:
            st.audio('telefono.m4a')
        telefono = st.text_input(label = "", placeholder = "Entrar su número de teléfono", label_visibility= "collapsed")

        col1, col2, col3= st.columns([.7, .1, .2])
        with col1:
            st.header("¿Usted ha tomado clases de lengua de señas antes?")
        with col2:
            st.audio('clases.m4a')
        clases_antes = st.radio(label = "", options = ["Si", "No"], label_visibility= "collapsed")
        
        col1, col2, col3= st.columns([.4, .1, .5])
        with col1:
            st.header("¿Cual temas ya sabe usted?")
        with col2:
            st.audio('temas.m4a')

        col1, col2, col3= st.columns([.2, .1, .7])
        with col1:
            bravo1 = st.checkbox("familia y básicos (Bravo 1)")
        with col2:
            st.audio('bravo1.m4a')
        bravo2 = st.checkbox("desayuno (Bravo 2)")
        bravo3 = st.checkbox("casa (Bravo 3)")
        bravo4 = st.checkbox("comida y ir de compras (Bravo 4)")
        bravo6 = st.checkbox("colores y letras (Bravo 6)")
        bravo7 = st.checkbox("escuela (Bravo 7)")
        asl1 = st.checkbox("hora de comer (ASL En Casa 1)")
        asl2 = st.checkbox("hora de bañar (ASL En Casa 2)")
        asl3 = st.checkbox("hora de cambiar el pañal (ASL En Casa 3)")
        asl4 = st.checkbox("hora de leer (ASL En Casa 4)")

        st.header("¿Cuantos años tiene su hijo sordo?")
        hijo_edad = st.radio(label="", label_visibility = "collapsed", options = ["0-4 años", "5+ años", "Soy maestro"])
        st.divider()
        st.header("¿Cuando se puede tomar clases? (Escoja todos que se puede)")
        st.subheader("Las horas son de tiempo Pacifico.  Mira a la mapa para saber tiempo en su area.")
        st.write("")
        st.subheader("ASL 1 (Primer Semestre)")
        lunes1 = st.checkbox("Lunes a las 7 pm", key="lunes1")
        st.image(img7pm, width=400)
        martes15 = st.checkbox("Martes a las 5 pm", key="martes15")
        st.image(img5pm, width=400)
        martes16 = st.checkbox("Martes a las 6 pm", key="martes16")
        st.image(img6pm, width=400)
        martes7 = st.checkbox("Martes a las 7 pm")
        st.image(img7pm, width=400)
        miercoles6 = st.checkbox("Miercoles a las 6 pm")
        st.image(img6pm, width=400)
        miercoles7 = st.checkbox("Miercoles a las 7 pm")
        st.image(img7pm, width=400)
        st.divider()

        st.subheader("ASL 2 (Segundo Semestre)")
        lunes5 = st.checkbox("Lunes a las 5 pm")
        st.image(img5pm, width=400)
        lunes6 = st.checkbox("Lunes a las 6 pm")
        st.image(img6pm, width=400)
        lunes2 = st.checkbox("Lunes a las 7 pm", key="lunes2")
        st.image(img7pm, width=400)
        martes2 = st.checkbox("Martes a las 6 pm", key="martes2")
        st.image(img6pm, width=400)
        viernes7 = st.checkbox("Viernes a las 7 pm")
        st.image(img7pm, width=400)
        st.divider()

        st.subheader("ASL 3 (Tercer Semestre)")
        martes3 = st.checkbox("Martes a las 5 pm", key="martes3")
        st.image(img5pm, width=400)
        martes730 = st.checkbox("Martes a las 7:30 pm")
        st.image(img730pm, width=400)
        jueves12 = st.checkbox("Jueves a las 12 pm")
        st.image(img12pm, width=400)
        sabado11 = st.checkbox("Sabado a las 11 am")
        st.image(img11am, width=400)
        st.divider()

        st.subheader("ASL En Casa (niños de 0-4 años)")
        lunes7 = st.checkbox("Lunes a las 7 pm")
        st.image(img7pm, width=400)
        miercoles5 = st.checkbox("Miercoles a las 5 pm")
        st.image(img5pm, width=400)
        st.divider()

        st.subheader("Necesito otra horario.  Estoy disponible...")
        sabadoother12 = st.checkbox("Sabado a las 12 pm", key='sabadoother12')
        st.image(img12pm, width=400)
        sabadoother1 = st.checkbox("Sabado a la 1 pm", key='sabadoother1')
        st.image(img1pm, width=400)
        domingoother10 = st.checkbox("Domingo a las 10 am", key='domingoother10')
        st.image(img10am, width=400)
        domingoother11 = st.checkbox("Domingo a las 11 am", key='domingoother11')
        st.image(img11am, width=400)
        domingoother12 = st.checkbox("Domingo a las 12 pm", key='domingoother12')
        st.image(img12pm, width=400)
        st.divider()

        st.write("¿Cual es el mejor modo de contacto?")
        llamar = st.checkbox("Llamada")
        texto = st.checkbox("Texto")
        correo = st.checkbox("Correo Electronico")
            
        submit_res = st.form_submit_button(label="Entregar")


        if submit_res:
            with open('profiles1.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                field = ["name", "email", "phone number", "Previous classes", "Bravo1", "Bravo2", "Bravo3", "Bravo4", "Bravo6", "Bravo7", "ASL1", "ASL2", "ASL3", "ASL4", "Child Age", 
                "L7", "M5", "M6", "M7", "Mi6", "Mi7", "L5", "L6", "L7_2", "M6_2", "V7", "M5_3", "M730", "J12", "S12", "L7_Casa", "Mi5", "S12",
                "S1", "D10", "D11", "D12", "Llamar", "Texto", "Correo"]
                
                writer.writerow(field)
                writer.writerow([nombre, correo, telefono, clases_antes, bravo1, bravo2, bravo3, bravo4, bravo6, bravo7, asl1, asl2, asl3, asl4, hijo_edad,
                lunes1, martes15, martes16, martes7, miercoles6, miercoles7, lunes6, lunes7, lunes2, martes2, viernes7, martes3, martes730, jueves12, sabado11, lunes7, miercoles5, sabadoother12, sabadoother1,
                domingoother10,domingoother11, domingoother12, llamar, texto, correo])
            
            msg = MIMEMultipart()
            fileToSend = 'profiles1.csv'
            ctype, encoding = mimetypes.guess_type('profiles1.csv')
            if ctype is None or encoding is not None:
                ctype = "application/octet-stream"

            maintype, subtype = ctype.split("/", 1)

            if maintype == "text":
                fp = open(fileToSend)
                # Note: we should handle calculating the charset
                attachment = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == "image":
                fp = open(fileToSend, "rb")
                attachment = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == "audio":
                fp = open(fileToSend, "rb")
                attachment = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
            else:
                fp = open(fileToSend, "rb")
                attachment = MIMEBase(maintype, subtype)
                attachment.set_payload(fp.read())
                fp.close()
                encoders.encode_base64(attachment)
            attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
            msg.attach(attachment)


            send_email(sender = st.secrets["SENDER_ADDRESS"], password = st.secrets["SENDER_PASSWORD"], receiver = "celena.a.ponce@gmail.com", smtp_server = st.secrets["SMTP_SERVER_ADDRESS"], smtp_port = st.secrets["PORT"], email_message = msg, subject = "")
            
