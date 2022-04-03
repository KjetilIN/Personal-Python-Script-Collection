import random
import math
from re import A

"""
WarGames Script.

This is a script to create a random unit for the wargames project. 
(See Github)
After running this script, you should be able to get a file with random units.

#Version-LOG: 

- 0.0.1: returnes line of unit information 
- 0.0.2: generate a new army to a file

NB! needs a list of random names as file named "randomName.txt" 

@author Kjetil Indrehus
@version 0.0.1

"""



units = ["Infantry","Commander","Cavalry","Ranged"]

def getRandomHealth():
    """Method that return a random integer between 1 and 100"""
    return random.randint(1,100)

def getRadomName():
    nameNumberIndex = random.randint(1,900) #random index in file
   
    lines = []
    with(open("dummy-data-genrating/randomName.txt","r")) as file:
        lines = file.readlines()
        
    
    return lines[nameNumberIndex].rstrip()
    
def getRandomUnit():
    return str(units[random.randint(0,len(units)-1)])


def createNewUnitFile(amount,name,armyname):
    file = open(name+".csv","w")
    file.write(armyname+","+"\n")

    for x in range(amount):
        line = getRandomUnit()+","+getRadomName()+","+str(getRandomHealth())+"\n"
        file.write(line)

    file.close()


createNewUnitFile(200,"pythonUnit","human")