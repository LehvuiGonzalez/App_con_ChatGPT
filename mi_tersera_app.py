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

# Opción para elegir si se ingresa un ingreso, un gasto o ambos
tipo_transaccion = st.selectbox("¿Qué deseas registrar?", ["Ingreso", "Gasto", "Ingreso y Gasto"])

# Ingreso de valores
monto = st.number_input("Monto en pesos", min_value=0.0, step=0.01)
fecha_seleccionada = st.date_input("Seleccionar fecha", value=datetime.today().date())

# Botón para guardar los datos
if st.button("Guardar Datos"):
    if monto > 0:
        # Si se elige "Ingreso y Gasto", se agregan ambos registros
        if tipo_transaccion == "Ingreso":
            df = guardar_datos("Ingreso", monto, fecha_seleccionada)
            st.write("Ingreso guardado correctamente")
        elif tipo_transaccion == "Gasto":
            df = guardar_datos("Gasto", monto, fecha_seleccionada)
            st.write("Gasto guardado correctamente")
        elif tipo_transaccion == "Ingreso y Gasto":
            # Si es Ingreso y Gasto, se guardan ambos tipos con el mismo monto
            df_ingreso = guardar_datos("Ingreso", monto, fecha_seleccionada)
            df_gasto = guardar_datos("Gasto", monto, fecha_seleccionada)
            st.write("Ingreso y Gasto guardados correctamente")
    else:
        st.write("Por favor ingresa un valor mayor a 0")

# Mostrar la tabla de registros
st.subheader("Registros de Finanzas")

# Mostrar la tabla si el archivo CSV existe
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    df['monto'] = df['monto'].apply(lambda x: f"${x:,.2f}")  # Formatear los montos como pesos
    st.write(df)
else:
    st.write("Aún no hay registros.")


