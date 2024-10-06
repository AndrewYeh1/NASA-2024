import pygame


class PlanetInfoPanel:
    def __init__(self, canvasIn):
        self.canvas = canvasIn

        self.planet = ""

        self.rect = pygame.Rect(10, 10, 100, 200)
        self.font = pygame.font.SysFont("Arial", 10)
        self.planetTextSurface = self.font.render(self.planet, False, (0, 0, 0))

    def show(self):
        pygame.draw.rect(self.canvas, (200, 200, 200), self.rect)
        self.canvas.blit(self.planetTextSurface, (50, 50))

    def setPlanet(self, planetIn):
        self.planet = planetIn
        self.planetTextSurface = self.font.render(self.planet, False, (0, 0, 0))
