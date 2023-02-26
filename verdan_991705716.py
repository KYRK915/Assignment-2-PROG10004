#Kyrk Verdan 991705716

import random
import time

"""
A program that calculates the average CO2 levels in different buildings. It takes inputs from the user and calculates the average
"""



# This function gets the amount of days and calculates the average CO2 levels from those days
def average():

    y = int(input("Enter the number of days for the readings: "))
    y += 1
    days = 1
    aveList = []

    #This asks the user for the CO2 readings based on how many days they input
    while days != y:
        time.sleep(0.5)
        z = int(input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ". format(days)))

        # This makes sure the input is between 20 and 50
        if z >= 20 and z <= 50:
            aveList.append(z)
        elif z <20 or z >50:
            while z <20 or z >50:
                print ('Wrong Input')
                z = int(input("Enter the C02 for Day {} (Between 20 - 50 PPM) : ". format(days)))
                if z >= 20 and z <= 50:
                    aveList.append(z)
        days += 1

    time.sleep(0.5)     
    print("Rounded Average Readings", sum(aveList)/ len(aveList), 'PPM')



# this function generates the random sensors
def sensorDeploy():

    x = int(input("Enter the number of sensors deployed across Sheridan Campus: "))
    x += 1
    sensor = 1

    while sensor != x:
        time.sleep(0.5)
        print("This is for Sensor", sensor, " at position", '(' + str(random.randint(1,100)) + ',' + str(random.randint(1,100)) + ')' )            
        sensor += 1
        average()
        time.sleep(0.5)
    
    continueProgram()



# this function determines if the user still wants to continue or not
def continueProgram ():
    a = input("Do you want to continue: (Y)es or (N)o: ").upper()

    if a == 'YES' or a == 'Y':
        time.sleep(0.5)
        sensorDeploy()
    
    elif a == 'NO' or a == 'N':
        time.sleep(0.5)
        print ('Exiting Program')

    # Makes sure the input is correct    
    else:
        time.sleep(0.5)
        print('Wrong Input')
        time.sleep(0.5)
        a = input("Do you want to continue: (Y)es or (N)o: ").upper()
        if a == 'YES' or a == 'Y':
            sensorDeploy()
    
        elif a == 'NO' or a == 'N':
            print ('Exiting Program')


sensorDeploy()