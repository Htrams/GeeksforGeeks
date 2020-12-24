# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
# Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.

noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    senten=input()
    strLen=len(senten)
    lastDot=strLen
    for i in range(strLen-1,-1,-1):
        if senten[i]=='.':
            print(senten[i+1:lastDot],'.',sep='',end='')
            lastDot=i
        elif i==0:
            print(senten[i:lastDot])
