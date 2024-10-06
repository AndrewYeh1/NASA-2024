from . import planetData
from . import planetToCart


class PlanetProjection:
    def __init__(self):
        self.planets = planetData.PlanetData("resources/exoplanets.xlsx")
        self.viewX = []
        self.viewY = []
        self.name = []
    
    def project(self):
        self.viewX = []
        self.viewY = []

        for i in range(len(self.planets.name)):
            self.name = self.planets.name[i]
            year = self.planets.year[i]
            ra = self.planets.ra[i]
            dec = self.planets.dec[i]
            dist = self.planets.dist[i]

            if ra is not None and dec is not None and dist is not None:
                x, y, z = planetToCart.equalToCart(ra, dec, dist)
            
                camX, camY = planetData.TripleDtoDoubleD(0, 0, 0, x, y, z)

                self.viewX.append(camX)
                self.viewY.append(camY)
            else:
                print("no coordinate data for planet")
    


