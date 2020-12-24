# https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items/0
# Given weights and values related to n items and the maximum capacity allowed for these items. What is the maximum value we can achieve if we can pick any weights any number of times for a total allowed weight of W?

# Input:
# The first line of input contains an integer denoting the number of test cases. Then T test cases follow . Each test case contains two integers N and W denoting the number of items and the total allowed weight. In the next two lines are space separated values of the array denoting values of the items (val[]) and their weights (wt[]) respectively.

# Output:
# For each test case, in a new line, print the  maximum value which we can achieve if we can pick any weights any number of times for a bag of size W.


noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    numberOfItems,maximumWeight=[int(i) for i in input().split()]
    values=[int(i) for i in input().split()]
    weights=[int(i) for i in input().split()]
    dp={}
    for w in range(0,maximumWeight+1):
        if w==0:
            dp[0]=0
            continue
        maxvalue=-1
        maxvalueindex=-1
        for i in range(0,numberOfItems):
            if w-weights[i]<0:
                continue
            if dp[w-weights[i]]+values[i]>maxvalue:
                maxvalue=dp[w-weights[i]]+values[i]
                maxvalueindex=i
        if maxvalue==-1:
            dp[w]=dp[w-1]
        else:
            dp[w]=dp[w-weights[maxvalueindex]]+values[maxvalueindex]
    print(dp)
    print(dp[maximumWeight])