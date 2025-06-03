import streamlit as st
from utils import stroop
from utils import digit_span
from utils import atencion

def calcular_resumen(resultados):
    total = len(resultados)
    aciertos = sum(1 for correcto, _ in resultados if correcto)
    tiempo_promedio = round(sum(t for _, t in resultados) / total, 2) if total else 0
    return aciertos, total, tiempo_promedio

def mensaje_motivador(aciertos, total):
    if aciertos == total:
        return "¡Excelente! 🌟 Has acertado todas las respuestas."
    elif aciertos >= total * 0.7:
        return "¡Muy bien! 🎯 Tienes un buen nivel de atención."
    else:
        return "No te desanimes. 💪 Sigue practicando y mejorando."


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
    atencion.iniciar_atencion()
    fin_test = atencion.mostrar_ronda(callback_siguiente=lambda: cambiar_pantalla('resultados'))

# --- Resultados finales ---
elif st.session_state.pantalla == 'resultados':
    st.title("🎉 ¡Resultados de tu evaluación!")

    # Stroop
    if 'stroop_resultados' in st.session_state:
        aciertos, total, tiempo = calcular_resumen(st.session_state.stroop_resultados)
        st.subheader("🟥 Stroop Test")
        st.markdown(f"**Aciertos:** {aciertos}/{total}")
        st.markdown(f"**Tiempo promedio:** {tiempo} segundos")
        st.info(mensaje_motivador(aciertos, total))

    # Digit Span
    if 'digit_resultados' in st.session_state:
        aciertos, total, tiempo = calcular_resumen(st.session_state.digit_resultados)
        st.subheader("🔢 Digit Span Test")
        st.markdown(f"**Aciertos:** {aciertos}/{total}")
        st.markdown(f"**Tiempo promedio:** {tiempo} segundos")
        st.info(mensaje_motivador(aciertos, total))

    # Atención sostenida
    if 'atencion_resultados' in st.session_state:
        aciertos, total, tiempo = calcular_resumen(st.session_state.atencion_resultados)
        st.subheader("🎯 Atención Sostenida")
        st.markdown(f"**Aciertos:** {aciertos}/{total}")
        st.markdown(f"**Tiempo promedio:** {tiempo} segundos")
        st.info(mensaje_motivador(aciertos, total))

    st.success("¡Gracias por participar en Mente Clara!")
    if st.button("Volver al inicio"):
        cambiar_pantalla('inicio')
