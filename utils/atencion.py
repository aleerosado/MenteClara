import streamlit as st
import random
import time

def iniciar_atencion():
    if 'atencion_ronda' not in st.session_state:
        st.session_state.atencion_ronda = 0
        st.session_state.atencion_resultados = []
        st.session_state.atencion_objetivo = None
        st.session_state.atencion_inicio = None
        nueva_ronda()

def nueva_ronda():
    formas = ['🔵', '🟥', '🔺', '⭐', '💚']
    # Elige el objetivo (uno nuevo cada ronda)
    st.session_state.atencion_objetivo = random.choice(formas)
    # Genera distractores (sin el objetivo)
    distractores = [f for f in formas if f != st.session_state.atencion_objetivo]
    opciones = random.sample(distractores, k=3)  # 3 distractores únicos
    # Inserta el objetivo en una posición aleatoria
    opciones.insert(random.randint(0, 3), st.session_state.atencion_objetivo)
    st.session_state.atencion_opciones = opciones
    st.session_state.atencion_inicio = time.time()


def mostrar_ronda(callback_siguiente):
    st.markdown("### Encuentra el siguiente símbolo:")
    st.markdown(f"<h2>{st.session_state.atencion_objetivo}</h2>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    for idx, forma in enumerate(st.session_state.atencion_opciones):
        with [col1, col2, col3, col4][idx]:
            if st.button(forma, key=f"atencion-{idx}-{forma}"):
                tiempo = round(time.time() - st.session_state.atencion_inicio, 2)
                correcta = forma == st.session_state.atencion_objetivo
                st.session_state.atencion_resultados.append((correcta, tiempo))
                st.session_state.atencion_ronda += 1
                if st.session_state.atencion_ronda >= 5:
                    callback_siguiente()
                else:
                    nueva_ronda()
                    st.rerun()
