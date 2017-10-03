"""
Name:  Wu Kevin, Period 6
Program:  Python Workbook Ex 006

This program calculates the tax and total cost of a meal.

1.  Significant constants:
    TAX_RATE=0.02
    TIP_RATE=0.18

2.  Imports:

3.  The inputs are:
    costMeal=input("What is the cost of the meal?:  ")

3.  Computations:
    taxAmount=costMeal*TAX_RATE
    tipAmount=costMeal*TIP_RATE
    totalAmount=taxAmount+tipAmount+costMeal

4.  The outputs are:
    taxAmount
    tipAmount
    totalAmount

"""

################
################
################
# Significant
# constants
TAX_RATE=0.02
TIP_RATE=0.18

################
################
################
# Imports

################
################
################
# Inputs
costMeal=int(input("What is the cost of the meal?:  "))

################
################
################
# Computations
taxAmount=costMeal*TAX_RATE
tipAmount=costMeal*TIP_RATE
totalAmount=taxAmount+tipAmount+costMeal

################
################
################
# Output
print("The tax amount is {:0.2f}".format(taxAmount))
print("The tip amount is {:0.2f}".format(tipAmount))
print("The total cost is {:0.2f}".format(totalAmount))

################
################
################
# Terminate
# Program
print()
print()
print("-" * 50)

print("Name:  Kevin Wu, Period 6, Roster 23")
print("Program:  p6 r23 wu kevin exer 006.py")

blah = input("Press ENTER to quit.")


