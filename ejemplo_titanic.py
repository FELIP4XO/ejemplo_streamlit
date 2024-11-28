import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components

# Cargar el DataFrame
df = pd.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv")

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
    color_grafico = st.color_picker('Selecciona un color para el grafico', '#007bff')
    boton1 = st.button("¿Cual es la relación de nivel de estrés y modo de trabajo?")
    if boton1:
        st.write("alo")
    casil1 = st.checkbox("Hola")
    if casil1:
        st.write("Casilla presionada")
        casil2 = st.checkbox("subcasilla")
        if casil2:
            casil3 = st.checkbox("Otramas")

# Configuración de columnas compatibles para gráficos
columnas_para_barras_y_histogramas = {
    "categóricas": ["Gender", "Job_Role", "Work_Location", "Mental_Health_Condition"],
    "numéricas": ["Age", "Years_of_Experience", "Stress_Level", "Productivity_Change"]
}

# Selector de tipo de gráfico
st.sidebar.markdown("## Configuración de gráficos")
tipo_grafico = st.sidebar.radio("Selecciona el tipo de gráfico:", ["Barras", "Histograma"])

# Selector de columnas según el gráfico
if tipo_grafico == "Barras":
    columna_x = st.sidebar.selectbox("Selecciona una columna para el eje X (categórica):", 
                                     columnas_para_barras_y_histogramas["categóricas"])
elif tipo_grafico == "Histograma":
    columna_y = st.sidebar.selectbox("Selecciona una columna para el eje Y (numérica):", 
                                     columnas_para_barras_y_histogramas["numéricas"])

# Generación del gráfico
if tipo_grafico == "Barras":
    st.subheader(f"Gráfico de barras: {columna_x}")
    conteo = df[columna_x].value_counts()
    plt.figure(figsize=(8, 6))
    plt.bar(conteo.index, conteo.values, color=color_grafico)
    plt.title(f"Distribución de {columna_x}", fontsize=16)
    plt.xlabel(columna_x)
    plt.ylabel("Conteo")
    st.pyplot(plt)

elif tipo_grafico == "Histograma":
    st.subheader(f"Histograma: {columna_y}")
    plt.figure(figsize=(8, 6))
    plt.hist(df[columna_y].dropna(), bins=20, color=color_grafico, alpha=0.7)
    plt.title(f"Distribución de {columna_y}", fontsize=16)
    plt.xlabel(columna_y)
    plt.ylabel("Frecuencia")
    st.pyplot(plt)
