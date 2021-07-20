# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 10:04:24 2021

@author: RP
"""

import random

def generate_random_coordinate(min_lat=-90,max_lat=90,min_lon=-180,max_lon=180,precision=6,seed=None):
    
    """Generate a random coordinate of defined precision within bounds.
    
    Parameters
    ----------
    min_lat : float (optional)
      minimum latitude in decimal degrees
    max_lat : float (optional)
      maximum latitude in decimal degrees
    min_lon : float (optional)
      minimum longitude in decimal degrees
    max_lat : float (optional)
      maximum longitude in decimal degrees
    precision : int (optional)
      number of digits to round to after decimal
    seed : int (optional)
      if set to int, sets random.seed(seed)
      
    Returns
    -------
    coord : tuple
      tuple of form (latitude,longitude)
    """
    
    if(isinstance(seed,int)):
        random.seed(seed)
    
    latitude = round(random.uniform(min_lat,max_lat),precision)
    
    longitude = round(random.uniform(min_lon,max_lon),precision)
    
    coord = (latitude,longitude)
    
    return coord

def generate_random_coordinates(n,min_lat=-90,max_lat=90,min_lon=-180,max_lon=180,precision=6,seed=None):
    
    """Generate a list of n random coordinates of defined precision within bounds.
    
    Parameters
    ----------
    n : int
      number of coordinates to generate
    min_lat : float (optional)
      minimum latitude in decimal degrees
    max_lat : float (optional)
      maximum latitude in decimal degrees
    min_lon : float (optional)
      minimum longitude in decimal degrees
    max_lat : float (optional)
      maximum longitude in decimal degrees
    precision : int (optional)
      number of digits to round to after decimal
    seed : int (optional)
      if set to int, sets random.seed(seed)
      
    Returns
    -------
    coords : list
      list of tuple of form (latitude,longitude)
    """
    
    if(isinstance(seed,int)):
        random.seed(seed)
    
    coords = [generate_random_coordinate(min_lat=min_lat,
                                             max_lat=max_lat,
                                             min_lon=min_lon,
                                             max_lon=max_lon,
                                             precision=precision) for c in range(0,n)]
    
    return coords

def coords_to_lat_lon_lists(coords):
    
    """Converts a list of coordinates in tuple form (latitude,longitude) to a list of latitudes and a list of longitudes.
    
    Parameters
    ----------
    coords : list(tuple)
      a list of coordinates in tuple form (latitude,longitude)
      
    Returns
    -------
    lats : list
      list of latitudes in input order
    lons : list
      list of longitudes in input order
    """
    
    lats = [c[0] for c in coords]
    lons = [c[1] for c in coords]
    
    return lats,lons