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

    def getStarData(self, ra, dec, w, h, rows):
        Gaia.ROW_LIMIT = rows

        # Extract the dataset
        coord = SkyCoord(ra=ra, dec=dec, unit=(u.degree, u.degree), frame='icrs')

        maxDistance = 1000  # parsecs

        maxParallax = 1000 / maxDistance

        query = f"""
            SELECT TOP 1000 * 
            FROM gaiadr3.gaia_source
            WHERE DISTANCE(0, 0, ra, dec) < 180
            AND phot_g_mean_mag < 7
        """

        job = Gaia.launch_job_async(query)
        r = job.get_results()

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