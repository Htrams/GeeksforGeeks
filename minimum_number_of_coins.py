# https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins/0
# Given a value N, total sum you have. You have to make change for Rs. N, and there is infinite supply of each of the denominations in Indian currency, i.e., you have infinite supply of { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000} valued coins/notes, Find the minimum number of coins and/or notes needed to make the change for Rs N.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Each test case consist of an Integer value N denoting the amount to get change for.

# Output:
# Print all the denominations needed to make the change in a separate line.

import math

noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    totalSum=int(input())
    allowedDenominations=[1,2,5,10,20,50,100,200,500,2000]
    dp={}
    dp[0]=[0]
    for i in range(1,totalSum+1):
        currentMin=math.inf
        for denom in allowedDenominations:
            if i-denom<0:
                continue
            if dp[i-denom][0]<currentMin:
                currentMin=dp[i-denom][0]
                currentDenom=denom
        dp[i]=[currentMin+1]+dp[i-currentDenom][1:]+[currentDenom]
    for i in dp[totalSum][1:]:
        print(i,'',end='')
    print()