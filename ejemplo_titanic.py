import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

datos_sismicos = pd.read_csv("seismic_data.csv") 

st.title("Visualización de Datos Sísmicos")
st.write("Esta aplicación te permite explorar datos sísmicos de un archivo CSV.")

fig, ax = plt.subplots()
ax.scatter(datos_sismicos["Magnitude"], datos_sismicos["Depth"]) 
ax.set_xlabel("Magnitude")  
ax.set_ylabel("Depth")
ax.set_title("Depth vs. Magnitude")

st.pyplot(fig)

if st.checkbox("Mostrar Tabla de Datos"):
    st.dataframe(datos_sismicos)
