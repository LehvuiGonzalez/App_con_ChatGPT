import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Ruta del archivo CSV para almacenar los datos
csv_file = 'registro_finanzas.csv'

# Función para almacenar los datos
def guardar_datos(tipo, monto, fecha, presupuesto_restante):
    data = {
        'fecha': fecha,
        'tipo': tipo,
        'monto': monto,
        'presupuesto_restante': presupuesto_restante
    }
    
    # Verificar si el archivo CSV existe, si no, crear uno nuevo
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(columns=['fecha', 'tipo', 'monto', 'presupuesto_restante'])
    
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
    # Inicializar el presupuesto restante
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        total_ingresos = df[df['tipo'] == 'Ingreso']['monto'].apply(lambda x: float(x.replace('$', '').replace(',', ''))).sum()
        total_gastos = df[df['tipo'] == 'Gasto']['monto'].apply(lambda x: float(x.replace('$', '').replace(',', ''))).sum()
        presupuesto_restante = presupuesto_inicial + total_ingresos - total_gastos
    else:
        presupuesto_restante = presupuesto_inicial
    
    # Ajustar el presupuesto restante según el tipo de transacción
    if tipo_transaccion == "Ingreso" and ingreso_monto > 0:
        presupuesto_restante += ingreso_monto  # Si es un ingreso, se suma al presupuesto
        df = guardar_datos("Ingreso", ingreso_monto, fecha_seleccionada, presupuesto_restante)
        st.write("Ingreso guardado correctamente")
    elif tipo_transaccion == "Gasto" and gasto_monto > 0:
        presupuesto_restante -= gasto_monto  # Si es un gasto, se resta del presupuesto
        df = guardar_datos("Gasto", gasto_monto, fecha_seleccionada, presupuesto_restante)
        st.write("Gasto guardado correctamente")
    elif tipo_transaccion == "Ingreso y Gasto" and ingreso_monto > 0 and gasto_monto > 0:
        # Si es "Ingreso y Gasto", se suman los ingresos y se restan los gastos
        presupuesto_restante += ingreso_monto
        presupuesto_restante -= gasto_monto
        df_ingreso = guardar_datos("Ingreso", ingreso_monto, fecha_seleccionada, presupuesto_restante)
        df_gasto = guardar_datos("Gasto", gasto_monto, fecha_seleccionada, presupuesto_restante)
        st.write("Ingreso y Gasto guardados correctamente")
    else:
        st.write("Por favor ingresa un monto mayor a 0 para Ingreso o Gasto")

# Mostrar la tabla de registros
st.subheader("Registros de Finanzas")

# Mostrar la tabla si el archivo CSV existe
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    df['monto'] = df['monto'].apply(lambda x: f"${x:,.2f}")  # Formatear los montos como pesos
    df['presupuesto_restante'] = df['presupuesto_restante'].apply(lambda x: f"${x:,.2f}")  # Formatear el presupuesto restante como pesos
    st.write(df)

else:
    st.write("Aún no hay registros.")


