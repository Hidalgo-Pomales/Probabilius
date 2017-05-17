# This program will calculate simple probability and statistics operations

#Author: Hidalgo Pomales

import itertools
import math
from collections import deque

def calculatePermutations(list1):
    return list(itertools.permutations(list1))

# def calculateCircularPermutations(list1):
#     normalPerm = calculatePermutations(list1[:len(list1)-1])
#     resultList = []
#     for item in normalPerm:
#         tuple = []
#         for i in range(0, len(item)):
#             tuple.append(item[i])
#         tuple.append(len(list1))
#         resultList.append(tuple)
#     return resultList

def calculateCircularPermutations(list1):
    return math.factorial(list1.pop() - 1)

def calculatePartialPermutations(list1):
    return math.factorial(list1[0])/math.factorial(list1[0] - list1[1])

def calculateCombinations(list1):
    tempList=[]
    for i in range(1, len(list1) + 1):
       tempList=tempList+ (list(itertools.combinations(list1, i)))
    return tempList

def rotate(list1, n):
    return list1[n:] + list1[:n]


def calculateAverage(list):
    return float((sum(list)/len(list)))


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
    midIndex =(listLength-1)//2

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



def calculateVariance(list):

    # Calculate the mean or average of the list
    mean = calculateAverage(list)
    sum =0

    # For each element of the list substract to the number the mean and square the result
    for element in list:
        number = pow((element-mean),2)
        sum += number

    return (float(sum)/len(list))


def calculateStandardDeviation(list):

    # Calculate the variance.
    variance = calculateVariance(list)

    # Get the square root, and present only 4 decimal places.
    return format(math.sqrt(variance),'.4f')

def calculateTrimmedMean(list):

    #Sort the list.
    sortedList = sorted(list)[1:-1]

    # get the trimmed mean
    return sum(sortedList) / len(sortedList)


def CalculateMax(list):
    max = list[0]
    #iterate to find the max number
    for i in list[1:]:
        if i > max:
            max = i
    #return the max number
    return max


def CalculateMin(list):
    min = list[0]

    #iterate to find the min
    for i in list[1:]:
        if i < min:
            min = i
    # return the min
    return min

def CalculateRange(list):
        #use the max and min functions
	    return CalculateMax(list) - CalculateMin(list)

def CalculateProbabilities(number1,number2):
    x = max(randint(1,number1) for _ in range(number1+2))
    return x;
