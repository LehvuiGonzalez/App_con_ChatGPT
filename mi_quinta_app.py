import streamlit as st
import folium
from streamlit_folium import st_folium

# Título de la aplicación
st.title("Mapa Interactivo de Coordenadas")

# Ingreso de coordenadas
st.header("Ingresa las coordenadas (Latitud y Longitud)")

latitude = st.number_input("Latitud", min_value=-90.0, max_value=90.0, value=20.0)
longitude = st.number_input("Longitud", min_value=-180.0, max_value=180.0, value=-90.0)

# Crear un mapa en Folium centrado en las coordenadas iniciales
map_center = [latitude, longitude]
my_map = folium.Map(location=map_center, zoom_start=10)

# Añadir un marcador en las coordenadas proporcionadas por el usuario
folium.Marker([latitude, longitude], popup=f'Coordenadas: {latitude}, {longitude}').add_to(my_map)

# Mostrar el mapa interactivo en Streamlit
st_folium(my_map, width=700, height=500)

# Mostrar las coordenadas ingresadas por el usuario
st.write(f"Has ingresado las coordenadas: Latitud {latitude}, Longitud {longitude}")
