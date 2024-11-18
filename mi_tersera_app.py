import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Función para almacenar los datos en un DataFrame (simulando una base de datos simple)
def obtener_datos():
    try:
        df = pd.read_csv("finanzas_personales.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Fecha", "Categoria", "Monto", "Tipo", "Descripcion"])
    return df

# Función para guardar los datos en un CSV
def guardar_datos(df):
    df.to_csv("finanzas_personales.csv", index=False)

# Pantalla principal
def mostrar_dashboard():
    st.title("App de Finanzas Personales")
    
    # Menú de navegación
    opcion = st.sidebar.selectbox("Selecciona una opción", ["Inicio", "Ingresos", "Gastos", "Presupuestos", "Metas de Ahorro", "Reportes"])

    if opcion == "Inicio":
        st.header("Bienvenido a tu Dashboard de Finanzas Personales")
        df = obtener_datos()
        st.write("Resumen de tu situación financiera")
        st.write(f"Número total de transacciones: {len(df)}")
        
        ingresos = df[df['Tipo'] == 'Ingreso']['Monto'].sum()
        gastos = df[df['Tipo'] == 'Gasto']['Monto'].sum()
        st.write(f"Ingresos Totales: {ingresos}")
        st.write(f"Gastos Totales: {gastos}")
        st.write(f"Balance: {ingresos - gastos}")

    elif opcion == "Ingresos":
        st.header("Registrar Ingreso")
        monto = st.number_input("Monto del Ingreso", min_value=0.0, step=0.01)
        categoria = st.text_input("Categoría del Ingreso")
        descripcion = st.text_input("Descripción")
        
        if st.button("Guardar Ingreso"):
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            df = obtener_datos()
            df = df.append({"Fecha": fecha, "Categoria": categoria, "Monto": monto, "Tipo": "Ingreso", "Descripcion": descripcion}, ignore_index=True)
            guardar_datos(df)
            st.success("Ingreso guardado exitosamente!")

    elif opcion == "Gastos":
        st.header("Registrar Gasto")
        monto = st.number_input("Monto del Gasto", min_value=0.0, step=0.01)
        categoria = st.text_input("Categoría del Gasto")
        descripcion = st.text_input("Descripción")
        
        if st.button("Guardar Gasto"):
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            df = obtener_datos()
            df = df.append({"Fecha": fecha, "Categoria": categoria, "Monto": monto, "Tipo": "Gasto", "Descripcion": descripcion}, ignore_index=True)
            guardar_datos(df)
            st.success("Gasto guardado exitosamente!")

    elif opcion == "Presupuestos":
        st.header("Registrar Presupuesto")
        categoria = st.text_input("Categoría del Presupuesto")
        monto_presupuestado = st.number_input("Monto Presupuestado", min_value=0.0, step=0.01)
        
        if st.button("Guardar Presupuesto"):
            # Aquí podrías guardar este presupuesto en otro archivo o DataFrame
            st.success(f"Presupuesto para {categoria} guardado exitosamente!")

    elif opcion == "Metas de Ahorro":
        st.header("Establecer Meta de Ahorro")
        meta = st.text_input("Nombre de la Meta de Ahorro")
        monto_meta = st.number_input("Monto de la Meta", min_value=0.0, step=0.01)
        
        if st.button("Guardar Meta de Ahorro"):
            st.success(f"Meta de ahorro '{meta}' guardada con un monto de {monto_meta}!")

    elif opcion == "Reportes":
        st.header("Reportes de Finanzas")
        df = obtener_datos()
        
        # Reporte mensual
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        df['Mes'] = df['Fecha'].dt.to_period('M')
        
        resumen_mensual = df.groupby([df['Mes'], 'Tipo']).agg({"Monto": "sum"}).unstack(fill_value=0)
        st.write("Reporte Mensual")
        st.write(resumen_mensual)

        # Reporte semanal
        df['Semana'] = df['Fecha'].dt.to_period('W')
        resumen_semanal = df.groupby([df['Semana'], 'Tipo']).agg({"Monto": "sum"}).unstack(fill_value=0)
        st.write("Reporte Semanal")
        st.write(resumen_semanal)

        # Graficos de comparación
        st.write("Gráfico de Comparación de Ingresos y Gastos Mensuales")
        resumen_mensual['Monto', 'Ingreso'].plot(kind='bar', label="Ingresos", color='green')
        resumen_mensual['Monto', 'Gasto'].plot(kind='bar', label="Gastos", color='red', alpha=0.6)
        plt.title('Comparación de Ingresos y Gastos Mensuales')
        plt.xlabel('Mes')
        plt.ylabel('Monto')
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(plt)

if __name__ == "__main__":
    mostrar_dashboard()


