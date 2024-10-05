import math

class CoordConversion:
    
    def equaToCart(rightAscension, declination, distance):
        pi = math.pi
        rightAscensionRads = rightAscension*pi/180.0
        declinationRads = declination*pi/180.0
    
        x = distance*math.cos(declinationRads)*math.cos(rightAscensionRads)
        y = distance*math.cos(declinationRads)*math.sin(rightAscensionRads)
        z = distance*math.sin(declinationRads)
    
        return (x,y,z)
    
    