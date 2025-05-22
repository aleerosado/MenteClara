import streamlit as st
import random
import time

colores = {
    'Rojo': 'red',
    'Verde': 'green',
    'Azul': 'blue',
    'Amarillo': 'yellow'
}

def iniciar_stroop():
    if 'stroop_ronda' not in st.session_state:
        st.session_state.stroop_ronda = 0
        st.session_state.stroop_resultados = []
        st.session_state.stroop_inicio = None

def nueva_ronda():
    palabra = random.choice(list(colores.keys()))
    color_visual = random.choice(list(colores.values()))
    st.session_state.stroop_palabra = palabra
    st.session_state.stroop_color = color_visual
    st.session_state.stroop_inicio = time.time()

def mostrar_ronda(callback_siguiente):
    if 'stroop_palabra' not in st.session_state or 'stroop_color' not in st.session_state:
        nueva_ronda()
    st.markdown(f"### ¿En qué color está escrita esta palabra?")
    st.markdown(f"<h1 style='color:{st.session_state.stroop_color}'>{st.session_state.stroop_palabra}</h1>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    for idx, (nombre, css) in enumerate(colores.items()):
        with [col1, col2, col3, col4][idx]:
            if st.button(nombre):
                fin = time.time()
                tiempo = round(fin - st.session_state.stroop_inicio, 2)
                correcta = css == st.session_state.stroop_color
                st.session_state.stroop_resultados.append((correcta, tiempo))
                st.session_state.stroop_ronda += 1
                if st.session_state.stroop_ronda >= 5:
                    callback_siguiente()
                else:
                    nueva_ronda()
                    st.rerun()

