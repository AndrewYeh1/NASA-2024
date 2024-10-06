import random
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from math import cos, sin

NUM_STARS = 150

class Star:
    def __init__(self, x, y, radius, name):
        self.x = x
        self.y = y
        self.radius = radius
        self.name = name
        self.selected = False

# Generate random 2D stars with varying sizes
def generate_stars(num_stars):
    stars = []
    for i in range(num_stars):
        x = random.uniform(-800, 800)
        y = random.uniform(-600, 600)
        radius = random.uniform(10, 30)
        name = f"Star-{i+1}"
        stars.append(Star(x, y, radius, name))
    return stars

# Render a circular star
def draw_star_circle(star):
    num_segments = 20
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 1, 1)

    glVertex2f(star.x, star.y)
    for i in range(num_segments + 1):
        angle = 2 * 3.14159 * i / num_segments
        glVertex2f(star.x + (star.radius * cos(angle)), star.y + (star.radius * sin(angle)))
    glEnd()

# Display star name when selected
def draw_star_name(star):
    font = pygame.font.SysFont("Arial", 18, True)
    text_surface = font.render(star.name, True, (255, 255, 255))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glRasterPos2f(star.x + star.radius + 10, star.y)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

    glDisable(GL_BLEND)

# Handle mouse click events to select a star
def handle_mouse_click(stars, pos, width, height):
    for star in stars:
        screen_x = (pos[0] / width) * 1600 - 800
        screen_y = -((pos[1] / height) * 1200 - 600)

        if abs(star.x - screen_x) < star.radius and abs(star.y - screen_y) < star.radius:
            for s in stars:
                s.selected = False
            star.selected = True
            return star
    return None

# Main function
def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("ExoSky")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-800, 800, -600, 600)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    
    zoom = 1.0

    stars = generate_stars(NUM_STARS)
    selected_star = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom *= 1.1
                if event.button == 5:
                    zoom /= 1.1

                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    selected_star = handle_mouse_click(stars, pos, width, height)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glScalef(zoom, zoom, 1)

        for star in stars:
            draw_star_circle(star)

        if selected_star:
            draw_star_name(selected_star)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
