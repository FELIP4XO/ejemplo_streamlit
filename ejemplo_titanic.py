import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
file_path = "Impact_of_Remote_Work_on_Mental_Health.csv"  # Asegúrate de que el archivo esté en la misma carpeta
df = pd.read_csv(file_path)

# Identificar columnas numéricas y categóricas
columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
columnas_categoricas = df.select_dtypes(include=["object", "category"]).columns.tolist()

# Configuración inicial
st.title("Visualización de Datos Interactiva con Compatibilidad Dinámica")
st.sidebar.header("Opciones de Gráfico")

# Selección de tipo de gráfico
tipo_grafico = st.sidebar.selectbox(
    "Selecciona el tipo de gráfico",
    ["Scatter", "Line", "Bar", "Barh", "Pie", "Histograma", "Boxplot"]
)

# Filtrar columnas compatibles
if tipo_grafico in ["Scatter", "Line", "Bar", "Barh"]:
    x_columnas = columnas_numericas  # Eje X solo numérico
    y_columnas = columnas_numericas + columnas_categoricas  # Eje Y puede ser numérico o categórico
elif tipo_grafico == "Pie":
    x_columnas = columnas_numericas  # Eje X numérico para los valores
    y_columnas = columnas_categoricas  # Eje Y categórico para las etiquetas
elif tipo_grafico == "Histograma":
    x_columnas = columnas_numericas  # Solo eje X numérico
    y_columnas = ["N/A"]  # No requiere eje Y
elif tipo_grafico == "Boxplot":
    x_columnas = columnas_numericas  # Numérico para la distribución
    y_columnas = columnas_categoricas  # Categórico para agrupar

# Widgets de selección
x_col = st.sidebar.selectbox("Selecciona el eje X", x_columnas)
y_col = st.sidebar.selectbox("Selecciona el eje Y", y_columnas) if y_columnas != ["N/A"] else "N/A"

# Generación del gráfico
st.header("Gráfico Generado")
plt.figure(figsize=(10, 6))

if tipo_grafico == "Scatter":
    plt.scatter(df[x_col], df[y_col], alpha=0.7, c='blue')
    plt.title("Gráfico de Dispersión")
elif tipo_grafico == "Line":
    plt.plot(df[x_col], df[y_col], marker='o', color='green')
    plt.title("Gráfico de Línea")
elif tipo_grafico == "Bar":
    plt.bar(df[y_col], df[x_col], color='orange')  # Cambiando el orden de X y Y
    plt.title("Gráfico de Barras")
elif tipo_grafico == "Barh":
    plt.barh(df[y_col], df[x_col], color='purple')  # Cambiando el orden de X y Y
    plt.title("Gráfico de Barras Horizontales")
elif tipo_grafico == "Pie":
    valores = df.groupby(y_col)[x_col].sum()  # Sumar valores por categoría
    plt.pie(valores, labels=valores.index, autopct='%1.1f%%')
    plt.title("Gráfico de Torta")
elif tipo_grafico == "Histograma":
    plt.hist(df[x_col], bins=10, color='gray', edgecolor='black')
    plt.title("Histograma")
elif tipo_grafico == "Boxplot":
    df.boxplot(column=x_col, by=y_col, grid=False)  # Cambiando el orden de X y Y
    plt.title("Gráfico de Cajas")
    plt.suptitle("")

plt.xlabel(x_col)
if y_col != "N/A":
    plt.ylabel(y_col)
plt.grid(True)
st.pyplot(plt)
