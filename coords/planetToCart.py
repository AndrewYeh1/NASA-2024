import math

class CoordConversion:
    
    def equaToCart(rightAscension, declination, distance):
        pi = math.pi
        rightAscensionRads = rightAscension*pi/180.0
        declinationRads = declination*pi/180.0
    
        x = distance*math.cos(declinationRads)*math.cos(rightAscensionRads)
        y = distance*math.cos(declinationRads)*math.sin(rightAscensionRads)
        z = distance*math.sin(declinationRads)
    
        return [x,y,z]
    
    #converts star position from earth to star, to exoplanet to star
    def convertStarPosition(earthToStar, earthToExoplanet):
        exoplanetToStar = earthToStar - earthToExoplanet
        return exoplanetToStar