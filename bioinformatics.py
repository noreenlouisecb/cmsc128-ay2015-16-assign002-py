#!/usr/bin/python
#####################################################
# Author: BUNDOC, Noreen Louise C.                  #
# CMSC 128 AB - 7L                                  #
# Programming Assignment 2(Bioinformatics Library)  #
#####################################################

###
#   This function gets the hamming distance of string 1 and string 2
#   Hamming Distance: number of characters that differ in ith position
#       from position 1 to position len(string1)
#   Parameters: String str1, String str2
#   Return:     the hamming distance
###
def getHammingDistance(str1, str2):
    # str1 and str2 of same length wherein the length is greater than 0
    if(len(str1) == len(str2) and len(str1) > 0):
        counter = 0;
        # traverse each letter in str1
        for index in range(len(str1)):
            # if the letter in str1 is not equal to letter of str2 at certain index
            # then increment counter (the hamming distance)
            if(str1[index] != str2[index]):
                counter+=1
        return counter
    # str1 and str2 length is zero
    elif(len(str1) == 0 and len(str) == 0):
        return "String length is zero(0). Invalid."
    # str1's and str2's length are not equal
    else:
        return "Error! Strings are not equal!"

###
#   This function counts the number of occurrence of pattern in original
#   Parameters: String original, String pattern
#   Return:     number of pattern that exists in original
###
def countSubstrPattern(original, pattern):
    # checks if length of original word is greater than 0
    if(len(original) > 0):
        counter = 0; checker = 0
        # traverse per letter in original word
        for index in range(len(original)):
            # tempindex gets the value of index
            # checker == 0, pattern is found
            # checker == 1, pattern is not found
            tempindex = index; checker = 0
            # traverse per letter in pattern word
            for index2 in range(len(pattern)):
                # checks if tempindex is not equal the word length of original
                if(tempindex != len(original)):
                    # if letter in original is not equal to letter in pattern
                    if(original[tempindex] != pattern[index2]):
                        checker = 1
                        break
                    else:
                        # increment tempindex by 1
                        tempindex+=1
                # if tempindex greater than the word length of original
                else:
                    # pattern not found
                    checker = 1
                    break
            if(checker == 0):
                counter += 1
        return counter
    # if length of original word is not greater than 0
    else:
        return 0

###
#   This function checks if string is valid given the alphabet
#   Parameters: String str, String alphabet
#   Return:     boolean; True if string is valid else False
###
def isValidString(str, alphabet):
    # traverse each letter in str
    for index in range(len(str)):
        # check if letter in str[index] is not in alphabet, return False
        if(str[index] not in alphabet):
            return False
    # if every letter is in the alphabet, return True
    return True

###
#   This function counts the number of Gs minus the number of Cs in the first n nucleotides.
#   Parameters: String str, int n
#   Return:     number of Gs minus number of Cs in first n nucleotides
###
def getSkew(str, n):
    # checks if length of str is greater than 0
    # checks if length of str is greater than or equal to n
    # checks if n is greater than or equal to 0
    if(len(str) > 0 and len(str) >= n and n > 0):
        gCount = 0
        cCount = 0
        # traverse per letter in a genome str
        for index in range(0, n):
            # if letter is G, increment gCount
            if(str[index] == "G"):
                gCount += 1
            # if letter is C, increment cCount
            elif(str[index] == "C"):
                cCount += 1
        # after traversing, return gCount - cCount
        return gCount - cCount
    # if n is less than or equal to 0 or n is greater than the length of string
    elif(len(str) <= n or n <= 0):
        return "Invalid n"
    # if string length is less than 0
    else:
        return "Invalid string length"

###
#   This function finds the maximum (number of Gs minus the number of Cs) in the first n nucleotides.
#   Parameters: String str, int n
#   Return:     maximum (number of Gs minus number of Cs) in first n nucleotides
###
def getMaxSkewN(str, n):
    # checks if length of str is greater than 0
    # checks if length of str is greater than or equal to n
    # checks if n is greater than or equal to 0
    if(len(str) > 0 and len(str) >= n and n > 0):
        gCount = 0
        cCount = 0
        gminusc = 0
        # traverse per letter in a genome str
        for index in range(0, n):
            # if letter is G, increment gCount
            if(str[index] == "G"):
                gCount += 1
            # if letter is C, increment cCount
            elif(str[index] == "C"):
                cCount += 1
            # compare previous gminusc to current gminusc, if greater replace previous
            if(index != 0):
                if(gminusc < gCount - cCount):
                    gminusc = gCount - cCount
            else:
                gminusc = gCount - cCount
        # return gminusc
        return gminusc
    # if n is less than or equal to 0 or n is greater than the length of string
    elif(len(str) <= n or n <= 0):
        return "Invalid n"
    # if string length is less than 0
    else:
        return "Invalid string length"

###
#   This function finds the minimum (number of Gs minus the number of Cs) in the first n nucleotides.
#   Parameters: String str, int n
#   Return:     minimum (number of Gs minus number of Cs) in first n nucleotides
###
def getMinSkewN(str, n):
    # checks if length of str is greater than 0
    # checks if length of str is greater than or equal to n
    # checks if n is greater than or equal to 0
    if(len(str) > 0 and len(str) >= n and n > 0):
        cCount = 0
        gminusc = 0
        gCount = 0
        # traverse per letter in a genome str
        for index in range(0, n):
            # if letter is G, increment gCount
            if(str[index] == "G"):
                gCount += 1
            # if letter is C, increment cCount
            elif(str[index] == "C"):
                cCount += 1
            # compare previous gminusc to current gminusc, if less than, replace previous
            if(index != 0):
                if(gminusc > gCount - cCount):
                    gminusc = gCount - cCount
            else:
                gminusc = gCount - cCount
        # return gminusc
        return gminusc
    # if n is less than or equal to 0 or n is greater than the length of string
    elif(len(str) <= n or n <= 0):
        return "Invalid n"
    # if string length is less than 0
    else:
        return "Invalid string length"
