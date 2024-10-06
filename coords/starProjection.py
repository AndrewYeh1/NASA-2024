import starData


class StarData:
    def __init__(self):
        self.starData = starData.StarData()

    def getStarPos(self, ra, dec, w, h):
        self.starData.getStarData(ra, dec, w, h, 100)

        name = self.starData.name
        x = self.starData.x
        y = self.starData.y
        z = self.starData.z



        x = []
        y = []
        return x, y

    def project(self, x, y, z, ra, dec, dist):
        return x, y
