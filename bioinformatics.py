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

def countSubstrPattern(original, pattern):
    if(len(original) > 0):
        counter = 0; checker = 0
        for index in range(len(original)):
            tempindex = index; checker = 0
            for index2 in range(len(pattern)):
                if(tempindex != len(original)):
                    if(original[tempindex] != pattern[index2]):
                        checker = 1
                        break
                    else:
                        tempindex+=1
                else:
                    checker = 1
                    break
            if(checker == 0):
                counter += 1
        return counter
    else:
        return 0

def isValidString(str, alphabet):
    for index in range(len(str)):
        if(str[index] not in alphabet):
            return False
    return True

def getSkew(str, n):
    if(len(str) > 0 and len(str) >= n and n >= 0):
        gCount = 0
        cCount = 0
        for index in range(0, n):
            if(str[index] == "G"):
                gCount += 1
            elif(str[index] == "C"):
                cCount += 1
        return gCount - cCount
    elif(len(str) <= n or n < 0):
        return "Invalid n"
    else:
        return "Invalid string length"

def getMaxSkewN(str, n):
    if(len(str) > 0 and len(str) >= n and n >= 0):
        gCount = 0
        cCount = 0
        gminusc = 0
        for index in range(0, n):
            if(str[index] == "G"):
                gCount += 1
            elif(str[index] == "C"):
                cCount += 1
            if(index != 0):
                if(gminusc < gCount - cCount):
                    gminusc = gCount - cCount
            else:
                gminusc = gCount - cCount
        return gminusc
    elif(len(str) <= n or n < 0):
        return "Invalid n"
    else:
        return "Invalid string length"

def getMinSkewN(str, n):
    if(len(str) > 0 and len(str) >= n and n >= 0):
        cCount = 0
        gminusc = 0
        gCount = 0
        for index in range(0, n):
            if(str[index] == "G"):
                gCount += 1
            elif(str[index] == "C"):
                cCount += 1
            if(index != 0):
                if(gminusc > gCount - cCount):
                    gminusc = gCount - cCount
            else:
                gminusc = gCount - cCount
        return gminusc
    elif(len(str) <= n or n < 0):
        return "Invalid n"
    else:
        return "Invalid string length"
