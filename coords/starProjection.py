from . import starData
from . import planetData

class StarData:
    def __init__(self):
        self.starData = starData.StarData()

    def getStarPos(self, ra, dec, hemisphere):
        ra = 0
        dec = 0
        w = 180 #x angle
        h = 180 #z angle
        #100 = stars returned
        self.starData.getStarData(ra, dec, w, h, 100)

        #following data types are arrays
        name = self.starData.name
        x = self.starData.x
        y = self.starData.y
        z = self.starData.z

        viewX = []
        viewY = []
        
        for i in range(len(self.starData.name)):
            #from earth (0,0,0) coordinates
            camX, camY = planetData.TripleDtoDoubleD(0, 0, 0, x[i], y[i], z[i])
            self.viewX.append(camX)
            self.viewY.append(camY)

        return viewX, viewY, name

