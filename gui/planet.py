import gui.button


class Planet(gui.button.Button):
    def __init__(self, xIn, yIn, sizeIn, canvasIn, nameIn):
        super().__init__(xIn, yIn, sizeIn, canvasIn)
        self.name = nameIn
