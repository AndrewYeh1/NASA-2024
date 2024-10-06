import openpyxl
import numpy as np

print (PlanetData.TripleDtoDoubleD(1,2,3,3,2,1))


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

    def TripleDtoDoubleD(x, y, z, StarX, StarY, StarZ): 

        #arrays of star and exoplanet position
        positionStar = np.array([StarX, StarY, StarZ])
        cameraPosition = np.array([x, y, z])

        #unitvector point straight ahead from origin (camera position/exoplanet position)
        #and its magnitude
        unitvecY = np.array([x,y+1,z])
        unitvecYMag = np.linalg.norm(unitvecY)

        #field of views in vertical and horizontal direction
        FOVz = 130/2
        FOVx = 200/2

        #width and height of screen (set to 1920x1080)
        widthX = 1920/2
        heightY = 1080/2

        #vector from exoplanet to star & magnitude of the vector 
        distanceVec = positionStar - cameraPosition
        distanceMag = np.linalg.norm(distanceVec)

        dVecX = distanceVec
        dVecZ = distanceVec 
        
        #vectors in x-y plane to find angle with unit vector 
        dVecX[2] = z
        dVecZ[0] = x

        #take the magnitudes of the vectors 
        dVecXMag = np.linalg.norm(dVecX)
        dVecZMag = np.linalg.norm(dVecZ)

        #Find the horizontal angle 
        inside1 = np.dot(unitvecY, dVecX) / (dVecXMag*unitvecYMag)
        angleX = np.acos(inside1)

        #Find the vertical angle 
        inside2 = np.dot(unitvecY, dVecZ) / (dVecZMag*unitvecYMag)
        angleZ = np.acos(inside2) 

        #Find the coords on the screen based on the angle fraction 
        fracX = angleX / FOVx
        fracZ = angleZ / FOVz
        
        #coords on the plane! 
        xCoord = fracX*widthX
        yCoord = fracZ*heightY


        return xCoord, yCoord 








        



