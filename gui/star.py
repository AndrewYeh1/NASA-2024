import gui.button


class Star(gui.button.Button):
    def __init__(self, xIn, yIn, sizeIn, canvasIn, nameIn):
        super().__init__(xIn, yIn, sizeIn, canvasIn)
        self.name = nameIn
