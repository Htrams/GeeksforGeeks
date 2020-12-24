# https://practice.geeksforgeeks.org/problems/longest-valid-parentheses/0
# Given a string S consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid parenthesis substring.

from collections import deque
noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    inputStr=input()
    stack=deque()
    preGroupCount=deque()
    maxCount=0
    currentCount=0
    for i in inputStr:
        if i==')':
            if stack and stack.pop() == '(':
                currentCount=currentCount+2+preGroupCount.pop()
                if currentCount>maxCount:
                    maxCount=currentCount
            else:
                stack=deque()
                currentCount=0
        else:
            stack.append(i)
            preGroupCount.append(currentCount)
            currentCount=0
    print(maxCount)