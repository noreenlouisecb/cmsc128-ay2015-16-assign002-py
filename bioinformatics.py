#!/usr/bin/python

def getHammingDistance(str1, str2):
    if(len(str1) == len(str2) and len(str1) > 0):
        str1.upper(); str2.upper()
        counter = 0;
        for index in range(len(str1)):
            if(str1[index] != str2[index]):
                counter+=1
        return counter
    elif(len(str1) == 0 and len(str) == 0):
        return "String length is zero(0). Invalid."
    else:
        return "Error! Strings are not equal!"
