import streamlit as st
import pandas as pd
from datetime import datetime

# Función para almacenar los datos
def guardar_datos(ingresos, gastos, presupuesto, fecha):
    data = {
        'fecha': fecha,
        'ingresos': ingresos,
        'gastos': gastos,
        'presupuesto': presupuesto
    }
    
    # Cargar el archivo CSV si existe, si no, crear uno nuevo
    try:
        df = pd.read_csv('finanzas.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['fecha', 'ingresos', 'gastos', 'presupuesto'])
    
    # Agregar la nueva entrada
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv('finanzas.csv', index=False)
    
    return df

# Función para calcular las diferencias
def calcular_diferencias(df):
    df['diferencia'] = df['presupuesto'] - (df['ingresos'] - df['gastos'])
    return df

# Título de la app
st.title("Registro de Finanzas Personales")

# Entrada de datos
st.header("Ingresar Datos Financieros")

ingresos = st.number_input("Ingresos", min_value=0.0, step=0.01)
gastos = st.number_input("Gastos", min_value=0.0, step=0.01)
presupuesto = st.number_input("Presupuesto", min_value=0.0, step=0.01)

# Seleccionar fecha o usar la actual
fecha_seleccionada = st.date_input("Seleccionar fecha", value=datetime.today().date())

# Botón para guardar los datos
if st.button("Guardar Datos"):
    df = guardar_datos(ingresos, gastos, presupuesto, fecha_seleccionada)
    st.write("Datos guardados correctamente")
    st.write(df)

# Mostrar el reporte de diferencias
st.header("Reporte de Diferencias")

# Cargar los datos históricos desde el archivo CSV
try:
    df_existing = pd.read_csv('finanzas.csv')
    df_report = calcular_diferencias(df_existing)
    st.write("Reporte de las diferencias entre lo presupuestado y lo real:")
    st.write(df_report)
except FileNotFoundError:
    st.write("No hay datos disponibles para mostrar.")
