import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
file_path = "Impact_of_Remote_Work_on_Mental_Health.csv"
df = pd.read_csv(file_path)

# Identificar columnas numéricas y categóricas
numericas = df.select_dtypes(include=[np.number]).columns.tolist()
categoricas = df.select_dtypes(include=["object", "category"]).columns.tolist()

# Opciones de gráficos
st.title("Visualización de Datos")
tipo_grafico = st.sidebar.selectbox("Selecciona el tipo de gráfico", ["Scatter", "Line", "Bar", "Barh", "Histograma"])

# Selección de ejes
x_col = st.sidebar.selectbox("Eje X (numérico)", numericas)
if tipo_grafico in ["Scatter", "Line", "Bar", "Barh"]:
    y_col = st.sidebar.selectbox("Eje Y", numericas + categoricas)
else:
    y_col = None

# Generación de gráficos
plt.figure(figsize=(10, 5))
if tipo_grafico == "Scatter":
    plt.scatter(df[x_col], df[y_col], alpha=0.7)
    plt.title("Gráfico de Dispersión")
elif tipo_grafico == "Line":
    plt.plot(df[x_col], df[y_col], marker='o')
    plt.title("Gráfico de Línea")
elif tipo_grafico == "Bar":
    plt.bar(df[y_col], df[x_col])
    plt.title("Gráfico de Barras")
elif tipo_grafico == "Barh":
    plt.barh(df[y_col], df[x_col])
    plt.title("Gráfico de Barras Horizontales")
elif tipo_grafico == "Histograma":
    plt.hist(df[x_col], bins=10, color='gray', edgecolor='black')
    plt.title("Histograma")

plt.xlabel(x_col)
if y_col:
    plt.ylabel(y_col)
st.pyplot(plt)
