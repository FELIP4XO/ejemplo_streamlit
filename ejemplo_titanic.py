import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components

# Cargar el DataFrame
df = pd.read_csv("csvsinnan.csv")

# Título principal
st.title("Salud mental en trabajo remoto")

# Estilo personalizado
st.markdown("""
<style>
    [data-testid=stSidebar] {background-color: #10609d;}
</style>
""", unsafe_allow_html=True)

# Barra lateral
with st.sidebar:
    st.markdown("<h1 style='color: white'>Opciones de color</h1>", unsafe_allow_html=True)
    st.title('Reproductor Musical desde YouTube')
    playlist_url = "https://www.youtube.com/playlist?list=PLHLua7lnY9X-uAKqwp0T23h3A4d-ZajTO"
    playlist_id = playlist_url.split('list=')[-1]
    components.iframe(f"https://www.youtube.com/embed/videoseries?list={playlist_id}", width=300, height=200)
    color_grafico = st.color_picker('Selecciona un color para el gráfico', '#007bff')

# Configuración de columnas compatibles para gráficos
columnas_para_histograma = ["Age", "Years_of_Experience", "Stress_Level", "Productivity_Change"]
columnas_para_barras = {
    "x": ["Gender", "Job_Role", "Work_Location", "Mental_Health_Condition"],
    "y": ["Age", "Years_of_Experience", "Stress_Level", "Productivity_Change"]
}

# Selector de tipo de gráfico
st.sidebar.markdown("## Configuración de gráficos")
tipo_grafico = st.sidebar.radio("Selecciona el tipo de gráfico:", ["Barras", "Histograma"])

# Configuración según el gráfico seleccionado
if tipo_grafico == "Barras":
    st.sidebar.markdown("### Configuración de gráfico de barras")
    columna_x_barras = st.sidebar.selectbox("Selecciona la columna para el eje X (categórica):", columnas_para_barras["x"])
    columna_y_barras = st.sidebar.selectbox("Selecciona la columna para el eje Y (numérica):", columnas_para_barras["y"])
elif tipo_grafico == "Histograma":
    st.sidebar.markdown("### Configuración de histograma")
    columna_y_histograma = st.sidebar.selectbox("Selecciona la columna para el eje Y (numérica):", columnas_para_histograma)

# Generación del gráfico
if tipo_grafico == "Barras":
    st.subheader(f"Gráfico de barras: {columna_x_barras} vs {columna_y_barras}")
    grouped_data = df.groupby(columna_x_barras)[columna_y_barras].mean().sort_values()
    plt.figure(figsize=(8, 6))
    plt.bar(grouped_data.index, grouped_data.values, color=color_grafico)
    plt.title(f"{columna_y_barras} promedio por {columna_x_barras}", fontsize=16)
    plt.xlabel(columna_x_barras)
    plt.ylabel(f"Promedio de {columna_y_barras}")
    st.pyplot(plt)

elif tipo_grafico == "Histograma":
    st.subheader(f"Histograma: {columna_y_histograma}")
    plt.figure(figsize=(8, 6))
    plt.hist(df[columna_y_histograma].dropna(), bins=20, color=color_grafico, alpha=0.7)
    plt.title(f"Distribución de {columna_y_histograma}", fontsize=16)
    plt.xlabel(columna_y_histograma)
    plt.ylabel("Frecuencia")
    st.pyplot(plt) 
