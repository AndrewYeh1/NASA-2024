import pygame

pygame.init()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

clock = pygame.time.Clock()

bg = pygame.image.load(open("resources\milkyway_2020_4k_gal_print.jpg"))
#centre of image has RA = 0 and DEC = 0

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
    screen.blit(bg, (0, 0))
    
    # Render the graphics here.
    
    #parameters: x pos, y pos, distance, size
    star(5,5,1,500)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(30)         # wait until next frame (at 30 FPS)
 

