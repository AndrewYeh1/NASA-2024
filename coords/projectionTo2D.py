import planetData
import planetToCart

class PlanetProjection:
    def __init__(self):
        self.planetData = planetData.PlanetData()
    
    def project(self):
        viewX = []
        viewY = []
                
        for i in range(len(self.planetData.name)):
            name = planetData.name[i]
            year = planetData.year[i]
            ra = planetData.ra[i]
            dec = planetData.dec[i]
            dist = planetData.dist[i]
            
            x, y, z = planetToCart.equaToCart(ra[i], dec[i], dist[i])
            
            camX, camY = planetData.TripleDtoDoubleD(0, 0, 0, x, y, z)

            viewX.add(camX)
            viewY.add(camY)
            planetZ.add(z)
    


