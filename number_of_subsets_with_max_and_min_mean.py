# This is code was not accepted. I misunderstood the question and still don't understand it.

# https://practice.geeksforgeeks.org/problems/number-of-subsets-and-mean/0
# Let Max be the maximum possible mean of a multiset of values obtained from an array.
# Let Min be the minimum possible mean of a multiset of values obtained from the same array. Note that in a multiset values may repeat.The task is to find the number of multisets with mean as Max and the number of multisets with mean as Min. The answer may be too large so output the number of multisets modulo 109+7.

from collections import defaultdict
import math
noOfTestCases = int(input())
for testcase in range(noOfTestCases):
    arrSize=int(input())
    arr=[int(i) for i in input().split()]
    prefixSum=defaultdict(lambda : None)
    prefixSum[0]=-1
    maxNum=0
    minNum=math.inf
    noOfMaxMeanSets=0
    noOfMinMeanSets=0
    previousSum=0
    for i in range(arrSize):
        if arr[i]>maxNum:
            maxNum=arr[i]
        if arr[i]<minNum:
            minNum=arr[i]

    for i in range(arrSize):
        previousSum=previousSum+arr[i]
        prefixSum[previousSum]=i
        n=1
        while True:
            maxFind=previousSum-maxNum*n
            if maxFind>=0 and prefixSum[maxFind]!=None and i-prefixSum[maxFind]==n:
                noOfMaxMeanSets=noOfMaxMeanSets+1
            if maxFind<0:
                break
            n=n+1
        n=1
        while True:
            minFind=previousSum-minNum*n
            if minFind>=0 and prefixSum[minFind]!=None and i-prefixSum[minFind]==n:
                noOfMinMeanSets=noOfMinMeanSets+1
            if minFind<0:
                break
            n=n+1
        # while True:
        #     maxFind=previousSum-maxNum*n
        #     minFind=previousSum-minNum*n
        #     if maxFind>=0 and prefixSum[maxFind]!=None and i-prefixSum[maxFind]==n:
        #         noOfMaxMeanSets=noOfMaxMeanSets+1
        #     if minFind and prefixSum[minFind]!=None and i-prefixSum[minFind]==n:
        #         noOfMinMeanSets=noOfMinMeanSets+1
        #     if maxFind<0 and minFind<0:
        #         break
        #     n=n+1
    print(noOfMaxMeanSets%1000000007,noOfMinMeanSets%1000000007)