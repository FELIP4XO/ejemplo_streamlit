import pandas as pd
import streamlit as st
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
    color_grafico = st.color_picker('Selecciona un color para el gráfico', '#007bff')

# Columnas para gráficos
columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
columnas_categoricas = df.select_dtypes(include=['object']).columns.tolist()

# --- Botones para mostrar gráficos ---
boton_barras = st.button("Mostrar gráfico de barras")
boton_dispersión = st.button("Mostrar gráfico de dispersión")

# Mostrar gráfico de barras si el botón es presionado
if boton_barras:
    columna_x_barras = st.selectbox("Selecciona la columna para el eje X (Categórica):", columnas_categoricas)
    columna_y_barras = st.selectbox("Selecciona la columna para el eje Y (Numérica):", columnas_numericas)
    
    if columna_x_barras and columna_y_barras:
        # Agrupar por la columna categórica y calcular el promedio para la columna numérica
        grouped_data = df.groupby(columna_x_barras)[columna_y_barras].mean().sort_values()
        st.write(grouped_data)
        
        # Crear gráfico de barras
        st.bar_chart(grouped_data, color=color_grafico)

# Mostrar gráfico de dispersión si el botón es presionado
if boton_dispersión:
    columna_x_dispersion = st.selectbox("Selecciona la columna para el eje X (Numérica):", columnas_numericas, key="dispersion_x")
    columna_y_dispersion = st.selectbox("Selecciona la columna para el eje Y (Numérica):", columnas_numericas, key="dispersion_y")
    
    if columna_x_dispersion and columna_y_dispersion:
        # Verificar que ambas columnas sean numéricas
        if pd.api.types.is_numeric_dtype(df[columna_x_dispersion]) and pd.api.types.is_numeric_dtype(df[columna_y_dispersion]):
            # Crear gráfico de dispersión
            st.subheader(f"Gráfico de Dispersión: {columna_y_dispersion} vs {columna_x_dispersion}")
            plt.scatter(df[columna_x_dispersion], df[columna_y_dispersion], color=color_grafico)
            plt.xlabel(columna_x_dispersion)
            plt.ylabel(columna_y_dispersion)
            st.pyplot(plt)
        else:
            st.warning("Por favor, selecciona dos columnas numéricas para crear un gráfico de dispersión.")

