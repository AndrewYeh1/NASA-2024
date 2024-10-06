import pygame

from . import exoplanetSelector


class Gui:
    def __init__(self):
        pygame.init()
        canvas = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Starmap")

        self.planetSelector = exoplanetSelector.ExoplanetSelector(canvas)

        self.run()

    def run(self):
        ex = False
        while not ex:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ex = True
            self.planetSelector.show()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ex = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    selectedPlanet = self.planetSelector.mouseClick(x, y)
                    print(selectedPlanet)

            pygame.display.update()

