# This program will calculate simple probability and statistics operations

#Author: Hidalgo Pomales

import itertools

def calculatePermutations(list):
    return itertools.permutations(list)



def calculateCombinations(list):
    return itertools.combinations


def calculateAverage(list):
    return (list/len(list));


def calculateMode(list):
        d={}

        # Store the list in a dictionary, if already exists add one to the frequency
        # [ valueOfMode (key) : frequencyOfMode (value) ]
        for i in list:
             try:
                 d[i]+=1
             except:
                 d[i]=1

        valueOfMode= 0
        frequencyOfMode= 0

        # Iterates through the keys to find the biggest value
        # Store the valueOfMode (key) and frequencyOfMode (value)
        modes=[]
        for key in d.keys():
            if d[key] > frequencyOfMode:
                valueOfMode = key
                frequencyOfMode =d[key]

        # Append the mode
        modes.append(("Mode: "+ str(valueOfMode),"Frequency: "+str(frequencyOfMode)))

        #Check if there are more than one mode
        for keyValue in d.keys():
            if d[keyValue]==frequencyOfMode and ("Mode: "+ str(keyValue),"Frequency: "+str(d[keyValue])) not in modes:
                print keyValue
                print d[keyValue]
                modes.append(("Mode: " + str(keyValue), "Frequency: " + str(d[keyValue])))


        return modes



