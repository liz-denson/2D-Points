#######################################################################################################
# Word Search (Grid Class)
# Liz Denson & Caroline Holland
# Last modified on 2023-02-28
#
# An object-oriented program that utilizes a GUI and includes a 2D Point class instantiating randomly
# generated points within a specified coordinate range, and plotting those points on a canvas.
#######################################################################################################

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
        
    # Call X and Y getters and setters through the propery function
    x = property(get_x, set_x)
    y = property(get_y, set_y)
    
    # Calculate the distance between two points and takes another Point as an argument
    def dist(self, other_point):
        # Distance formula to calculate the distance between the two points
        return math.sqrt((self._x - other_point.get_x()) ** 2 + (self._y - other_point.get_y()) ** 2)

    # Calculate the midpoint between two points and takes another Point as an argument
    def midpt(self, other_point):
        # Calculates the average of the X and Y components of the two points
        mid_x = (self._x + other_point.get_x()) / 2.0
        mid_y = (self._y + other_point.get_y()) / 2.0
        # Returns a new Point instance with the midpoint coordinates
        return Point(mid_x, mid_y)

    # Magic method to provide a string representation of the Point instance
    def __str__(self):
        # Returns a string in the format (x,y)
        return "({}, {})".format(self._x, self._y)
        
