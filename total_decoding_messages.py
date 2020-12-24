# https://practice.geeksforgeeks.org/problems/total-decoding-messages/0
# A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# You are an FBI agent. You have to determine the total number of ways that message can be decoded.
# Note: An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and If there are leading 0’s, extra trailing 0’s and two or more consecutive 0’s then it is an invalid string.

# Example :
# Given encoded message "123",  it could be decoded as "ABC" (1 2 3) or "LC" (12 3) or "AW"(1 23).
# So total ways are 3.

from collections import defaultdict
noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    strLen=int(input())
    arr=[int(i) for i in input()]
    dp=defaultdict(lambda : 1)
    flag=0
    for i in range(strLen):
        temp=0
        if arr[i]>0 and arr[i]<10:
            temp=temp+dp[i-1]
        if i>0 and arr[i-1]!=0 and arr[i-1]*10+arr[i]<27 and arr[i-1]*10+arr[i]>0:
            temp=temp+dp[i-2]
        if temp==0:
            flag=1
            break
        dp[i]=temp
    
    if flag==1:
        print(0)
    else:
        print(dp[strLen-1])