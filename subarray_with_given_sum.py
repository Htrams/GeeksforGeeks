# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0
# Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

from collections import defaultdict
noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    prefixSum=defaultdict(lambda : None)
    noOfElements,targetSum=[int(i) for i in input().split()]
    arr=[int(i) for i in input().split()]
    runningSum=0
    ans=-1
    flag=0
    for i in range(noOfElements):
        runningSum=runningSum+arr[i]
        prefixSum[runningSum]=i
        if runningSum==targetSum:
            print('1',i+1)
            flag=1
            break
        if prefixSum[runningSum-targetSum]!=None:
            print(prefixSum[runningSum-targetSum]+2,i+1)
            flag=1
            break
    if flag==0:
        print(-1)