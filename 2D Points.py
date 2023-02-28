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
import tkinter
import random

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
    
# CoordinateSystem class that inherits from Tkinter's Canvas class
class CoordinateSystem(tk.Canvas):
    # Class varaibles
    # Class variable for the radius of the plotted points
    POINT_RADIUS = 0
    # Class variable for the possible colors of the plotted points
    POINT_COLORS = [ "black", "red", "green", "blue", "cyan", "yellow", "magenta" ]
    # Constructor for the CoordinateSystem class
    def __init__(self, master, width=800, height=800, num_points=5000):
        # Initializes a new canvas with the specified width and height, and white background
        super().__init__(master, width=width, height=height, bg='white')
        # Pack the canvas to fill the entire Tkinter window
        self.pack(fill=tk.BOTH, expand=True)
        # Instance variable for the number of points to plot
        self.num_points = num_points
        
