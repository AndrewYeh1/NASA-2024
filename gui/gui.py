import pygame


class Gui:
    def __init__(self):
        pygame.init()
        canvas = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Starmap")
        self.run()

    def run(self):
        ex = False
        while not ex:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ex = True
            pygame.display.update()

