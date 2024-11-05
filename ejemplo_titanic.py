import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

datos_sismicos = pd.read_csv('seismic_data.csv')

st.title('Visualización de Datos Sísmicos')
st.write('Esta aplicación te permite explorar datos sísmicos de un archivo CSV.')

fig, ax = plt.subplots()
ax.scatter(datos_sismicos['Magnitude'], datos_sismicos['Depth'])
ax.set_xlabel('Magnitud')
ax.set_ylabel('Profundidad')
ax.set_title('Profundidad vs Magnitud')
st.pyplot(fig)

columnas_numericas = datos_sismicos.select_dtypes(include=['number']).columns[-2:]

with st.sidebar:
    st.header('opciones de color')
    color_grafico = st.color_picker('Selecciona un color para el grafico','#007bff')
    
for columna in columnas_numericas:
    if st.button(f'Grafico de barra de {columna}'):
        fig, ax = plt.subplots()
        ax.bar(datos_sismicos.index, datos_sismicos[columna], color = color_grafico)
        ax.set_xlabel('Índice')
        ax.set_ylabel(columna)
        ax.set_title(f'grafico de barras de {columna}')
        st.pyplot(fig)

if st.checkbox("Mostrar Tabla de Datos"):
    st.dataframe(datos_sismicos)
