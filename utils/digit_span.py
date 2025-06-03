import streamlit as st
import random
import time

def iniciar_digit_span():
    if 'digit_ronda' not in st.session_state:
        st.session_state.digit_ronda = 0
        st.session_state.digit_resultados = []
        st.session_state.digit_secuencia = []
        st.session_state.digit_inicio = None
        nueva_secuencia()

def nueva_secuencia():
    longitud = 3 + st.session_state.digit_ronda  # Empezamos con 3 dígitos
    st.session_state.digit_secuencia = [str(random.randint(0, 9)) for _ in range(longitud)]
    st.session_state.digit_inicio = None
    st.session_state.digit_mostrada = False

def mostrar_secuencia():
    if not st.session_state.digit_mostrada:
        st.markdown(f"### Memoriza esta secuencia")
        st.markdown(f"<h2>{' '.join(st.session_state.digit_secuencia)}</h2>", unsafe_allow_html=True)
        if st.button("Siguiente"):
            st.session_state.digit_mostrada = True
            st.session_state.digit_inicio = time.time()
            st.rerun()

    else:
        respuesta = st.text_input("Escribe la secuencia:")
        if st.button("Enviar"):
            tiempo = round(time.time() - st.session_state.digit_inicio, 2)
            correcta = respuesta.strip().replace(" ", "") == ''.join(st.session_state.digit_secuencia)
            st.session_state.digit_resultados.append((correcta, tiempo))
            st.session_state.digit_ronda += 1
            if st.session_state.digit_ronda >= 5:
                return True  # Fin del test
            else:
                nueva_secuencia()
                st.rerun()

    return False
