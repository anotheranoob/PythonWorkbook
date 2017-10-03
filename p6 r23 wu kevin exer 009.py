"""
Name:  Wu Kevin, Period 6, Roster 23
Program:  p6 r23 last first exer 009.py

This is replaced with a brief description
of the program's purpose.

1.  Significant constants:
INTEREST_PER_YEAR=0.04

2.  Imports:

3.  The inputs are:
moneyDeposited=int(input("How much money did you deposit?:  "))

4.  Computations:
oneYear=moneyDeposited*(1+INTEREST_PER_YEAR)
twoYear=oneYear*(1+INTEREST_PER_YEAR)
threeYear=twoYear*(1+INTEREST_PER_YEAR)

5.  The outputs are:
oneYear
twoYear
threeYear

"""

################
################
################
# Significant
# constants
INTEREST_PER_YEAR=0.04

################
################
################
# Imports

################
################
################
# Inputs
moneyDeposited=int(input("How much money did you deposit?:  "))

################
################
################
# Computations
oneYear=moneyDeposited*(1+INTEREST_PER_YEAR)
twoYear=oneYear*(1+INTEREST_PER_YEAR)
threeYear=twoYear*(1+INTEREST_PER_YEAR)

################
################
################
# Output
print("After 1 year you will have ${:0.2f}".format(oneYear))
print("After 2 years you will have ${:0.2f}".format(twoYear))
print("After 3 years you will have ${:0.2f}".format(threeYear))

################
################
################
# Terminate
# Program
print()
print()
print("-" * 50)

print("Name:  Wu Kevin, Period 6, Roster 23")
print("Program:  p6 r23 wu kevin exer 009.py")

blah = input("Press ENTER to quit.")


