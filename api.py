import streamlit as st
import google.generativeai as genai

# Carga la clave de API de forma segura
try:
    API_KEY = "AIzaSyCbnTdgxfHuRDxk0Nvoa75b0h4UxNEnoDE"
except KeyError:
    st.error("No se encontró la clave de API en st.secrets.  Asegúrate de haber configurado secrets.toml correctamente.")
    st.stop()

# Configura la API de Gemini
genai.configure(api_key=API_KEY)

# Elige el modelo (asegúrate de tener acceso)
model = genai.GenerativeModel('gemini-1.5-pro-latest')  # Cambia si es necesario

st.title("Generador de Texto Gemini")

prompt = st.text_area("Ingresa tu prompt:", "Escribe un cuento corto sobre un viaje en el tiempo.")

if st.button("Generar"):
    with st.spinner("Generando respuesta..."):
        try:
            response = model.generate_content(prompt)
            st.write("Respuesta:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error al generar: {e}")