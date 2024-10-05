import openpyxl


class PlanetData:
    name = []
    year = []
    ra = []
    dec = []
    dist = []
    x = []
    y = []
    z = []

    def __init__(self, file):
        dataFrame = openpyxl.load_workbook(file).active

        for row in range(1, dataFrame.max_row):
            for idx, col in enumerate(dataFrame.iter_cols(1, dataFrame.max_column)):
                if idx == 0:
                    self.name.append(col[row].value)
                elif idx == 1:
                    self.year.append(col[row].value)
                elif idx == 2:
                    self.ra.append(col[row].value)
                elif idx == 3:
                    self.dec.append(col[row].value)
                elif idx == 4:
                    self.dist.append(col[row].value)
        print(self.name)
        print(self.year)
        print(self.ra)
        print(self.dec)
        print(self.dist)

    #function turns star coordinates into 2d plane as if you were looking up at stars from planet (north/south pole)
    #dist star is from new planet to star
    def projectTo2D(distStarX, distStarY, distStarZ, planetX, planetY, planetZ, directionFacing):
        

        xPos = 1
        yPos = 2
        return [xPos, yPos]