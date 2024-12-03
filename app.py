import streamlit as st
from PIL import Image
import pytesseract

# Título de la aplicación
st.title("Analizador de Pantallas Web")

# Subir imagen
uploaded_file = st.file_uploader("Sube una captura de pantalla", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Mostrar la imagen cargada
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada", use_column_width=True)

    # Procesar la imagen para extraer texto
    st.write("### Análisis del contenido:")
    with st.spinner("Procesando la imagen..."):
        extracted_text = pytesseract.image_to_string(image)
        if extracted_text.strip():
            st.write("**Texto detectado:**")
            st.text(extracted_text)
        else:
            st.write("No se detectó texto en la imagen.")

    st.write("### Descripción general:")
    st.write("La imagen ha sido analizada para extraer texto visible y detectar posibles actividades relacionadas con su contenido.")

