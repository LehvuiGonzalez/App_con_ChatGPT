import streamlit as st

# Función principal de conversión
def convert_units(conversion_type, value):
    conversions = {
        # Conversiones de temperatura
        "Celsius a Fahrenheit": lambda x: (x * 9/5) + 32,
        "Fahrenheit a Celsius": lambda x: (x - 32) * 5/9,
        "Celsius a Kelvin": lambda x: x + 273.15,
        "Kelvin a Celsius": lambda x: x - 273.15,
        
        # Conversiones de longitud
        "Pies a metros": lambda x: x * 0.3048,
        "Metros a pies": lambda x: x / 0.3048,
        "Pulgadas a centímetros": lambda x: x * 2.54,
        "Centímetros a pulgadas": lambda x: x / 2.54,
        
        # Conversiones de peso/masa
        "Libras a kilogramos": lambda x: x * 0.453592,
        "Kilogramos a libras": lambda x: x / 0.453592,
        "Onzas a gramos": lambda x: x * 28.3495,
        "Gramos a onzas": lambda x: x / 28.3495,
        
        # Conversiones de volumen
        "Galones a litros": lambda x: x * 3.78541,
        "Litros a galones": lambda x: x / 3.78541,
        "Pulgadas cúbicas a centímetros cúbicos": lambda x: x * 16.3871,
        "Centímetros cúbicos a pulgadas cúbicas": lambda x: x / 16.3871,
        
        # Conversiones de tiempo
        "Horas a minutos": lambda x: x * 60,
        "Minutos a segundos": lambda x: x * 60,
        "Días a horas": lambda x: x * 24,
        "Semanas a días": lambda x: x * 7,
        
        # Conversiones de velocidad
        "Millas por hora a kilómetros por hora": lambda x: x * 1.60934,
        "Kilómetros por hora a metros por segundo": lambda x: x / 3.6,
        "Nudos a millas por hora": lambda x: x * 1.15078,
        "Metros por segundo a pies por segundo": lambda x: x * 3.28084,
        
        # Conversiones de área
        "Metros cuadrados a pies cuadrados": lambda x: x * 10.7639,
        "Pies cuadrados a metros cuadrados": lambda x: x / 10.7639,
        "Kilómetros cuadrados a millas cuadradas": lambda x: x * 0.386102,
        "Millas cuadradas a kilómetros cuadrados": lambda x: x / 0.386102,
        
        # Conversiones de energía
        "Julios a calorías": lambda x: x / 4.184,
        "Calorías a kilojulios": lambda x: x * 4.184,
        "Kilovatios-hora a megajulios": lambda x: x * 3.6,
        "Megajulios a kilovatios-hora": lambda x: x / 3.6,
        
        # Conversiones de presión
        "Pascales a atmósferas": lambda x: x / 101325,
        "Atmósferas a pascales": lambda x: x * 101325,
        "Barras a libras por pulgada cuadrada": lambda x: x * 14.5038,
        "Libras por pulgada cuadrada a bares": lambda x: x / 14.5038,
        
        # Conversiones de tamaño de datos
        "Megabytes a gigabytes": lambda x: x / 1024,
        "Gigabytes a Terabytes": lambda x: x / 1024,
        "Kilobytes a megabytes": lambda x: x / 1024,
        "Terabytes a petabytes": lambda x: x / 1024,
    }
    return conversions[conversion_type](value)

# Configuración de la aplicación
st.title("Conversor Universal en Tiempo Real")
st.write("Selecciona una categoría, el tipo de conversión y proporciona un valor.")

# Selección de categoría
categories = {
    "Temperatura": ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"],
    "Longitud": ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"],
    "Peso/Masa": ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"],
    "Volumen": ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"],
    "Tiempo": ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"],
    "Velocidad": ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"],
    "Área": ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"],
    "Energía": ["Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"],
    "Presión": ["Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"],
    "Tamaño de datos": ["Megabytes a gigabytes", "Gigabytes a Terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"],
}

# Categoría y tipo de conversión
category = st.selectbox("Selecciona una categoría", list(categories.keys()))
conversion_type = st.selectbox("Selecciona un tipo de conversión", categories[category])

# Unidades de entrada y salida
input_unit = st.text_input("Unidad de entrada (por ejemplo, 10)".format(conversion_type))
output_unit = st.text_input("Unidad de salida (por ejemplo, 100)".format(conversion_type))

# Ingreso del valor para la conversión
value = st.number_input("Ingresa el valor a convertir", min_value=0.0, step=0.1)

# Si se ingresa un valor, realizar la conversión en tiempo real
if value:
    result = convert_units(conversion_type, value)
    st.write(f"Se ha convertido: {value} {input_unit} a {result} {output_unit}.")
