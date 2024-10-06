import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia
import numpy as np


class StarData:

    def __init__(self):

        self.name = []
        self.ra = []
        self.dec = []
        self.dist = []
        self.x = []
        self.y = []
        self.z = []
        
        # Extract the dataset
        coord = SkyCoord(ra=280, dec=-60, unit=(u.degree, u.degree), frame='icrs')
        width = u.Quantity(0.1, u.degree)
        height = u.Quantity(0.1, u.degree)
        r = Gaia.query_object(coordinate=coord, width=width, height=height)
        
        # Extract the data from the result
        self.name = r['DESIGNATION'].data
        self.ra = r['ra'].data  # Extract right ascension
        self.dec = r['dec'].data  # Extract declination
        parallax = r['parallax'].data  # Extract parallax

        # Calculate distance in parsecs from parallax (mas to parsecs)
        self.dist = (1 / parallax) * u.pc  # Automatically handles units conversion

        # Convert RA, DEC from degrees to radians for trig functions
        ra_rad = np.radians(self.ra)
        dec_rad = np.radians(self.dec)

        # Calculate the 3D Cartesian coordinates (x, y, z)
        self.x = (self.dist * np.cos(dec_rad) * np.cos(ra_rad)).to(u.pc)
        self.y = (self.dist * np.cos(dec_rad) * np.sin(ra_rad)).to(u.pc)
        self.z = (self.dist * np.sin(dec_rad)).to(u.pc)

    def print_data(self):
        print(f"Name: {self.name}")
        print(f"RA: {self.ra}")
        print(f"DEC: {self.dec}")
        print(f"Distance (pc): {self.dist}")
        print(f"X: {self.x}")
        print(f"Y: {self.y}")
        print(f"Z: {self.z}")
