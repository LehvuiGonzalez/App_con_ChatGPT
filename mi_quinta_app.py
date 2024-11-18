import streamlit as st
import random
import time
import math

# Función para analizar la operación matemática y dividirla en números y operadores
def parse_expression(expression):
    numbers = [int(s) for s in expression.split() if s.isdigit()]
    operators = [s for s in expression.split() if not s.isdigit()]
    return numbers, operators

# Función para generar el flujo de partículas a partir de la operación
def generate_particle_flow(numbers, operators, canvas_width, canvas_height):
    particles = []
    x_pos = 50
    y_pos = 100

    # Crear partículas para los números
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

    # Crear partículas para los operadores
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

    # Crear una partícula para el resultado de la operación
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

# Crear lienzo para el flujo de partículas
canvas = st.empty()  # Este será el espacio para actualizar las partículas

# Generar y mostrar el flujo de partículas
if expression:
    particles, result = generate_particle_flow(numbers, operators, canvas_width, canvas_height)
    
    # Simular el movimiento de las partículas
    for _ in range(30):  # Ejecutar varias iteraciones para simular el movimiento
        particles = update_particles(particles, canvas_width, canvas_height)

        # Dibuja las partículas en el lienzo de Streamlit
        canvas.markdown("### Operación en flujo de partículas")

        for particle in particles:
            if particle['type'] == 'number':
                canvas.markdown(f"**Número:** {particle['value']} ({particle['x']:.2f}, {particle['y']:.2f})")
            elif particle['type'] == 'operator':
                canvas.markdown(f"**Operador:** {particle['value']} ({particle['x']:.2f}, {particle['y']:.2f})")
            elif particle['type'] == 'result':
                canvas.markdown(f"**Resultado:** {particle['value']} ({particle['x']:.2f}, {particle['y']:.2f})")
        
        # Hacer una pausa entre iteraciones para simular el movimiento de las partículas
        time.sleep(0.1)
    
    # Mostrar el resultado de la operación
    st.write(f"El resultado de la operación es: {result}")
