#Kyrk Verdan 991705716

import random
import time

"""
A program that calculates the average CO2 levels in different buildings. It takes inputs from the user and calculates the average
"""
# This function gets the amount of days and calculates the average CO2 levels from those days
def average():

    y = int(input("Enter the number of days for the readings: "))
    print (y)

    #This asks the user for the CO2 readings based on how many days they input
    while y > 0:
        time.sleep(0.5)
        z = int(input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ". format(y)))
        print (z)
        y-= 1 

average()