"""
Name:  Charlie Brown, Period 9
Program:  Page 999, Program 999

This program calculates the area of
rectangle.

1.  Significant constants:


2.  Imports:


3.  The inputs are:


3.  Computations:


4.  The outputs are:


"""

################
################
################
# Significant
# constants

################
################
################
# Imports
from math import *

################
################
################
# Inputs
lat1=float(input("What is the latitude of the first point?:  "))
long1=float(input("What is the longitude of the first point?:  "))
lat2=float(input("What is the latitude of the second point?:  "))
long2=float(input("What is the longitutde of the second point?:  "))

################
################
################
# Computations
distance=6371.01*acos(sin(radians(lat1))*sin(radians(lat2))+cos(radians(lat1))*cos(radians(lat2))*cos(long1-long2))

################
################
################
# Output
print("The distance is:", distance)

################
################
################
# Terminate
# Program
blah = str(input("Press ENTER to quit."))     # required
