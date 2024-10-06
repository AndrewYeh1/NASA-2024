from gui import star

from coords import starData


class StarmapViewer:
    def __init__(self, canvasIn):
        self.canvas = canvasIn

        planetX = [250, 230, 280]
        planetY = [300, 300, 300]

        self.starList = []
        for i in range(len(planetX)):
            self.starList.append(star.Star(planetX[i], planetY[i], 3, self.canvas, "P1"))

    def show(self):
        for i in self.starList:
            i.show()

    def mouseClick(self, x, y):
        for i in self.starList:
            if i.collision(x, y):
                i.setColor((255, 0, 0))
                return i.name
