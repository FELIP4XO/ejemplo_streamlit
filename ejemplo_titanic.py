import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

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
    boton1 = st.button("¿Cuál es la relación entre el nivel de estrés y el modo de trabajo?")
    if boton1:
        st.write("alo")
    casil1 = st.checkbox("Hola")
    if casil1:
        st.write("Casilla presionada")
        casil2 = st.checkbox("subcasilla")
        if casil2:
            casil3 = st.checkbox("Otras más")

# Selección de tipo de gráfico
tipo_grafico = st.radio("Selecciona el tipo de gráfico", ["Barras", "Histograma", "Líneas", "Dispersión"])

# Columnas para gráficos
columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
columnas_categoricas = df.select_dtypes(include=['object']).columns.tolist()

# Si seleccionamos gráfico de barras
if tipo_grafico == "Barras":
    columna_x_barras = st.selectbox("Selecciona la columna para el eje X (Categórica):", columnas_categoricas)
    columna_y_barras = st.selectbox("Selecciona la columna para el eje Y (Numérica):", columnas_numericas)
    
    if columna_x_barras and columna_y_barras:
        # Agrupar por la columna categórica y calcular el promedio para la columna numérica
        grouped_data = df.groupby(columna_x_barras)[columna_y_barras].mean().sort_values()
        st.write(grouped_data)
        
        # Crear gráfico de barras
        st.subheader(f"Gráfico de Barras: {columna_y_barras} por {columna_x_barras}")
        st.bar_chart(grouped_data, color=color_grafico)

# Si seleccionamos histograma
elif tipo_grafico == "Histograma":
    columna_histograma = st.selectbox("Selecciona la columna para el histograma:", columnas_numericas)
    if columna_histograma:
        # Crear histograma
        st.subheader(f"Histograma de {columna_histograma}")
        plt.hist(df[columna_histograma].dropna(), bins=20, color=color_grafico)
        st.pyplot(plt)

# Si seleccionamos gráfico de líneas
elif tipo_grafico == "Líneas":
    columna_x_lineas = st.selectbox("Selecciona la columna para el eje X (Numérica):", columnas_numericas)
    columna_y_lineas = st.selectbox("Selecciona la columna para el eje Y (Numérica):", columnas_numericas)
    
    if columna_x_lineas and columna_y_lineas:
        # Crear gráfico de líneas
        st.subheader(f"Gráfico de Líneas: {columna_y_lineas} vs {columna_x_lineas}")
        plt.plot(df[columna_x_lineas], df[columna_y_lineas], color=color_grafico)
        plt.xlabel(columna_x_lineas)
        plt.ylabel(columna_y_lineas)
        st.pyplot(plt)

# Si seleccionamos gráfico de dispersión
elif tipo_grafico == "Dispersión":
    columna_x_dispersion = st.selectbox("Selecciona la columna para el eje X (Numérica):", columnas_numericas)
    columna_y_dispersion = st.selectbox("Selecciona la columna para el eje Y (Numérica):", columnas_numericas)
    
    if columna_x_dispersion and columna_y_dispersion:
        # Crear gráfico de dispersión
        st.subheader(f"Gráfico de Dispersión: {columna_y_dispersion} vs {columna_x_dispersion}")
        plt.scatter(df[columna_x_dispersion], df[columna_y_dispersion], color=color_grafico)
        plt.xlabel(columna_x_dispersion)
        plt.ylabel(columna_y_dispersion)
        st.pyplot(plt)
