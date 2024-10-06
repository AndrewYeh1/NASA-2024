import pygame
import random
import math

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ExoVerse")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

font = pygame.font.SysFont(None, 24)


#PUT THE INFORMATION OF THE STARS HERE REEEEEEEEEEEE
def generate_stars(num_stars, center_x, center_y):
    stars = []
    for i in range(num_stars):
        distance = random.uniform(100, 400)
        angle = random.uniform(0, 2 * math.pi)
        x = center_x + distance * math.cos(angle)
        y = center_y + distance * math.sin(angle)
        star_name = f"Star-{i + 1}"
        stars.append({'position': (x, y), 'name': star_name, 'clicked': False, 'selected': False})
    return stars



def draw_stars(screen, stars):
    for star in stars:
        x, y = star['position']
        if star['selected']:
            color = RED
        else:
            color = WHITE

        pygame.draw.circle(screen, color, (int(x), int(y)), 3)  # Draw small circles for stars

        # Display the name if the star is clicked
        if star['clicked']:
            name_surface = font.render(star['name'], True, WHITE)
            screen.blit(name_surface, (x + 10, y - 10))


def check_star_click(stars, mouse_pos):
    for star in stars:
        x, y = star['position']
        distance = math.sqrt((x - mouse_pos[0]) ** 2 + (y - mouse_pos[1]) ** 2)
        if distance <= 5:  # If the mouse is close enough to the star (within 5 pixels)
            star['clicked'] = True  # Mark the star as clicked


# Function to choose a star as the "location"
def choose_star_location(stars, mouse_pos):
    for star in stars:
        x, y = star['position']
        distance = math.sqrt((x - mouse_pos[0]) ** 2 + (y - mouse_pos[1]) ** 2)
        if distance <= 5:  # If the mouse is close enough to the star (within 5 pixels)
            # Deselect all other stars
            for other_star in stars:
                other_star['selected'] = False
            # Select the clicked star
            star['selected'] = True


# Main function
def main():
    running = True
    clock = pygame.time.Clock()

    # Set center of the "planet" (middle of the screen)
    planet_x = screen_width // 2
    planet_y = screen_height // 2

    # Generate stars with random positions and unique names
    num_stars = 100
    stars = generate_stars(num_stars, planet_x, planet_y)

    # Main loop
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if event.button == 1:  # Left-click to view the name of the star
                    check_star_click(stars, mouse_pos)
                elif event.button == 3:  # Right-click to choose the star as your location
                    choose_star_location(stars, mouse_pos)

        # Clear the screen
        screen.fill(BLACK)

        # Draw stars
        draw_stars(screen, stars)

        # Update the display
        pygame.display.flip()

        # Frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
