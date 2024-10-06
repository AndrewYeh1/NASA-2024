from . import star

from coords import starData


class StarmapViewer:
    def __init__(self, canvasIn):
        self.canvas = canvasIn

        starX = [250, 230, 280]
        starY = [300, 300, 300]
        names = ["P1", "P2", "P3"]

        self.starList = []
        self.generateStarList(names, starX, starY)

    def show(self):
        for i in self.starList:
            i.show()

    def mouseClick(self, x, y):
        for i in self.starList:
            if i.collision(x, y):
                return i.name

    def setPlanet(self, planet):
        pass

    def generateStarList(self, names, starX, starY):
        self.starList = []
        for i, name in enumerate(names):
            self.starList.append(star.Star(starX[i], starY[i], 3, self.canvas, name))
