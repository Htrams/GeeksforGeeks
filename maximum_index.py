# https://practice.geeksforgeeks.org/problems/maximum-index/0
# Given an array A[] of N positive integers. The task is to find the maximum of j - i subjected to the constraint of A[i] <= A[j].

noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    noOfElements=int(input())
    arr=[int(i) for i in input().split()]
    maxIndexDiff=0
    i=0
    while noOfElements - i - 1>maxIndexDiff:
        j=noOfElements-1
        while arr[j]<arr[i] or i==j:
            j=j-1
        if j-i > maxIndexDiff:
            maxIndexDiff=j-i
        i=i+1
    print(maxIndexDiff)