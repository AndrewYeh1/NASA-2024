import pygame


class Button:
    def __init__(self, xIn, yIn, sizeIn, canvasIn):
        self.x = xIn
        self.y = yIn
        self.size = sizeIn
        self.canvas = canvasIn

        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

        self.color = (255, 255, 255)

    def show(self):
        pygame.draw.rect(self.canvas, self.color, self.rect)

    def collision(self, xIn, yIn):
        return self.x <= xIn <= self.x + self.size and self.y <= yIn <= self.y + self.size

    def setColor(self, colorIn):
        self.color = colorIn
