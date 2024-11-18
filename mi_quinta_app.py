import streamlit as st
import math
import random
import numpy as np
from streamlit_drawable_canvas import st_canvas

# Función para analizar la operación matemática y dividirla en componentes
def parse_expression(expression):
    # Dividir la expresión en números y operadores
    numbers = [int(s) for s in expression.split() if s.isdigit()]
    operators = [s for s in expression.split() if not s.isdigit()]
    return numbers, operators

# Crear un flujo de partículas para la operación matemática
def generate_particle_flow(numbers, operators, canvas_width, canvas_height):
    particles = []
    x_pos = 50
    y_pos = 100

    # Generar partículas para los números
    for number in numbers:
        particles.append({
            'type': 'number',
            'value': number,
            'x': x_pos,
            'y': y_pos,
            'dx': random.uniform(1, 3),
            'dy': random.uniform(-1, 1),
        })
        x_pos += 50  # Desplazamiento horizontal

    # Generar partículas para los operadores
    for operator in operators:
        particles.append({
            'type': 'operator',
            'value': operator,
            'x': x_pos,
            'y': y_pos,
            'dx': random.uniform(1, 3),
            'dy': random.uniform(-1, 1),
        })
        x_pos += 50  # Desplazamiento horizontal

    # Generar partículas para los resultados
    result = eval(' '.join([str(num) for num in numbers] + operators))
    particles.append({
        'type': 'result',
        'value': result,
        'x': x_pos,
        'y': y_pos,
        'dx': random.uniform(1, 3),
        'dy': random.uniform(-1, 1),
    })

    return particles, result

# Función para actualizar las partículas
def update_particles(particles, canvas_width, canvas_height):
    for particle in particles:
        particle['x'] += particle['dx']
        particle['y'] += particle['dy']
        
        # Rebotar las partículas al llegar al borde
        if particle['x'] <= 0 or particle['x'] >= canvas_width:
            particle['dx'] = -particle['dx']
        if particle['y'] <= 0 or particle['y'] >= canvas_height:
            particle['dy'] = -particle['dy']
    return particles

# Streamlit app
st.title("Operación Matemática como Flujo de Partículas")

# Input de la operación matemática
expression = st.text_input("Ingresa una operación matemática (Ej: 3 + 5 * 2):", "3 + 5 * 2")

# Análisis de la operación
numbers, operators = parse_expression(expression)
canvas_width = 700
canvas_height = 500

# Crear lienzo interactivo para el flujo de partículas
canvas_result = st_canvas(
    fill_color="white",  # Color de fondo
    stroke_color="black",  # Color del trazo
    stroke_width=2,  # Grosor del trazo
    background_color="white",  # Color de fondo del canvas
    width=canvas_width,  # Ancho
    height=canvas_height,  # Alto
    drawing_mode="freedraw",  # Modo de dibujo libre
    key="canvas",
)

# Generar y mostrar el flujo de partículas
if expression:
    particles, result = generate_particle_flow(numbers, operators, canvas_width, canvas_height)
    
    # Actualizar las partículas
    particles = update_particles(particles, canvas_width, canvas_height)

    # Dibujar las partículas en el lienzo
    for particle in particles:
        if particle['type'] == 'number':
            st.markdown(f"**Número:** {particle['value']} ({particle['x']}, {particle['y']})")
        elif particle['type'] == 'operator':
            st.markdown(f"**Operador:** {particle['value']} ({particle['x']}, {particle['y']})")
        elif particle['type'] == 'result':
            st.markdown(f"**Resultado:** {particle['value']} ({particle['x']}, {particle['y']})")

    # Mostrar el resultado de la operación
    st.write(f"El resultado de la operación es: {result}")


