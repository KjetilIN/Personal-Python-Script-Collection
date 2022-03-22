import random
import math

"""
WarGames Script.

This is a script to create a random unit for the wargames project. 
(See Github)
After running this script, you should be able to get a file with random units.

#Version-LOG: 

- 0.0.1: returnes line of unit information 

NB! needs a list of random names as file named "randomName.txt" 

@author Kjetil Indrehus
@version 0.0.1

"""



units = ["Infantry","Commander","Cavalry","Ranged"]

def getRandomHealth():
    """Method that return a random integer between 1 and 100"""
    return random.randint(1,100)

def getRadomName():
    nameNumberIndex = random.randint(1,915) #random index in file
   
    lines = []
    with(open("randomName.txt","r")) as file:
        lines = file.readlines()
        
    return lines[nameNumberIndex]
    
def getRandomUnit():
    return units[random.randint(0,len(units)-1)]

for x in range(100):
    print(getRandomUnit()+","+getRadomName()+","+str(getRandomHealth()))