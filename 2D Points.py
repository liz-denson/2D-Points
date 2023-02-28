###############################################################################
# Word Search (Grid Class)
# Liz Denson & Caroline Holland
# Last modified on 2023-02-28
#
# An object-oriented program that utilizes a GUI and includes a 2D Point class
# instantiating randomly generated points within a specified coordinate range,
# and plotting those points on a canvas.
###############################################################################

# Import libraries
import math

# Point class
class Point:
    # Constructor that initializes a Point with specified values for X and Y
    # Defaults the 0.0 value for both components
    def __init__(self, x=0.0, y=0.0):
    # Instance variables where each component is a floating point value
    self._x = float(x)
    self._y = float(y)
    
    # Getters
    def get_x(self):
        # Accessor for the X component
        return self._x
    
    def get_y(self):
        # Accessor for the Y component
        return self._y
    
    # Setters
    def set_x(self, value):
        # Mutator method for the X component
        self._x = float(value)
        
    def set_y(self, value):
        # Mutator method for the Y component
        self._y = float(value)
        
