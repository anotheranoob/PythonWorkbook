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
LITERS_PER_GALLON=3.785411784
KILOMETERS_PER_MILE=1.609344

################
################
################
# Imports

################
################
################
# Inputs
milesPerGallon=float(input("How many miles per gallon does your car get?:  "))

################
################
################
# Computations
milesPerLiter=milesPerGallon/LITERS_PER_GALLON
kilometersPerLiter=milesPerLiter*KILOMETERS_PER_MILE
litersPer100Km=100/kilometersPerLiter

################
################
################
# Output
print("Your car needs", litersPer100Km, "liters of gas to go 100 km")

################
################
################
# Terminate
# Program
blah = str(input("Press ENTER to quit."))     # required
