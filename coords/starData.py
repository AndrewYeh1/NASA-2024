import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia


class StarData:
    name = []
    year = []
    ra = []
    dec = []
    dist = []
    x = []
    y = []
    z = []

    def __init__(self):
        coord = SkyCoord(ra=280, dec=-60, unit=(u.degree, u.degree), frame='icrs')
        width = u.Quantity(0.1, u.degree)
        height = u.Quantity(0.1, u.degree)
        r = Gaia.query_object(coordinate=coord, width=width, height=height)
