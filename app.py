import streamlit as st
from PIL import Image
import pytesseract

# Configurar el título de la aplicación
st.title("Analizador de Pantallas Web")

# Cargar imagen desde el usuario
uploaded_file = st.file_uploader("Sube una captura de pantalla", type=["jpg", "png", "jpeg"])

# Si el usuario carga una imagen
if uploaded_file is not None:
    # Abrir la imagen y mostrarla
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada", use_column_width=True)

    # Proceso de OCR para extraer texto
    st.write("### Análisis del contenido:")
    with st.spinner("Procesando la imagen..."):
        try:
            # Extraer texto de la imagen
            extracted_text = pytesseract.image_to_string(image)

            # Mostrar el texto detectado
            if extracted_text.strip():
                st.write("**Texto detectado:**")
                st.text(extracted_text)
            else:
                st.write("No se detectó texto en la imagen.")
        except Exception as e:
            st.error(f"Error al procesar la imagen: {e}")

    st.write("### Descripción general:")
    st.write("Esta imagen ha sido analizada para extraer texto visible y detectar posibles actividades relacionadas con su contenido.")

