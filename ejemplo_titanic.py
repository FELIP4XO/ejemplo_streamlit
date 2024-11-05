import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

datos_sismicos = pd.read_csv("seismic_data.csv") 

st.title("Visualización de Datos Sísmicos")
st.write("Esta aplicación te permite explorar datos sísmicos de un archivo CSV.")

fig, ax = plt.subplots()
ax.scatter(datos_sismicos["Depth"], datos_sismicos["Magnitude"]) 
ax.set_xlabel("Magnitud")  
ax.set_ylabel("Profundidad")
ax.set_title("Profundidad vs Magnitud")

st.pyplot(fig)

if st.checkbox("Mostrar Tabla de Datos"):
    st.dataframe(datos_sismicos)
