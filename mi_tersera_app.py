import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Ruta del archivo CSV
csv_file = 'finanzas.csv'

# Función para almacenar los datos
def guardar_datos(ingresos, gastos, presupuesto, fecha):
    data = {
        'fecha': fecha,
        'ingresos': ingresos,
        'gastos': gastos,
        'presupuesto': presupuesto
    }
    
    # Verificar si el archivo CSV existe, si no, crear uno nuevo
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(columns=['fecha', 'ingresos', 'gastos', 'presupuesto'])
    
    # Agregar la nueva entrada
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv(csv_file, index=False)
    
    return df

# Función para calcular las diferencias
def calcular_diferencias(df):
    df['diferencia'] = df['presupuesto'] - (df['ingresos'] - df['gastos'])
    return df

# Función para inferir el presupuesto
def inferir_presupuesto(ingresos, gastos):
    # Podemos usar un porcentaje de los ingresos para inferir el presupuesto
    porcentaje_presupuesto = 0.7  # 70% de los ingresos
    presupuesto_inferido = (ingresos * porcentaje_presupuesto) - gastos
    return presupuesto_inferido

# Título de la app
st.title("Registro de Finanzas Personales")

# Mostrar nombre del creador
st.write("Creador: Lehvui Gonzalez Cardona")

# Entrada de datos
st.header("Ingresar Datos Financieros")

# Ingreso de valores
ingresos = st.number_input("Ingresos", min_value=0.0, step=0.01)
gastos = st.number_input("Gastos", min_value=0.0, step=0.01)
presupuesto = st.number_input("Presupuesto (deja vacío para inferir)", min_value=0.0, step=0.01, format="%.2f")

# Seleccionar fecha o usar la actual
fecha_seleccionada = st.date_input("Seleccionar fecha", value=datetime.today().date())

# Si no se ingresa un presupuesto, inferirlo
if presupuesto == 0:
    presupuesto = inferir_presupuesto(ingresos, gastos)

# Mostrar los valores actuales del presupuesto, ingresos y gastos
st.write(f"**Presupuesto Actual:** {presupuesto}")
st.write(f"**Ingresos Actuales:** {ingresos}")
st.write(f"**Gastos Actuales:** {gastos}")

# Botón para guardar los datos
if st.button("Guardar Datos"):
    df = guardar_datos(ingresos, gastos, presupuesto, fecha_seleccionada)
    st.write("Datos guardados correctamente")
    st.write(df)

# Mostrar el reporte de diferencias
st.header("Reporte de Diferencias")

# Cargar los datos históricos desde el archivo CSV
if os.path.exists(csv_file):
    df_existing = pd.read_csv(csv_file)
    df_report = calcular_diferencias(df_existing)
    st.write("Reporte de las diferencias entre lo presupuestado y lo real:")
    st.write(df_report)
else:
    st.write("No hay datos disponibles para mostrar.")
