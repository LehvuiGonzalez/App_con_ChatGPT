import streamlit as st
import pandas as pd
import requests

# Título de la app
st.title("Análisis de Datos desde una API con Pandas")

# URL de la API (usaremos una API pública que devuelve datos en formato JSON)
url = 'https://jsonplaceholder.typicode.com/posts'

# Realizar la solicitud a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Convertir el JSON en un DataFrame de Pandas
    data = response.json()
    df = pd.DataFrame(data)
    
    # Mostrar las primeras filas del DataFrame
    st.subheader("Vista previa de los datos")
    st.write(df.head())  # Mostrar las primeras 5 filas del JSON convertido a DataFrame
    
    # Estadísticas básicas del DataFrame
    st.subheader("Estadísticas descriptivas")
    st.write(df.describe())  # Estadísticas como media, desviación estándar, etc.
    
    # Verificar si hay valores nulos
    st.subheader("Valores nulos")
    st.write(df.isnull().sum())  # Mostrar la cantidad de valores nulos por columna
    
    # Permitir que el usuario seleccione una columna
    st.subheader("Explorar una columna")
    column = st.selectbox("Selecciona una columna para visualizar:", df.columns)
    
    # Mostrar los datos de la columna seleccionada
    if column:
        st.write(f"Contenido de la columna {column}:")
        st.write(df[column])  # Mostrar la columna seleccionada
    
    # Mostrar el número de filas y columnas
    st.write(f"El conjunto de datos contiene {df.shape[0]} filas y {df.shape[1]} columnas.")
    
else:
    st.error(f"Error al obtener los datos de la API. Código de estado: {response.status_code}")
