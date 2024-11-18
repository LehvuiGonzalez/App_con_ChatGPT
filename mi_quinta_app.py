import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Función para analizar la operación matemática y dividirla en números y operadores
def parse_expression(expression):
    numbers = [int(s) for s in expression.split() if s.isdigit()]
    operators = [s for s in expression.split() if not s.isdigit()]
    return numbers, operators

# Función para generar el flujo de partículas a partir de la operación
def generate_particle_flow(numbers, operators):
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
            'color': random.choice(['red', 'green', 'blue', 'orange', 'purple', 'yellow'])
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
            'color': random.choice(['red', 'green', 'blue', 'orange', 'purple', 'yellow'])
        })
        x_pos += 50  # Desplazamiento horizontal

    return particles

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
st.title("Visualización Matemática con Partículas")

# Input de la operación matemática
expression = st.text_input("Ingresa una operación matemática (Ej: 3 + 5 * 2):", "3 + 5 * 2")

# Crear el botón para iniciar el flujo de partículas
if st.button("Generar Partículas"):
    if expression:
        numbers, operators = parse_expression(expression)
        canvas_width = 700
        canvas_height = 500

        # Generar las partículas basadas en la operación
        particles = generate_particle_flow(numbers, operators)

        # Configurar el gráfico de matplotlib
        fig, ax = plt.subplots(figsize=(canvas_width / 100, canvas_height / 100), dpi=100)
        ax.set_xlim(0, canvas_width)
        ax.set_ylim(0, canvas_height)
        ax.set_facecolor('white')

        # Simular el movimiento de las partículas
        for _ in range(30):  # Ejecutar varias iteraciones para simular el movimiento
            particles = update_particles(particles, canvas_width, canvas_height)

            # Limpiar el gráfico para actualizar las partículas
            ax.clear()

            # Dibujar las partículas sobre el gráfico
            for particle in particles:
                ax.text(particle['x'], particle['y'], str(particle['value']), color=particle['color'], fontsize=12, ha='center')

            # Establecer límites y colores de fondo
            ax.set_xlim(0, canvas_width)
            ax.set_ylim(0, canvas_height)
            ax.set_facecolor('white')

            # Actualizar la visualización
            st.pyplot(fig)

            # Hacer una pausa entre iteraciones para simular el movimiento de las partículas
            time.sleep(0.1)

        st.write(f"Resultado de la operación: {eval(expression)}")
