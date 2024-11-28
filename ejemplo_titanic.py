import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components


df = pd.read_csv("csvsinnan.csv")
st.title("Salud mental en trabajo remoto")
st.markdown("""
<style>
    [data-testid=stSidebar] {background-color: #10609d;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h1 style='color: white'>Opciones de color</h1>", unsafe_allow_html=True)
    st.title('Reproductor Musical desde YouTube')
    
    playlist_url = "https://www.youtube.com/playlist?list=PLHLua7lnY9X-uAKqwp0T23h3A4d-ZajTO"
    playlist_id = playlist_url.split('list=')[-1]
    components.iframe(f"https://www.youtube.com/embed/videoseries?list={playlist_id}", width=300, height=200) 
    
    color_grafico = st.color_picker('Selecciona un color para el grafico','#007bff')    
    
    boton1 = st.button("¿Cual es la relacion de nivel de  estres y modo de trabajo?")
    if boton1:
        st.write("alo")
    casil1= st.checkbox("Hola")
    if casil1:
        st.write("Casilla presionada")
        casil2 = st.checkbox("subcasilla")
        if casil2:
            casil3 = st.checkbox("Otramas")

tipo_grafico = st.radio("Selecciona el tipo de gráfico", ["Barras", "Histograma"])

# Lista de columnas específicas permitidas para el histograma
columnas_histograma_permitidas = ['Age', 'Years_of_Experience', 'Hours_Worked_Per_Week']

# Lista de columnas numéricas que podrían ser usadas para el eje Y
columnas_numericas = ["Age", "Years_of_Experience", "Hours_Worked_Per_Week", "Number_of_Virtual_Meetings", 
                      "Work_Life_Balance_Rating", "Stress_Level", "Productivity_Change", 
                      "Social_Isolation_Rating", "Satisfaction_with_Remote_Work"]

# Lista de columnas categóricas que podrían ser usadas para el eje X
columnas_categoricas = ["Gender", "Job_Role", "Work_Location", "Mental_Health_Condition", 
                        "Access_to_Mental_Health_Resources", "Company_Support_for_Remote_Work", 
                        "Physical_Activity", "Sleep_Quality"]

columnas_histograma_disponibles = [col for col in columnas_numericas if col in columnas_histograma_permitidas]
# --- Si seleccionamos gráfico de barras ---
if tipo_grafico == "Barras":
    columna_x = st.selectbox("Selecciona la columna para el eje X:", columnas_categoricas)
    columna_y = st.selectbox("Selecciona la columna para el eje Y:", columnas_numericas)
    
    if columna_x and columna_y:
       st.bar_chart(df, x=columna_x, y=columna_y, color=color_grafico)

elif tipo_grafico == "Histograma":
    columna_histograma = st.selectbox("Selecciona la columna para el histograma:", columnas_histograma_disponibles, key="histograma")
    if columna_histograma:
        # Crear histograma
        st.subheader(f"Histograma de {columna_histograma}")
        plt.hist(df[columna_histograma].dropna(), bins=20, color=color_grafico)
        st.pyplot(plt)



columna_trastorno = ["Depresión","Ansiedad","Burnout"]
opciontras = st.selectbox("Selecciona uno de estos trastornos para saber mas de ellos",columna_trastorno)



st.title("Gráficos de Pastel")
tipo_grafico_pastel = st.radio("Selecciona el gráfico que deseas visualizar:", ["Porcentaje de empleados por región", "Porcentaje de empleados por género", "Distribución de roles laborales"])

# Generar gráfico de pastel
if tipo_grafico_pastel == "Porcentaje de empleados por región":
    st.subheader("Porcentaje de empleados por región")
    region_counts = df['Region'].value_counts()
    
    # Crear gráfico de pastel
    fig, ax = plt.subplots()
    ax.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Distribución por Región")
    st.pyplot(fig)

elif tipo_grafico_pastel == "Porcentaje de empleados por género":
    st.subheader("Porcentaje de empleados por género")
    gender_counts = df['Gender'].value_counts()
    
    # Crear gráfico de pastel
    fig, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Distribución por Género")
    st.pyplot(fig)

elif tipo_grafico_pastel == "Distribución de roles laborales":
    st.subheader("Distribución de roles laborales")
    role_counts = df['Job_Role'].value_counts()
    
    # Crear gráfico de pastel
    fig, ax = plt.subplots()
    ax.pie(role_counts, labels=role_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Distribución de Roles Laborales")
    st.pyplot(fig)




# graficos de barras apiladas 



# Mostrar los botones para elegir colores
st.sidebar.header('Selecciona los colores para los Niveles de Estrés')

color_grafico_1 = st.sidebar.color_picker('Nivel de Estrés 1 (Bajo)', '#007bff')
color_grafico_2 = st.sidebar.color_picker('Nivel de Estrés 2 (Moderado)', '#28a745')
color_grafico_3 = st.sidebar.color_picker('Nivel de Estrés 3 (Alto)', '#dc3545')

# Crear una lista de colores basada en los 3 colores seleccionados
colors = [color_grafico_1, color_grafico_2, color_grafico_3]

# Crear el gráfico de barras apiladas
fig, ax = plt.subplots(figsize=(10, 6))

# Crear el gráfico de barras apiladas sin agrupamiento (asumiendo que ya están los datos de la columna `Stress_Level`)
df_pivot = df.pivot_table(index='Work_Location', columns='Stress_Level', aggfunc='size', fill_value=0)

# Crear gráfico de barras apiladas
df_pivot.plot(kind='bar', stacked=True, ax=ax, color=colors)

# Etiquetas y título del gráfico
ax.set_title("Distribución de Niveles de Estrés según Ubicación Laboral", fontsize=16)
ax.set_xlabel("Ubicación Laboral", fontsize=12)
ax.set_ylabel("Número de Empleados", fontsize=12)
ax.legend(title="Nivel de Estrés", title_fontsize='13', fontsize='11')

# Mostrar el gráfico
st.pyplot(fig)


# final del codigo de graficos 


st.markdown("Al ver los datos de estrés según dónde trabajamos (oficina, casa o una mezcla), vemos que la situación es más complicada de lo que parece. Aunque trabajar desde casa puede ser más tranquilo para algunos, otros se sienten solos o les cuesta desconectar. En la oficina, las presiones del día a día y las relaciones con los compañeros también generan estrés. El modelo híbrido, que combina ambas opciones, podría ser una buena solución para muchos, pero hay que analizar caso por caso para saber qué funciona mejor para cada persona.")






# Columnas seleccionables
columns_to_use = [
    "Age",
    "Years_of_Experience",
    "Hours_Worked_Per_Week",
    "Number_of_Virtual_Meetings",
    "Work_Life_Balance_Rating",
    "Social_Isolation_Rating",
    "Company_Support_for_Remote_Work",
]

st.title("Gráfico de Dispersión Interactivo")

# Controles del usuario
x_axis = st.selectbox("Selecciona la columna para el eje X:", columns_to_use, index=0)
y_axis = st.selectbox("Selecciona la columna para el eje Y:", columns_to_use, index=1)
size = st.selectbox("Selecciona la columna para el tamaño de los círculos:", columns_to_use, index=2)
color = st.selectbox("Selecciona la columna para el color:", columns_to_use, index=3)

st.write("### Configuración seleccionada:")
st.write(f"**Eje X:** {x_axis}, **Eje Y:** {y_axis}, **Tamaño:** {size}, **Color:** {color}")

# Crear gráfico con Matplotlib
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    df[x_axis],
    df[y_axis],
    s=df[size] * 10,  # Multiplicamos por 10 para hacer los círculos más visibles
    c=df[color],
    cmap='viridis',  # Puedes cambiar la paleta de colores
    alpha=0.6,
    edgecolor='k'
)

# Etiquetas y título
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.title(f'Gráfico de Dispersión: {x_axis} vs {y_axis}')

# Barra de color
plt.colorbar(scatter, label=color)

# Mostrar gráfico en Streamlit
st.pyplot(plt)














st.subheader("Más información sobre el gráfico seleccionado")
informacion_1 = st.selectbox("Selecciona un tema para ver más información", ["Impacto del trabajo remoto", "Factores que afectan el estrés"], key="informacion_1")
if informacion_1 == "Impacto del trabajo remoto":
    st.write("El trabajo remoto tiene una gran influencia en la salud mental de los empleados. Puede aumentar el estrés debido a la falta de interacción social, la sobrecarga de trabajo, o la falta de control sobre el entorno.")
elif informacion_1 == "Factores que afectan el estrés":
    st.write("El estrés puede ser causado por varios factores, como la presión laboral, las responsabilidades familiares, el entorno de trabajo, y los problemas personales. La gestión del tiempo y las técnicas de relajación pueden ayudar a reducir el estrés.")

st.subheader("Más detalles sobre el estudio")
informacion_2 = st.selectbox("Selecciona un tema para obtener más detalles", ["Metodología del estudio", "Datos demográficos de los participantes"], key="informacion_2")
if informacion_2 == "Metodología del estudio":
    st.write("El estudio se basó en encuestas realizadas a trabajadores de diferentes sectores. Se recopilaron datos sobre su bienestar mental, estrés y satisfacción laboral.")
elif informacion_2 == "Datos demográficos de los participantes":
    st.write("Los participantes fueron trabajadores de diversas edades, géneros y niveles de experiencia. La mayoría trabajaba en sectores como tecnología, educación y atención al cliente.")
