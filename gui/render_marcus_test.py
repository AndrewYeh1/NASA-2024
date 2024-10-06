from re import S
import pygame

pygame.init()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

clock = pygame.time.Clock()

bg = pygame.image.load(open("resources\milkyway_2020_4k_gal_print.jpg"))
#centre of image has RA = 0 and DEC = 0

#star
def star(xPos, yPos, distance, size):
    displayColour = (255,255,255) #add colour functions
    rect = pygame.Rect(xPos, yPos, size/distance**2, size/distance**2) #size/dist^2 is apparent size change due to dist
    width = 0 #if width > 0, circle will be hollow
    pygame.draw.ellipse(screen, displayColour, rect, width)     
    return [xPos, yPos, size/distance**2, size/distance**2] # button rect info (x,y,width,length)


buttonList = []
buttonList.append(star(5,5,200,200))
#test^ will put for star(x pos, ypos)
testButton = star(5,5,200,200)
#for star in list do the function above^

lineList = []

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #for i in buttonList :
            testButton = pygame.Rect(buttonList[0])
            if testButton.collidepoint(events.pos):
                lineList.append(buttonList[0][0],buttonList[0][1]) #xy data for star
                testSquare = pygame.Rect(10, 10, 10, 10)
    
                pygame.draw.rect(screen, (255, 0, 0), testSquare)
    a,b = pygame.mouse.get_pos(            

    # Do logical updates here.
    # ...

    screen.fill("black")  # Fill the display with a solid color
    screen.blit(bg, (0, 0))
    
    # Render the graphics here.

    #parameters: x pos, y pos, distance, size
    star(5,5,1,500)

    

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(30)         # wait until next frame (at 30 FPS)
 

