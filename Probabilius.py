# This program will calculate simple probability and statistics operations

#Author: Hidalgo Pomales

import itertools

def calculatePermutations(list):
    return itertools.permutations(list)



def calculateCombinations(list):
    return itertools.combinations


def calculateAverage(list):
    return (sum(list)/len(list));


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
                modes.append(("Mode: " + str(keyValue), "Frequency: " + str(d[keyValue])))


        return modes



def calculateMedian(list):
    sortedList= sorted(list)
    listLength =len(list)
    midIndex =(listLength-1)/2

    # If the list is empty, then there is no median
    if( listLength< 1):
        return None

    # If the length of the list is odd, then return the number in the middle
    if(listLength % 2==1):
        return sortedList[midIndex]

    # If the length of the list even, then return the average of the numbers in the middle
    else:
        return((sortedList[midIndex]+sortedList[midIndex+1])/2.0)


def calculateUnion(list1,list2):
    tempList = []

    # Find which one is the bigger list
    if (len(list1) < len(list2)):
        short = list1
        bigger = list2
    else:
        short = list2
        bigger = list1

    # Iterate through the small one
    for element in short:
        tempList.append(element)

    # Iterate through the bigger one and add items that doesnt exist in the list
    for element in bigger:
        if element not in tempList:
            tempList.append(element)

    return tempList


def calculateIntersection(list1,list2):

    tempList =[]

    # If they have the same length, there we can iterate using just one loop
    if (len(list1) == len(list2)):
        for element in list1 and list2:
            if element in list1 and list2:
                tempList.append(element)

    # If not, then we need to find the bigger one to avoid exceptions
    else:
         if len(list1) > len(list2):
             bigger= list1
             smaller = list2
         else:
            bigger=list2
            smaller = list1

    # Since the intersections needs to be in both of the list we just go through the smaller one
    # because everything after the size of the smaller one, can not be an intersection.
         for element in smaller:
             if element in bigger:
                 if element not in tempList:
                    tempList.append(element)
    return tempList


def calculateComplement(list1, list2):
    tempList = []

    # If they have the same length, there we can iterate using just one loop
    if (len(list1) == len(list2)):
        for element,element2 in zip(list1,list2):
                if element not in list2 and element2 not in list1:
                    if element not in tempList:
                        tempList.append(element)
                    if element2 not in tempList:
                        tempList.append(element2)


    # If not, then we need to find the bigger one to avoid exceptions
    else:
        if len(list1) > len(list2):
            bigger = list1
            smaller = list2
        else:
            bigger = list2
            smaller = list1

        # Since the complements needs to be in one list and not in the other, we go through the smaller one
        # first to avoid exceptions.
        for element in smaller:
            if element not in bigger:
                if element not in tempList:
                    tempList.append(element)

        # Add the rest of the items that are not in the smaller one.
        for element2 in bigger:
                if element2 not in smaller:
                    if element2 not in tempList:
                        tempList.append(element2)
    return tempList



