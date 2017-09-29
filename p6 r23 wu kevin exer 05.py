"""
Name:  Kevin Wu, Period 6
Program: Python Workbook Exercize 5

This program calculates the deposits you get from recycling bottles.

1.  Significant constants:
CUTOFF_FOR_PAY=1

2.  Imports:

3.  The inputs are:
smallBottles
largeBottles

3.  Computations:
moneySaved=smallBottles*0.10+largeBottles*0.25

4.  The outputs are:
moneySaved

"""

################
################
################
# Significant
# constants
CUTOFF_FOR_PAY=1

################
################
################
# Imports

################
################
################
# Inputs
smallBottles=int(input("How many bottles are less than {}?:  ".format(CUTOFF_FOR_PAY)))
largeBottles=int(input("How many bottles are greater than {}?:  ".format(CUTOFF_FOR_PAY)))
    

################
################
################
# Computations
moneySaved=smallBottles*0.10+largeBottles*0.25

################
################
################
# Output
print("You saved ${:.2f}".format(moneySaved))

################
################
################
# Terminate
# Program
blah = str(input("Press ENTER to quit."))   		  # required


