import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia
import numpy as np

class StarData:
    def __init__(self):
        self.name = []
        self.year = []
        self.ra = []
        self.dec = []
        self.dist = []
        self.x = []
        self.y = []
        self.z = []

        coord = SkyCoord(ra=280, dec=-60, unit=(u.degree, u.degree), frame='icrs')
        width = u.Quantity(0.1, u.degree)
        height = u.Quantity(0.1, u.degree)
        
        r = Gaia.query_object(coordinate=coord, width=width, height=height)
        
        self.ra = r['ra'].data  # Extract right ascension
        self.dec = r['dec'].data  # Extract declination
        parallax = r['parallax'].data  # Extract parallax for distance calculation

        self.dist = 1 / (parallax * u.mas).to(u.arcsec).value  # Convert mas to arcseconds
        
        # Optionally, calculate the 3D Cartesian coordinates (x, y, z) based on ra, dec, and distance
        self.x = self.dist * u.pc * np.cos(np.radians(self.dec)) * np.cos(np.radians(self.ra))
        self.y = self.dist * u.pc * np.cos(np.radians(self.dec)) * np.sin(np.radians(self.ra))
        self.z = self.dist * u.pc * np.sin(np.radians(self.dec))

    def print_data(self):
        print(f"RA: {self.ra}")
        print(f"DEC: {self.dec}")
        print(f"Distance (pc): {self.dist}")
        print(f"X: {self.x}")
        print(f"Y: {self.y}")
        print(f"Z: {self.z}")

star_data = StarData()
star_data.print_data()
