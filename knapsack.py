# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0
# You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
# In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of four lines.
# The first line consists of N the number of items.
# The second line consists of W, the maximum capacity of the knapsack.
# In the next line are N space separated positive integers denoting the values of the N items,
# and in the fourth line are N space separated positive integers denoting the weights of the corresponding items.

# Output:
# For each testcase, in a new line, print the maximum possible value you can get with the given conditions that you can obtain for each test case in a new line.

noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    numberOfItems=int(input())
    maximumWeight=int(input())
    values=[int(i) for i in input().split()]
    weights=[int(i) for i in input().split()]
    dp={}
    for i in range(-1,numberOfItems):
        for j in range(0,maximumWeight+1):
            # prefix = [:i]
            if i==-1:
                dp[i,j]=0
                continue
            elif j>=weights[i]:
                dp[i,j]=max(
                    dp[i-1,j-weights[i]]+values[i],
                    dp[i-1,j]
                )
            else:
                dp[i,j]=dp[i-1,j]
            if i>0:
                del dp[i-2,j]
    print(dp[numberOfItems-1,maximumWeight])