import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np  # Necesario para generar datos aleatorios

df = pd.read_csv("csvsinnan.csv")
st.title("Salud mental en trabajo remoto")

# Personalización de la barra lateral
st.markdown("""
<style>
    [data-testid=stSidebar] {background-color: #10609d;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h1 style='color: white'>Opciones de color</h1>", unsafe_allow_html=True)
    st.title('Reproductor Musical desde YouTube')
    playlist_url = "https://www.youtube.com/playlist?list=PLHLua7lnY9X-uAKqwp0T23h3A4d-ZajTO"
    playlist_id = playlist_url.split('list=')[-1]
    components.iframe(f"https://www.youtube.com/embed/videoseries?list={playlist_id}", width=300, height=200)
    color_grafico = st.color_picker('Selecciona un color para el gráfico', '#007bff')

# Selección de tipo de gráfico
tipo_grafico = st.radio("Selecciona el tipo de gráfico", ["Barras", "Histograma"])

# Lista de columnas específicas permitidas para el histograma
columnas_histograma_permitidas = ['age', 'Years_of_Experience', 'Hours_Worked_Per_Week']

# Columnas para gráficos
columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
columnas_categoricas = df.select_dtypes(include=['object']).columns.tolist()

# Filtrar las columnas numéricas para que solo incluyan las permitidas
columnas_histograma_disponibles = [col for col in columnas_numericas if col in columnas_histograma_permitidas]

# --- Si seleccionamos gráfico de barras ---
if tipo_grafico == "Barras":
    columna_x_barras = st.selectbox("Selecciona la columna para el eje X (Categórica):", columnas_categoricas, key="barras_x")
    columna_y_barras = st.selectbox("Selecciona la columna para el eje Y (Numérica):", columnas_numericas, key="barras_y")
    
    if columna_x_barras and columna_y_barras:
        # Agrupar por la columna categórica y calcular el promedio para la columna numérica
        grouped_data = df.groupby(columna_x_barras)[columna_y_barras].mean().sort_values()
        st.write(grouped_data)
        
        # Crear gráfico de barras
        st.subheader(f"Gráfico de Barras: {columna_y_barras} por {columna_x_barras}")
        st.bar_chart(grouped_data, color=color_grafico)

# --- Si seleccionamos histograma ---
elif tipo_grafico == "Histograma":
    columna_histograma = st.selectbox("Selecciona la columna para el histograma:", columnas_histograma_disponibles, key="histograma")
    if columna_histograma:
        # Crear histograma
        st.subheader(f"Histograma de {columna_histograma}")
        plt.hist(df[columna_histograma].dropna(), bins=20, color=color_grafico)
        st.pyplot(plt)


# --- Nueva sección para los gráficos de Líneas y Dispersión ---
tipo_grafico_2 = st.radio("Selecciona el tipo de gráfico", ["Líneas", "Dispersión"], key="lineas_dispersion")

# Si seleccionamos gráfico de líneas
if tipo_grafico_2 == "Líneas":
    columna_x_lineas = st.selectbox("Selecciona la columna para el eje X (Numérica):", columnas_numericas, key="lineas_x")
    columna_y_lineas = st.selectbox("Selecciona la columna para el eje Y (Numérica):", columnas_numericas, key="lineas_y")
    
    if columna_x_lineas and columna_y_lineas:
        # Crear gráfico de líneas
        st.subheader(f"Gráfico de Líneas: {columna_y_lineas} vs {columna_x_lineas}")
        plt.plot(df[columna_x_lineas], df[columna_y_lineas], color=color_grafico)
        plt.xlabel(columna_x_lineas)
        plt.ylabel(columna_y_lineas)
        st.pyplot(plt)

# Si seleccionamos gráfico de dispersión
elif tipo_grafico_2 == "Dispersión":
    columna_x_dispersion = st.selectbox("Selecciona la columna para el eje X (Numérica):", columnas_numericas, key="dispersion_x")
    columna_y_dispersion = st.selectbox("Selecciona la columna para el eje Y (Numérica):", columnas_numericas, key="dispersion_y")
    
    if columna_x_dispersion and columna_y_dispersion:
        # Crear gráfico de dispersión
        st.subheader(f"Gráfico de Dispersión: {columna_y_dispersion} vs {columna_x_dispersion}")
        plt.scatter(df[columna_x_dispersion], df[columna_y_dispersion], color=color_grafico)
        plt.xlabel(columna_x_dispersion)
        plt.ylabel(columna_y_dispersion)
        st.pyplot(plt)

# --- Bloques de selección para más información ---
# Bloque 1 de selección para más información
st.subheader("Más información sobre el gráfico seleccionado")
informacion_1 = st.selectbox("Selecciona un tema para ver más información", ["Impacto del trabajo remoto", "Factores que afectan el estrés"], key="informacion_1")
if informacion_1 == "Impacto del trabajo remoto":
    st.write("El trabajo remoto tiene una gran influencia en la salud mental de los empleados. Puede aumentar el estrés debido a la falta de interacción social, la sobrecarga de trabajo, o la falta de control sobre el entorno.")
elif informacion_1 == "Factores que afectan el estrés":
    st.write("El estrés puede ser causado por varios factores, como la presión laboral, las responsabilidades familiares, el entorno de trabajo, y los problemas personales. La gestión del tiempo y las técnicas de relajación pueden ayudar a reducir el estrés.")

# Bloque 2 de selección para más información
st.subheader("Más detalles sobre el estudio")
informacion_2 = st.selectbox("Selecciona un tema para obtener más detalles", ["Metodología del estudio", "Datos demográficos de los participantes"], key="informacion_2")
if informacion_2 == "Metodología del estudio":
    st.write("El estudio se basó en encuestas realizadas a trabajadores de diferentes sectores. Se recopilaron datos sobre su bienestar mental, estrés y satisfacción laboral.")
elif informacion_2 == "Datos demográficos de los participantes":
    st.write("Los participantes fueron trabajadores de diversas edades, géneros y niveles de experiencia. La mayoría trabajaba en sectores como tecnología, educación y atención al cliente.")




