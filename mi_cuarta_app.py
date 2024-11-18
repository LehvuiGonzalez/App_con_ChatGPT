import streamlit as st
import pandas as pd

# Función para calcular el PAPA global
def calcular_papa(df):
    total_creditos = df['Créditos'].sum()
    promedio_ponderado = (df['Calificación'] * df['Créditos']).sum() / total_creditos
    return promedio_ponderado

# Función para calcular el PAPA por tipología
def calcular_papa_por_tipologia(df, tipo_asignatura):
    df_tipo = df[df['Tipo'] == tipo_asignatura]
    total_creditos = df_tipo['Créditos'].sum()
    if total_creditos == 0:
        return 0
    promedio_ponderado = (df_tipo['Calificación'] * df_tipo['Créditos']).sum() / total_creditos
    return promedio_ponderado

# Título de la app
st.title("Calculadora de PAPA - Universidad Nacional de Colombia")

# Introducción para el formulario
st.write("""
    **Por favor, ingrese la información de cada materia de manera individual.**
    Asegúrese de completar todos los campos antes de continuar con el cálculo.
""")

# Crear una lista para almacenar los datos de las materias
materias = []
calificaciones = []
creditos = []
tipos = []

# Formulario para ingresar datos de las materias una por una
with st.form(key='materia_form'):
    materia = st.text_input("Nombre de la materia")
    calificacion = st.number_input("Calificación obtenida", min_value=0.0, max_value=5.0, step=0.1)
    credito = st.number_input("Número de créditos", min_value=1, max_value=6, step=1)
    tipo = st.selectbox("Tipo de asignatura", ["Teórica", "Práctica", "Laboratorio", "Seminario"])
    
    # Botón para agregar la materia
    agregar = st.form_submit_button("Agregar materia")

    if agregar:
        if materia and calificacion and credito and tipo:
            materias.append(materia)
            calificaciones.append(calificacion)
            creditos.append(credito)
            tipos.append(tipo)
            st.success(f"Materia '{materia}' agregada correctamente.")
        else:
            st.error("Por favor, complete todos los campos.")

# Mostrar las materias ingresadas hasta ahora
if materias:
    st.write("Materias ingresadas:")
    df = pd.DataFrame({
        'Materia': materias,
        'Calificación': calificaciones,
        'Créditos': cred
