from . import planet

from coords import projectionTo2D


class ExoplanetSelector:
    def __init__(self, canvasIn):
        self.canvas = canvasIn

        self.planetData = projectionTo2D.PlanetProjection()
        self.planetData.project()
        self.planetX = self.planetData.viewX
        self.planetY = self.planetData.viewY

        self.planetList = []
        for i in range(len(self.planetX)):
            self.planetList.append(planet.Planet(self.planetX[i], self.planetY[i], 3, self.canvas, "P1"))

    def show(self):
        for i in self.planetList:
            i.show()

    def mouseClick(self, x, y):
        for i in self.planetList:
            if i.collision(x, y):
                i.setColor((255, 0, 0))
                return i.name
