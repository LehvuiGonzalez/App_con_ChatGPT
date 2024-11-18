import streamlit as st
import numpy as np
import pygame
from streamlit_canvas import st_canvas

# Inicializar pygame
pygame.init()

# Configurar el tamaño de la ventana
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animación de Operación Matemática")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Configuración de partículas
class Particle:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += 0.1  # Efecto de gravedad
        if self.x > screen_width or self.x < 0:
            self.dx *= -1
        if self.y > screen_height:
            self.dy *= -0.9  # Rebote
            self.y = screen_height - 1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)

# Crear partículas
def generate_particles(x, y, num_particles=50, color=BLUE):
    particles = []
    for _ in range(num_particles):
        dx = np.random.uniform(-2, 2)
        dy = np.random.uniform(-5, -1)
        particles.append(Particle(x, y, dx, dy, color))
    return particles

# Lógica de animación
def animate_operation():
    # Operación matemática
    number1 = 45
    number2 = 56
    result = number1 + number2

    # Animación de la operación
    particles = generate_particles(screen_width // 2, screen_height // 2)

    # Bucle de animación
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Rellenar pantalla de blanco
        screen.fill(WHITE)

        # Dibujar partículas
        for particle in particles:
            particle.move()
            particle.draw()

        # Mostrar la operación en la pantalla
        font = pygame.font.Font(None, 74)
        text = font.render(f'{number1} + {number2} = {result}', True, RED)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, 50))

        pygame.display.flip()

        # Limitar la tasa de frames
        clock.tick(60)

    pygame.quit()

# Ejecutar la animación en la app de Streamlit
if st.button('Ver animación de operación'):
    animate_operation()

