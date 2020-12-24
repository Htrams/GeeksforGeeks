# https://practice.geeksforgeeks.org/problems/find-largest-word-in-dictionary/0
# Giving a dictionary and a string ‘str’, your task is to find the longest string in dictionary of size x which can be formed by deleting some characters of the given ‘str’.

from collections import defaultdict
noOfTestCases = int(input())
for testcase in range(noOfTestCases):
    noOfStrings = int(input())
    dictionary = input().split()
    targetStr = input()
    targetLen = len(targetStr)
    maxLength=0
    for potStr in dictionary:
        flag=0
        tempLen=len(potStr)
        if tempLen>targetLen:
            continue
        flagged=0
        j=0
        i=0
        while i<tempLen:
            if j==targetLen:
                flagged=1
                break
            if potStr[i]==targetStr[j]:
                j=j+1
                i=i+1
            else:
                j=j+1
        if flagged==0:
            if tempLen>maxLength:
                maxLength=tempLen
                maxLengthStr=potStr
    print(maxLengthStr)