import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Ruta del archivo CSV para almacenar los datos
csv_file = 'ingresos.csv'

# Función para almacenar los datos
def guardar_datos(ingresos, fecha):
    data = {
        'fecha': fecha,
        'ingresos': ingresos
    }
    
    # Verificar si el archivo CSV existe, si no, crear uno nuevo
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(columns=['fecha', 'ingresos'])
    
    # Agregar la nueva entrada
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv(csv_file, index=False)
    
    return df

# Título de la app
st.title("Registro de Ingresos")

# Entrada de datos
st.header("Ingresar Ingresos y Fecha")

# Ingreso de valores
ingresos = st.number_input("Ingresos", min_value=0.0, step=0.01)
fecha_seleccionada = st.date_input("Seleccionar fecha", value=datetime.today().date())

# Botón para guardar los datos
if st.button("Guardar Datos"):
    if ingresos > 0:
        df = guardar_datos(ingresos, fecha_seleccionada)
        st.write("Datos guardados correctamente")
    else:
        st.write("Por favor ingresa un valor de ingresos mayor a 0")

# Mostrar la tabla de ingresos guardados
st.subheader("Ingresos Registrados")

# Mostrar la tabla si el archivo CSV existe
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    st.write(df)
else:
    st.write("Aún no hay datos registrados.")

    
    # Reiniciar la aplicación
    st.experimental_rerun()

