import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
file_path = "Impact_of_Remote_Work_on_Mental_Health.csv"  # Asegúrate de que esté en la misma carpeta
df = pd.read_csv(file_path)

# Función para obtener columnas compatibles según el tipo de gráfico
def obtener_columnas_compatibles(tipo_grafico):
    if tipo_grafico in ["Scatter", "Line", "Bar", "Barh", "Histograma", "Boxplot", "Heatmap"]:
        return df.select_dtypes(include=[np.number]).columns.tolist()
    elif tipo_grafico == "Pie":
        return df.select_dtypes(include=["object", "category"]).columns.tolist()
    elif tipo_grafico == "Dispersión por Categoría":
        return df.columns.tolist()
    return []

# Configuración inicial de la aplicación
st.title("Visualización de Datos Interactiva")
st.sidebar.header("Opciones de Gráfico")

# Selección del tipo de gráfico
tipo_grafico = st.sidebar.selectbox(
    "Selecciona el tipo de gráfico",
    ["Scatter", "Line", "Bar", "Barh", "Pie", "Histograma", "Boxplot", "Heatmap", "Dispersión por Categoría"]
)

# Filtrar columnas compatibles
columnas_x = obtener_columnas_compatibles(tipo_grafico)
columnas_y = columnas_x if tipo_grafico not in ["Pie", "Histograma"] else ["N/A"]

# Widgets de selección de columnas
x_col = st.sidebar.selectbox("Selecciona el eje X", columnas_x)
y_col = st.sidebar.selectbox("Selecciona el eje Y", columnas_y) if columnas_y != ["N/A"] else "N/A"

# Generación de gráficos
st.header("Gráfico Generado")
plt.figure(figsize=(10, 6))

if x_col not in df.columns or (y_col not in df.columns and y_col != "N/A"):
    st.error("Selección de columnas no válida para el tipo de gráfico seleccionado.")
else:
    if tipo_grafico == "Scatter":
        plt.scatter(df[x_col], df[y_col], c='blue', alpha=0.7)
        plt.title("Gráfico de Dispersión")
    elif tipo_grafico == "Line":
        plt.plot(df[x_col], df[y_col], marker='o', color='green')
        plt.title("Gráfico de Línea")
    elif tipo_grafico == "Bar":
        plt.bar(df[x_col], df[y_col], color='orange')
        plt.title("Gráfico de Barras")
    elif tipo_grafico == "Barh":
        plt.barh(df[x_col], df[y_col], color='purple')
        plt.title("Gráfico de Barras Horizontales")
    elif tipo_grafico == "Pie":
        valores = df[x_col].value_counts()
        plt.pie(valores, labels=valores.index, autopct='%1.1f%%')
        plt.title("Gráfico de Torta")
    elif tipo_grafico == "Histograma":
        plt.hist(df[x_col], bins=10, color='gray', edgecolor='black')
        plt.title("Histograma")
    elif tipo_grafico == "Boxplot":
        plt.boxplot(df[x_col].dropna())
        plt.title("Gráfico de Cajas")
    elif tipo_grafico == "Heatmap":
        corr = df.select_dtypes(include=[np.number]).corr()
        plt.imshow(corr, cmap='coolwarm', interpolation='none')
        plt.colorbar()
        plt.title("Mapa de Calor")
    elif tipo_grafico == "Dispersión por Categoría":
        categorias = df[x_col].unique()
        for cat in categorias:
            subset = df[df[x_col] == cat]
            plt.scatter(subset.index, subset[y_col], label=str(cat), alpha=0.6)
        plt.legend()
        plt.title("Dispersión por Categoría")

    plt.xlabel(x_col)
    plt.ylabel(y_col if y_col != "N/A" else "")
    plt.grid(True)
    st.pyplot(plt)
