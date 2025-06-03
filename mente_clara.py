import streamlit as st
from utils import stroop
from utils import digit_span


# Inicializar estado de navegación
if 'pantalla' not in st.session_state:
    st.session_state.pantalla = 'inicio'

def cambiar_pantalla(nueva):
    st.session_state.pantalla = nueva

# --- Pantalla de inicio ---
if st.session_state.pantalla == 'inicio':
    st.title("🧠 Bienvenido a Mente Clara")
    st.markdown("Esta evaluación interactiva te ayudará a conocer mejor tu atención y memoria.\n\n**No es un diagnóstico médico.**")
    if st.button("Comenzar evaluación"):
        cambiar_pantalla('intro')

# --- Introducción general ---
elif st.session_state.pantalla == 'intro':
    st.header("¿Qué harás?")
    st.markdown("""
    Realizarás tres pruebas cognitivas:
    - 🟥 **Stroop Test**: atención y autocontrol
    - 🔢 **Digit Span**: memoria inmediata
    - 🎯 **Atención sostenida**: enfoque visual

    Hazlo con calma. Solo tú verás los resultados.
    """)
    if st.button("Empezar primera prueba"):
        cambiar_pantalla('stroop_intro')

# --- Instrucciones Stroop ---
elif st.session_state.pantalla == 'stroop_intro':
    st.subheader("Prueba 1: Stroop Test")
    st.markdown("Selecciona el color en el que está escrita la palabra, no lo que dice.")
    if st.button("Iniciar Stroop"):
        cambiar_pantalla('stroop')

# --- Stroop Test (placeholder) ---
elif st.session_state.pantalla == 'stroop':
    stroop.iniciar_stroop()
    stroop.mostrar_ronda(callback_siguiente=lambda: cambiar_pantalla('digit_intro'))

# --- Instrucciones Digit Span ---
elif st.session_state.pantalla == 'digit_intro':
    st.subheader("Prueba 2: Memoria de dígitos")
    st.markdown("Memoriza y repite secuencias de números.")
    if st.button("Iniciar Digit Span"):
        cambiar_pantalla('digit')

# --- Digit Span Test ---
elif st.session_state.pantalla == 'digit':
    digit_span.iniciar_digit_span()
    fin_test = digit_span.mostrar_secuencia()
    if fin_test:
        cambiar_pantalla('atencion_intro')

# --- Instrucciones Atención sostenida ---
elif st.session_state.pantalla == 'atencion_intro':
    st.subheader("Prueba 3: Atención sostenida")
    st.markdown("Encuentra el símbolo objetivo entre distractores.")
    if st.button("Iniciar prueba de atención"):
        cambiar_pantalla('atencion')

# --- Atención sostenida (placeholder) ---
elif st.session_state.pantalla == 'atencion':
    st.text("Aquí irá la lógica del test de atención.")
    if st.button("Ver resultados"):
        cambiar_pantalla('resultados')

# --- Resultados finales ---
elif st.session_state.pantalla == 'resultados':
    st.success("¡Has completado la evaluación!")
    st.markdown("Aquí aparecerá un resumen de tus resultados.")
    st.button("Volver al inicio", on_click=lambda: cambiar_pantalla('inicio'))
