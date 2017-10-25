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


################
################
################
# Inputs
changeToGive=int(input("How much change do you need in cents?:  "))

################
################
################
# Computations
numToonies=changeToGive//200
changeToGive%=200
numLoonies=changeToGive//100
changeToGive%=100
numQuarters=changeToGive//25
changeToGive%=25
numDimes=changeToGive//10
changeToGive%=10
numNickles=changeToGive//5
changeToGive%=5
numPennies=changeToGive

################
################
################
# Output
print("{} pennies, {} nickle(s), {} dime(s), {} quarter(s), {} loonie(s), and {} toonie(s)".format(numPennies, numNickles, numDimes, numQuarters, numLoonies, numToonies))

################
################
################
# Terminate
# Program
blah = str(input("Press ENTER to quit."))     # required
