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
from streamlit_js_eval import streamlit_js_eval

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

phone = False
screen_width = streamlit_js_eval(js_expressions='screen.width', key = 'SCR')

if screen_width != None:
  if screen_width < 400:
      phone = True
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
        # JavaScript code for playing audio on image click

    with st.form("Tomar clase de ASL"):
        col1, col2 = st.columns([.1, .9])
        if not phone:
            with col2:
                st.header("¿Cómo se llama usted?") 
            with col1:
                    github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/nombre.m4a"
                    audio_code = f"""
                    <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                    <script>
                        function playAudio() {{
                            var audio = document.getElementById('myAudio');
                            audio.play();
                        }}
                    </script>
                    """
                    html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=50)
        else:
            st.header("¿Cómo se llama usted?") 
            st.audio('nombre.m4a')
        nombre = st.text_input(label = "", placeholder = "Entrar su nombre", label_visibility= "collapsed")
        if not phone:
            col2, col1 = st.columns([.1, .9])
            with col1:
                st.header("¿Cuál es su correo electronico?")
            with col2:
                    github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/email.m4a"
                    audio_code = f"""
                                <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                                <script>
                                    function playAudio() {{
                                        var audio = document.getElementById('myAudio');
                                        audio.play();
                                    }}
                                </script>
                                """
                    html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=50)
        else:
            st.header("¿Cuál es su correo electronico?")
            st.audio('email.m4a')
        email = st.text_input(label = "", placeholder = "Entrar su correo electronico", label_visibility= "collapsed")
        if not phone:
            col2, col1 = st.columns([.1, .9])
            with col1:
                st.header("¿Cuál es su número de teléfono?")
            with col2:
                    github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/telefono.m4a"
                    audio_code = f"""
                                <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                                <script>
                                    function playAudio() {{
                                        var audio = document.getElementById('myAudio');
                                        audio.play();
                                    }}
                                </script>
                                """
                    html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=50)
        else:
            st.header("¿Cuál es su número de teléfono?")
            st.audio('telefono.m4a')
        telefono = st.text_input(label = "", placeholder = "Entrar su número de teléfono", label_visibility= "collapsed")

        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:
                st.header("¿Usted ha tomado clases de lengua de señas antes?")
            with col1:
                    github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/clases.m4a"
                    audio_code = f"""
                                <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                                <script>
                                    function playAudio() {{
                                        var audio = document.getElementById('myAudio');
                                        audio.play();
                                    }}
                                </script>
                                """
                    html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=50)
        else:
            st.header("¿Usted ha tomado clases de lengua de señas antes?")
            st.audio('clases.m4a')
        clases_antes = st.radio(label = "", options = ["Si", "No"], label_visibility= "collapsed")
        if not phone:
            col1, col2= st.columns([.1, .9])
            with col2:
                st.header("¿Cuál temas ya sabe usted?")
            with col1:
                    github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/temas.m4a"
                    audio_code = f"""
                                <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                                <script>
                                    function playAudio() {{
                                        var audio = document.getElementById('myAudio');
                                        audio.play();
                                    }}
                                </script>
                                """
                    html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=50)
        else:
            st.header("¿Cuál temas ya sabe usted?")
            st.audio('temas.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:
                bravo1 = st.checkbox("familia y básicos (Bravo 1)")
            with col1:
                    github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/bravo1.m4a"
                    audio_code = f"""
                                <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                                <script>
                                    function playAudio() {{
                                        var audio = document.getElementById('myAudio');
                                        audio.play();
                                    }}
                                </script>
                                """
                    html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)
        else:
            bravo1 = st.checkbox("familia y básicos (Bravo 1)")
            st.audio('bravo1.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:
                bravo2 = st.checkbox("desayuno (Bravo 2)")
            with col1:            
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/bravo2.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            bravo2 = st.checkbox("desayuno (Bravo 2)")
            st.audio('bravo2.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:
                bravo3 = st.checkbox("casa (Bravo 3)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/casa.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            bravo3 = st.checkbox("casa (Bravo 3)")
            st.audio('bravo3.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:
                bravo4 = st.checkbox("comida y ir de compras (Bravo 4)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/bravo4.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            bravo4 = st.checkbox("comida y ir de compras (Bravo 4)")
            st.audio('bravo4.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:
                bravo6 = st.checkbox("colores y letras (Bravo 6)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/bravo6.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            bravo6 = st.checkbox("colores y letras (Bravo 6)")
            st.audio('bravo6.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:
                bravo7 = st.checkbox("escuela (Bravo 7)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/bravo7.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            bravo7 = st.checkbox("escuela (Bravo 7)")
            st.audio('bravo7.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:
                asl1 = st.checkbox("hora de comer (ASL En Casa 1)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/asl1.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            asl1 = st.checkbox("hora de comer (ASL En Casa 1)")
            st.audio('asl1.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:  
                asl2 = st.checkbox("hora de bañar (ASL En Casa 2)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/asl2.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            asl2 = st.checkbox("hora de bañar (ASL En Casa 2)")
            st.audio('asl2.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:             
                asl3 = st.checkbox("hora de cambiar el pañal (ASL En Casa 3)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/asl3.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            asl3 = st.checkbox("hora de cambiar el pañal (ASL En Casa 3)")
            st.audio('asl3.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2: 
                asl4 = st.checkbox("hora de leer (ASL En Casa 4)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/asl4.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
             asl4 = st.checkbox("hora de leer (ASL En Casa 4)")
             st.audio('asl4.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2: 
                st.header("¿Cuantos años tiene su hijo sordo?")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/edad.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            st.header("¿Cuantos años tiene su hijo sordo?")
            st.audio('edad.m4a')
        hijo_edad = st.radio(label="", label_visibility = "collapsed", options = ["0-4 años", "5+ años", "Soy maestro"])
        st.divider()
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:         
                st.header("¿Cuándo se puede tomar clases? (Escoja todos que se puede)")
                st.subheader("Las horas son de tiempo Pacífico.  Mira a la mapa para saber la hora en su area.")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/tiempo.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            st.header("¿Cuándo se puede tomar clases? (Escoja todos que se puede)")
            st.subheader("Las horas son de tiempo Pacífico.  Mira a la mapa para saber la hora en su area.")
            st.audio('tiempo.m4a')
        st.write("")
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:
                st.subheader("ASL 1 (Primer Semestre)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/primer.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            st.subheader("ASL 1 (Primer Semestre)")
            st.audio('primer.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:        
                lunes1 = st.checkbox("Lunes a las 7 pm", key="lunes1")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/lunes7.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            lunes1 = st.checkbox("Lunes a las 7 pm", key="lunes1")
            st.audio('lunes7.m4a')
        st.image(img7pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                martes15 = st.checkbox("Martes a las 5 pm", key="martes15")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/martes5.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            martes15 = st.checkbox("Martes a las 5 pm", key="martes15")
            st.audio('martes5.m4a')        
        st.image(img5pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                martes16 = st.checkbox("Martes a las 6 pm", key="martes16")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/martes6.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            martes16 = st.checkbox("Martes a las 6 pm", key="martes16")
            st.audio('martes6.m4a')
        st.image(img6pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                martes7 = st.checkbox("Martes a las 7 pm")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/martes7.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            martes7 = st.checkbox("Martes a las 7 pm")
            st.audio('martes7.m4a')      
        st.image(img7pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                miercoles6 = st.checkbox("Miércoles a las 6 pm")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/miercoles6.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            miercoles6 = st.checkbox("Miércoles a las 6 pm")
            st.audio('miercoles6.m4a') 
        st.image(img6pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                miercoles7 = st.checkbox("Miércoles a las 7 pm")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/miercoles7.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            miercoles7 = st.checkbox("Miércoles a las 7 pm")
            st.audio('miercoles7.m4a')         
        st.image(img7pm, width=400)
        st.divider()
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                st.subheader("ASL 2 (Segundo Semestre)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/segundo.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            st.subheader("ASL 2 (Segundo Semestre)")
            st.audio('segundo.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                lunes5 = st.checkbox("Lunes a las 5 pm")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/lunes5.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            lunes5 = st.checkbox("Lunes a las 5 pm")
            st.audio('lunes5.m4a')
        st.image(img5pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                lunes6 = st.checkbox("Lunes a las 6 pm")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/lunes6.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            lunes6 = st.checkbox("Lunes a las 6 pm")
            st.audio('lunes6.m4a')
        st.image(img6pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                lunes2 = st.checkbox("Lunes a las 7 pm", key="lunes2")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/lunes7.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            lunes2 = st.checkbox("Lunes a las 7 pm", key="lunes2")
            st.audio('lunes7.m4a')        
        st.image(img7pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                martes2 = st.checkbox("Martes a las 6 pm", key="martes2")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/martes6.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            martes2 = st.checkbox("Martes a las 6 pm", key="martes2")
            st.audio('martes6.m4a')        
        st.image(img6pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                viernes7 = st.checkbox("Viernes a las 7 pm")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/viernes7.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            viernes7 = st.checkbox("Viernes a las 7 pm")
            st.audio('viernes7.m4a')       
        st.image(img7pm, width=400)
        st.divider()

        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                st.subheader("ASL 3 (Tercer Semestre)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/tercer.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            st.subheader("ASL 3 (Tercer Semestre)")
            st.audio('tercer.m4a')   
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                martes3 = st.checkbox("Martes a las 5 pm", key="martes3")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/martes5.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            martes3 = st.checkbox("Martes a las 5 pm", key="martes3")
            st.audio('martes5.m4a')              
        st.image(img5pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                martes730 = st.checkbox("Martes a las 7:30 pm")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/martes730.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            martes730 = st.checkbox("Martes a las 7:30 pm")
            st.audio('martes730.m4a')                     
        st.image(img730pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                jueves12 = st.checkbox("Jueves a las 12 pm")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/jueves12.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            jueves12 = st.checkbox("Jueves a las 12 pm")
            st.audio('jueves12.m4a')   
        st.image(img12pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                sabado11 = st.checkbox("sábado a las 11 am")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/sabado11.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            sabado11 = st.checkbox("sábado a las 11 am")
            st.audio('sabado11.m4a')        
        st.image(img11am, width=400)
        st.divider()
        
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                st.subheader("ASL En Casa (niños de 0-4 años)")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/encasa.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            st.subheader("ASL En Casa (niños de 0-4 años)")
            st.audio('encasa.m4a') 
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                lunes7 = st.checkbox("Lunes a las 7 pm")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/lunes7.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            lunes7 = st.checkbox("Lunes a las 7 pm")
            st.audio('lunes7.m4a')                
        st.image(img7pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                miercoles5 = st.checkbox("Miércoles a las 5 pm")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/miercoles5.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            miercoles5 = st.checkbox("Miércoles a las 5 pm")
            st.audio('miercoles5.m4a')       
        st.image(img5pm, width=400)
        st.divider()
        
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                st.subheader("Necesito otra horario.  Estoy disponible...")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/otro.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            st.subheader("Necesito otra horario.  Estoy disponible...")
            st.audio('otro.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                sabadoother12 = st.checkbox("Sábado a las 12 pm", key='sabadoother12')
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/sabado12.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            sabadoother12 = st.checkbox("Sábado a las 12 pm", key='sabadoother12')
            st.audio('sabado12.m4a')      
        st.image(img12pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                sabadoother1 = st.checkbox("Sábado a la 1 pm", key='sabadoother1')
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/sabado1.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            sabadoother1 = st.checkbox("Sábado a la 1 pm", key='sabadoother1')
            st.audio('sabado1.m4a')     
        st.image(img1pm, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                domingoother10 = st.checkbox("Domingo a las 10 am", key='domingoother10')
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/domingo10.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            domingoother10 = st.checkbox("Domingo a las 10 am", key='domingoother10')
            st.audio('domingo10.m4a')        
        st.image(img10am, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                domingoother11 = st.checkbox("Domingo a las 11 am", key='domingoother11')
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/domingo11.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            domingoother11 = st.checkbox("Domingo a las 11 am", key='domingoother11')
            st.audio('domingo11.m4a') 
        st.image(img11am, width=400)
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                domingoother12 = st.checkbox("Domingo a las 12 pm", key='domingoother12')
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/domingo12.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            domingoother12 = st.checkbox("Domingo a las 12 pm", key='domingoother12')
            st.audio('domingo12.m4a') 
        st.image(img12pm, width=400)
        st.divider()

        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                st.subheader("¿Cuál es el mejor modo de contacto?")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/contacto.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            st.subheader("¿Cuál es el mejor modo de contacto?")
            st.audio('contacto.m4a')
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                llamar = st.checkbox("Llamada")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/llamada.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            llamar = st.checkbox("Llamada")
            st.audio('llamada.m4a')        
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                texto = st.checkbox("Texto")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/texto.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            texto = st.checkbox("Texto")
            st.audio('texto.m4a')         
        if not phone:
            col1, col2 = st.columns([.1, .9])
            with col2:                
                correo = st.checkbox("Correo Electronico")
            with col1:
                github_audio_url = "https://raw.githubusercontent.com/celenaaponce/sandbox/main/correoelectronico.m4a"
                audio_code = f"""
                            <audio id="myAudio" src="{github_audio_url}" height="5"></audio>
                            <script>
                                function playAudio() {{
                                    var audio = document.getElementById('myAudio');
                                    audio.play();
                                }}
                            </script>
                            """
                html(f'<div onclick="playAudio()" style="cursor: pointer;" height="5"><img id="customImage" src="{image_url}" width="50" style="position: absolute; bottom: 0;"/></div>{audio_code}', height=30)  
        else:
            correo = st.checkbox("Correo Electronico")
            st.audio('correoelectronico.m4a')        
        
            
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
            st.header("Recibimos su formulario.  Contactamos pronto con el horario de su clase.  ¡Gracias!")

