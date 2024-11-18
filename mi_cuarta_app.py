import streamlit as st
import pandas as pd

# Función para calcular el PAPA
def calcular_papa(df):
    # Cálculo del PAPA Global
    total_creditos = df['Créditos'].sum()
    promedio_ponderado = (df['Calificación'] * df['Créditos']).sum() / total_creditos
    return promedio_ponderado

def calcular_papa_por_tipologia(df, tipo_asignatura):
    # Filtrar por tipo de asignatura
    df_tipo = df[df['Tipo'] == tipo_asignatura]
    total_creditos = df_tipo['Créditos'].sum()
    if total_creditos == 0:
        return 0
    promedio_ponderado = (df_tipo['Calificación'] * df_tipo['Créditos']).sum() / total_creditos
    return promedio_ponderado

# Título de la app
st.title("Calculadora de PAPA - Universidad Nacional de Colombia")

# Entrada de datos: materias, calificaciones, créditos y tipo de asignatura
materias = st.text_area("Introduce las materias, separadas por coma").split(',')
calificaciones = st.text_area("Introduce las calificaciones correspondientes, separadas por coma").split(',')
creditos = st.text_area("Introduce los créditos correspondientes, separados por coma").split(',')
tipos = st.text_area("Introduce el tipo de asignatura (teórica, práctica, etc.), separadas por coma").split(',')

# Convertir entradas a listas
materias = [m.strip() for m in materias]
calificaciones = [float(c.strip()) for c in calificaciones]
creditos = [int(c.strip()) for c in creditos]
tipos = [t.strip() for t in tipos]

# Crear un DataFrame con los datos ingresados
df = pd.DataFrame({
    'Materia': materias,
    'Calificación': calificaciones,
    'Créditos': creditos,
    'Tipo': tipos
})

# Mostrar los datos ingresados
st.write("Datos ingresados:", df)

# Cálculo del PAPA global
papa_global = calcular_papa(df)
st.write(f"**PAPA Global:** {papa_global:.2f}")

# Seleccionar tipo de asignatura para calcular el PAPA por tipología
tipo_asignatura = st.selectbox("Selecciona el tipo de asignatura para calcular el PAPA por tipología", df['Tipo'].unique())

# Cálculo del PAPA por tipología
papa_tipologia = calcular_papa_por_tipologia(df, tipo_asignatura)
st.write(f"**PAPA por tipo '{tipo_asignatura}':** {papa_tipologia:.2f}")
