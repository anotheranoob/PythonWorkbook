"""
Name:  Charlie Brown, Period 9
Program:  Page 999, Program 999

This program calculates the area of
a field.

1.  Significant constants:
    ACRES_IN_FEET=1/413560

2.  Imports:

3.  The inputs are:
    width
    length

3.  Computations:
    area=width*length*FEET_IN_ACRE

4.  The outputs are:
    area

"""

################
################
################
# Significant
# constants
ACRES_IN_FEET=1/43560

################
################
################
# Imports

################
################
################
# Inputs
width=int(input("What is the width of the field in feet?:  "))
length=int(input("What is the length of the field in feet?:  "))

################
################
################
# Computations
area=width*length*ACRES_IN_FEET

################
################
################
# Output
print("The area of the field in acres is {}".format(area))

################
################
################
# Terminate
# Program
print()
print()
print("-" * 50)

print("Name:  Kevin Wu, Period 6, Roster 23")
print("Program:  p6 r23 wu kevin exer 004.py")

blah = input("Press ENTER to quit.")   		  # required
