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

columnas_numericas = datos_sismicos.select_dtypes(include=['number']).columns

for columna in comnas_numericas:
    if st.button(f'Grafico de barra de {columna}'):
        fig, ax = plt.subplots()
        ax.bar(datos_sismicos.index, datos_sismicos[columna])
        ax.set_xlabel('Índice')
        ax.set_ylabel(columna)
        ax.set_title(f'grafico de barras de {columna}')
        st.pyplot(fig)

if st.checkbox("Mostrar Tabla de Datos"):
    st.dataframe(datos_sismicos)
