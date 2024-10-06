import pygame

from gui import exoplanetSelector


class Gui:
    def __init__(self):
        # pygame initialization
        pygame.init()
        canvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Starmap")

        # pygame 3d viewport display
        self.planetSelector = exoplanetSelector.ExoplanetSelector(canvas)

        self.run()

    def run(self):
        ex = False
        while not ex:
            self.planetSelector.show()

            x, y = pygame.mouse.get_pos()
            self.planetSelector.mouse(x, y)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ex = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            pygame.display.update()

