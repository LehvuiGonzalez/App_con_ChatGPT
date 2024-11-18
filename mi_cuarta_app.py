import streamlit as st
import pandas as pd

# Función para calcular el P.A.P.A.
def calcular_papa(datos):
    suma_ponderada = sum(datos['Calificación'] * datos['Créditos'])
    suma_creditos = sum(datos['Créditos'])
    papa = suma_ponderada / suma_creditos
    return papa

# Pantalla principal de la app
def mostrar_dashboard():
    st.title("Calculadora de P.A.P.A. - Promedio Académico Ponderado Acumulado")
    
    # Ingreso de datos por parte del usuario
    st.header("Ingresa los datos de tus materias")

    # Crear un formulario para ingresar varias materias
    num_materias = st.number_input("Número de materias", min_value=1, max_value=20, value=1)

    # Crear listas para almacenar los datos
    materias = []
    calificaciones = []
    creditos = []
    tipos_materia = []

    tipos = ["Optativa", "Obligatoria", "Libre", "Otra"]  # Tipos de materias

    for i in range(num_materias):
        st.subheader(f"Materia {i+1}")
        materia = st.text_input(f"Nombre de la materia {i+1}", key=f"materia_{i}")
        calificacion = st.number_input(f"Calificación obtenida en {materia}", min_value=0.0, max_value=5.0, step=0.1, key=f"calificacion_{i}")
        credito = st.number_input(f"Créditos de {materia}", min_value=1, max_value=10, step=1, key=f"credito_{i}")
        
        # Selección del tipo de materia
        tipo_materia = st.selectbox(f"Tipo de {materia}", tipos, key=f"tipo_{i}")
        
        # Almacenamos los valores ingresados
        if materia and calificacion and credito:
            materias.append(materia)
            calificaciones.append(calificacion)
            creditos.append(credito)
            tipos_materia.append(tipo_materia)
    
    # Crear DataFrame con los datos ingresados
    datos = pd.DataFrame({
        "Materia": materias,
        "Calificación": calificaciones,
        "Créditos": creditos,
        "Tipo": tipos_materia
    })

    # Botón para calcular el P.A.P.A.
    if st.button("Calcular P.A.P.A."):
        if len(materias) > 0:
            # Calcular el P.A.P.A.
            papa = calcular_papa(datos)
            st.subheader("Resultado del cálculo del P.A.P.A.")
            st.write(f"Tu **P.A.P.A.** es: {papa:.2f}")
            st.write("Detalles de tus materias:")
            st.dataframe(datos)
        else:
            st.warning("Por favor, ingresa los datos de al menos una materia para calcular el P.A.P.A.")

if __name__ == "__main__":
    mostrar_dashboard()

