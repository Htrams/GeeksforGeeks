# https://practice.geeksforgeeks.org/problems/finding-the-numbers/0
# You are given an array A containing 2*N+2 positive numbers, out of which 2*N numbers exist in pairs whereas the other two number occur exactly once and are distinct. You need to find the other two numbers and print them in ascending order.
from collections import defaultdict

noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    n=int(input())
    tracker=defaultdict(lambda : 0)
    arr=[int(i) for i in input().split()]
    for i in range(2*n+2):
        tracker[arr[i]]=tracker[arr[i]]+1
        if tracker[arr[i]]== 2:
            del tracker[arr[i]]
    num1,num2=tracker.keys()
    if num1>num2:
        print(num2,num1)
    else:
        print(num1,num2)
