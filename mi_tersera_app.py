import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Ruta del archivo CSV para almacenar los datos
csv_file = 'registro_finanzas.csv'

# Función para almacenar los datos
def guardar_datos(tipo, monto, fecha):
    data = {
        'fecha': fecha,
        'tipo': tipo,
        'monto': monto
    }
    
    # Verificar si el archivo CSV existe, si no, crear uno nuevo
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(columns=['fecha', 'tipo', 'monto'])
    
    # Agregar la nueva entrada
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv(csv_file, index=False)
    
    return df

# Título de la app
st.title("Registro de Finanzas Personales")

# Entrada de datos
st.header("Ingresar Ingresos o Gastos y Fecha")

# Definir el presupuesto inicial
presupuesto_inicial = st.number_input("Presupuesto Inicial en pesos", min_value=0.0, step=0.01, format="%.2f", value=0.0)

# Opción para elegir si se ingresa un ingreso, un gasto o ambos
tipo_transaccion = st.selectbox("¿Qué deseas registrar?", ["Ingreso", "Gasto", "Ingreso y Gasto"])

# Ingreso de valores comunes
fecha_seleccionada = st.date_input("Seleccionar fecha", value=datetime.today().date())

# Si se selecciona "Ingreso" o "Gasto", muestra solo el campo correspondiente
if tipo_transaccion == "Ingreso" or tipo_transaccion == "Ingreso y Gasto":
    ingreso_monto = st.number_input("Monto del Ingreso en pesos", min_value=0.0, step=0.01, format="%.2f")
else:
    ingreso_monto = 0.0  # Si no es ingreso, no se pide

if tipo_transaccion == "Gasto" or tipo_transaccion == "Ingreso y Gasto":
    gasto_monto = st.number_input("Monto del Gasto en pesos", min_value=0.0, step=0.01, format="%.2f")
else:
    gasto_monto = 0.0  # Si no es gasto, no se pide

# Botón para guardar los datos
if st.button("Guardar Datos"):
    if tipo_transaccion == "Ingreso" and ingreso_monto > 0:
        df = guardar_datos("Ingreso", ingreso_monto, fecha_seleccionada)
        st.write("Ingreso guardado correctamente")
    elif tipo_transaccion == "Gasto" and gasto_monto > 0:
        df = guardar_datos("Gasto", gasto_monto, fecha_seleccionada)
        st.write("Gasto guardado correctamente")
    elif tipo_transaccion == "Ingreso y Gasto" and ingreso_monto > 0 and gasto_monto > 0:
        # Si es "Ingreso y Gasto", se guardan ambos valores
        df_ingreso = guardar_datos("Ingreso", ingreso_monto, fecha_seleccionada)
        df_gasto = guardar_datos("Gasto", gasto_monto, fecha_seleccionada)
        st.write("Ingreso y Gasto guardados correctamente")
    else:
        st.write("Por favor ingresa un monto mayor a 0 para Ingreso o Gasto")

# Mostrar el presupuesto restante
st.subheader(f"Presupuesto Restante: ${presupuesto_inicial:,.2f}")

# Calcular el presupuesto restante basado en los ingresos y gastos
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    # Sumar los ingresos y los gastos
    total_ingresos = df[df['tipo'] == 'Ingreso']['monto'].sum()
    total_gastos = df[df['tipo'] == 'Gasto']['monto'].sum()
    
    # Calcular el presupuesto restante
    presupuesto_restante = presupuesto_inicial + total_ingresos - total_gastos
    st.subheader(f"Presupuesto Restante: ${presupuesto_restante:,.2f}")
else:
    presupuesto_restante = presupuesto_inicial
    st.write("Aún no hay registros.")

# Mostrar la tabla de registros
st.subheader("Registros de Finanzas")

# Mostrar la tabla si el archivo CSV existe
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    df['monto'] = df['monto'].apply(lambda x: f"${x:,.2f}")  # Formatear los montos como pesos
    st.write(df)
else:
    st.write("Aún no hay registros.")



