from gui import planet

from coords import planetData


class ExoplanetSelector:
    def __init__(self, canvasIn):
        self.canvas = canvasIn

        planetX = [250, 230, 280]
        planetY = [300, 300, 300]

        self.planetList = []
        for i in range(len(planetX)):
            self.planetList.append(planet.Planet(planetX[i], planetY[i], 3, self.canvas, "P1"))

    def show(self):
        for i in self.planetList:
            i.show()

    def mouseClick(self, x, y):
        for i in self.planetList:
            if i.collision(x, y):
                i.setColor((255, 0, 0))
                return i.name
