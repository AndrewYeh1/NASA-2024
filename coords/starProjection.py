import starData
import planetData


class StarData:
    def __init__(self):
        self.starData = starData.StarData()

    def getStarPos(self):
        #this function should take in star data position and convert it to a 2d plane to render 
        ra = 0
        dec = 0
        w = 180 #x angle
        h = 180 #z angle
        #100 = stars returned
        self.starData.getStarData(ra, dec, w, h, 100)

        #following data types are arrays
        name = self.starData.name
        x = self.starData.x.value
        y = self.starData.y.value
        z = self.starData.z.value

        print(x)
        print(y)
        print(z)
        
        viewX = [] 
        viewY = []

        for i in range(len(self.starData.name)):
            #from earth (0,0,0) coordinates

            #camX is the x position of the star on the screen once projected, and camY is the y position of the screen
            if y[i] > 0:
                camX, camY = planetData.TripleDtoDoubleD(0, 0, 0, x[i], y[i], z[i], 1)
                viewX.append(camX)
                viewY.append(camY)
        
        return viewX, viewY
 
#test condtions:
#starData = StarData()
#x, y = starData.getStarPos()
#print(x)
#print(y)