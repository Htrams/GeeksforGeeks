# https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    arrSize=int(input())
    arr=[int(i) for i in input().split()]
    currentMax=arr[0]
    previousSum=arr[0]
    for i in range(1,arrSize):
        previousSum=max(
            previousSum+arr[i],
            arr[i]
        )
        if previousSum>currentMax:
            currentMax=previousSum
    print(currentMax)