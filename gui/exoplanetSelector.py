import pygame

from gui import button


class ExoplanetSelector:
    def __init__(self, canvasIn):
        self.canvas = canvasIn

        planetX = [250, 230, 280]
        planetY = [300, 300, 300]

        self.buttonList = []
        for i in range(len(planetX)):
            self.buttonList.append(button.Button(planetX[i], planetY[i], 5, self.canvas))

    def show(self):
        for i in self.buttonList:
            i.show()

    def mouse(self, x, y):
        for i in self.buttonList:
            if i.collision(x, y):
                i.setColor((255, 0, 0))
