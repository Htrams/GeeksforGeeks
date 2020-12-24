# https://practice.geeksforgeeks.org/problems/gold-mine-problem/0
# Given a gold mine (M) of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down\) that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right. Your task is to find out maximum amount of gold which he can collect.
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer n and m denoting the size of the matrix. Then in the next line are n*m space separated values of the matrix.

# Output:
# For each test case in a new line print an integer denoting the max gold the miner could collect.


def coord2val(i,j):
    global n,m
    return m*i+j
noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    n,m=[int(i) for i in input().split()]
    matrix=[int(i) for i in input().split()]
    dp={}
    for i in range(m-1,-1,-1):
        for j in range(0,n):
            if i==m-1:
                dp[j,i]=matrix[coord2val(j,i)]
                continue
            if j==0 and j==n-1:
                dp[j,i]=dp[j,i+1]+matrix[coord2val(j,i)]
            elif j==0:
                dp[j,i] = max(dp[j,i+1],dp[j+1,i+1]) + matrix[coord2val(j,i)]
            elif j==n-1:
                dp[j,i] = max(dp[j,i+1],dp[j-1,i+1]) + matrix[coord2val(j,i)]
            else:
                dp[j,i] = max(dp[j,i+1],dp[j-1,i+1],dp[j+1,i+1]) + matrix[coord2val(j,i)]
    maxvalue=0
    for i in range(0,n):
        if dp[i,0]>maxvalue:
            maxvalue=dp[i,0]
    print(maxvalue)