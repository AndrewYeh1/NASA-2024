from . import star

from coords import starProjection

import pygame


class StarmapViewer:
    def __init__(self, canvasIn):
        self.canvas = canvasIn

        # self.starData = starProjection.StarData()
        # starX, starY, names = self.starData.getStarPos(0, 0, 1)

        starX = [300, 500, 300, 150, 230]
        starY = [400, 300, 200, 500, 350]
        names = ["1", "2", "3", "4", "5"]

        self.starList = []
        self.generateStarList(names, starX, starY)

        self.connectedStars = []

        self.mouseX = 0
        self.mouseY = 0

    def show(self):
        for i in self.starList:
            i.show()
        if len(self.connectedStars) > 0:
            dots = self.connectedStars.copy()
            dots.append([self.mouseX, self.mouseY])
            pygame.draw.lines(self.canvas, (255, 255, 0), False, dots)

    def mouseClick(self, x, y):
        print("try click")
        for i in self.starList:
            if i.collision(x, y):
                print("hit")
                self.connectedStars.append((i.x + 2, i.y + 2))
                return i.name

    def mouseOver(self, x, y):
        self.mouseX = x
        self.mouseY = y

    def setPlanet(self, planet):
        pass

    def generateStarList(self, names, starX, starY):
        self.starList = []
        for i, name in enumerate(names):
            self.starList.append(star.Star(starX[i], starY[i], 5, self.canvas, name))
