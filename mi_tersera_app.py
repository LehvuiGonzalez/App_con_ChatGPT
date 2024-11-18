import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Ruta del archivo CSV
csv_file = 'finanzas.csv'

# Función para almacenar los datos
def guardar_datos(ingresos, gastos, presupuesto, fecha, meta_ahorro):
    data = {
        'fecha': fecha,
        'ingresos': ingresos,
        'gastos': gastos,
        'presupuesto': presupuesto,
        'meta_ahorro': meta_ahorro
    }
    
    # Verificar si el archivo CSV existe, si no, crear uno nuevo
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(columns=['fecha', 'ingresos', 'gastos', 'presupuesto', 'meta_ahorro'])
    
    # Agregar la nueva entrada
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv(csv_file, index=False)
    
    return df

# Función para calcular las diferencias
def inferir_presupuesto(ingresos, gastos):
    # Podemos usar un porcentaje de los ingresos para inferir el presupuesto
    porcentaje_presupuesto = 0.7  # 70% de los ingresos
    presupuesto_inferido = (ingresos * porcentaje_presupuesto) - gastos
    return presupuesto_inferido

# Título de la app
st.title("Registro de Finanzas Personales")

# Mostrar nombre del creador
st.write("Creador: Lehvui Gonzalez Cardona")

# Inicialización de las variables en session_state si no están definidas
if 'ingresos' not in st.session_state:
    st.session_state.ingresos = 0.0
    st.session_state.gastos = 0.0
    st.session_state.presupuesto = 0.0
    st.session_state.meta_ahorro = 0.0

# Entrada de datos
st.header("Ingresar Datos Financieros")

# Ingreso de valores
ingresos = st.number_input("Ingresos", min_value=0.0, step=0.01, value=st.session_state.ingresos)
gastos = st.number_input("Gastos", min_value=0.0, step=0.01, value=st.session_state.gastos)
presupuesto = st.number_input("Presupuesto (deja vacío para inferir)", min_value=0.0, step=0.01, format="%.2f", value=st.session_state.presupuesto)
meta_ahorro = st.number_input("Meta de Ahorro", min_value=0.0, step=0.01, value=st.session_state.meta_ahorro)

# Seleccionar fecha o usar la actual
fecha_seleccionada = st.date_input("Seleccionar fecha", value=datetime.today().date())

# Si no se ingresa un presupuesto, inferirlo y actualizarlo en session_state
if presupuesto == 0:
    presupuesto = inferir_presupuesto(ingresos, gastos)

# Actualizar el presupuesto y la meta de ahorro globalmente
st.session_state.presupuesto = presupuesto
st.session_state.meta_ahorro = meta_ahorro

# Mostrar los valores actuales del presupuesto, ingresos y gastos
st.write(f"**Presupuesto Actual:** {st.session_state.presupuesto}")
st.write(f"**Ingresos Actuales:** {ingresos}")
st.write(f"**Gastos Actuales:** {gastos}")
st.write(f"**Meta de Ahorro Actual:** {st.session_state.meta_ahorro}")

# Barra de progreso para la meta de ahorro
if st.session_state.meta_ahorro > 0:
    progreso = (ingresos - gastos) / st.session_state.meta_ahorro
    st.progress(min(progreso, 1.0))

# Botón para guardar los datos
if st.button("Guardar Datos"):
    df = guardar_datos(ingresos, gastos, st.session_state.presupuesto, fecha_seleccionada, st.session_state.meta_ahorro)
    st.write("Datos guardados correctamente")
    st.write(df)

# Botón para limpiar los datos
if st.button("Limpiar Datos"):
    # Limpiar los valores en session_state
    st.session_state.ingresos = 0.0
    st.session_state.gastos = 0.0
    st.session_state.presupuesto = 0.0
    st.session_state.meta_ahorro = 0.0
    
    # Reiniciar la aplicación
    st.experimental_rerun()

