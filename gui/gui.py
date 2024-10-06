import pygame

from . import exoplanetSelector
from . import starmapViewer
from . import planetInfoPanel


class Gui:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.canvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Starmap")

        self.planetSelector = exoplanetSelector.ExoplanetSelector(self.canvas)
        self.starmapViewer = starmapViewer.StarmapViewer(self.canvas)
        self.planetInfo = planetInfoPanel.PlanetInfoPanel(self.canvas)

        self.screen = "planet"

        self.run()

    def run(self):
        ex = False
        while not ex:
            self.canvas.fill((0, 0, 0))

            if self.screen == "planet":
                self.planetSelector.show()
            elif self.screen == "star":
                self.starmapViewer.show()

            # mouse over events
            x, y = pygame.mouse.get_pos()
            if self.screen == "planet":
                hoverPlanet = self.planetSelector.mouseOver(x, y)
                if hoverPlanet != "none":
                    self.planetInfo.setPlanet(hoverPlanet)
                    self.planetInfo.show()
            elif self.screen == "star":
                self.starmapViewer.mouseOver(x, y)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ex = True

                # mouse events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("mouse down")
                    x, y = pygame.mouse.get_pos()
                    if self.screen == "planet":
                        selectedPlanet = self.planetSelector.mouseClick(x, y)
                        if selectedPlanet != "none":
                            self.screen = "star"
                            self.starmapViewer.setPlanet(selectedPlanet)
                    if self.screen == "star":
                        self.starmapViewer.mouseClick(x, y)

            pygame.display.update()

