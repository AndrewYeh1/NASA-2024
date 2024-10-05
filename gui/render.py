import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

def star(xPos, yPos, distance, size):
    displayColour = (255,255,255) #add colour functions
    rect = pygame.Rect(xPos, yPos, size/distance**2, size/distance**2) #size/dist^2 is apparent size change due to dist
    width = 0 #if width > 0, circle will be hollow
    pygame.draw.ellipse(screen, displayColour, rect, width)      
    
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("black")  # Fill the display with a solid color
    gameDisplay.blit(bg, (0, 0))
    
    # Render the graphics here.
    star(5,5,5,100)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(30)         # wait until next frame (at 30 FPS)
 

