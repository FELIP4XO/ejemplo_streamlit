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
    x_columnas = columnas_numericas + columnas_categoricas  # Eje X puede ser numérico o categórico
    y_columnas = columnas_numericas  # Eje Y solo numérico
elif tipo_grafico == "Pie":
    x_columnas = columnas_categoricas  # Eje X categórico para las etiquetas
    y_columnas = columnas_numericas  # Eje Y numérico para los valores
elif tipo_grafico == "Histograma":
    x_columnas = columnas_numericas  # Solo eje X numérico
    y_columnas = ["N/A"]  # No requiere eje Y
elif tipo_grafico == "Boxplot":
    x_columnas = columnas_categoricas  # Categórico para agrupar
    y_columnas = columnas_numericas  # Numérico para la distribución

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
    plt.bar(df[x_col], df[y_col], color='orange')
    plt.title("Gráfico de Barras")
elif tipo_grafico == "Barh":
    plt.barh(df[x_col], df[y_col], color='purple')
    plt.title("Gráfico de Barras Horizontales")
elif tipo_grafico == "Pie":
    valores = df.groupby(x_col)[y_col].sum()  # Sumar valores por categoría
    plt.pie(valores, labels=valores.index, autopct='%1.1f%%')
    plt.title("Gráfico de Torta")
elif tipo_grafico == "Histograma":
    plt.hist(df[x_col], bins=10, color='gray', edgecolor='black')
    plt.title("Histograma")
elif tipo_grafico == "Boxplot":
    df.boxplot(column=y_col, by=x_col, grid=False)
    plt.title("Gráfico de Cajas")
    plt.suptitle("")

plt.xlabel(x_col)
if y_col != "N/A":
    plt.ylabel(y_col)
plt.grid(True)
st.pyplot(plt)
