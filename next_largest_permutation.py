# My Rating = 4
# https://practice.geeksforgeeks.org/problems/next-permutation/0
# Implement the next permutation, which rearranges numbers into the numerically next greater permutation of 
# numbers. If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted 
# in an ascending order.

#code
import math
n=int(input())
for testCase in range(n):
    arrLen = int(input())
    arr = [int(i) for i in input().split()]
    maxValue=0
    for i in range(arrLen-1,-1,-1):
        if arr[i] > maxValue:
            maxValue=arr[i]
            continue
        minValue=math.inf
        for j in range(i+1,arrLen):
            if arr[j]>arr[i] and arr[j]<minValue:
                minValue=arr[j]
                minIndex=j
        temp=arr[minIndex]
        del arr[minIndex]
        arr = arr[:i] + [temp] + sorted(arr[i:])
        break
    for i in arr:
        print(i,end=" ")
    print()