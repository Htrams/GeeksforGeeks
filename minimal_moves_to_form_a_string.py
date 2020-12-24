# https://practice.geeksforgeeks.org/problems/minimal-moves-to-form-a-string/0
# Given a string S, we need to write a program to check if it is possible to construct the given string S by performing any of the below operations any number of times. In each step, we can:

# Add any character at the end of the string.
# or, append the string to the string itself.
# The above steps can be applied any number of times. We need to print the minimum steps required to form the string.

# Input:
# The first line contains an integer T, the number of test cases. For each test case, there is a string s which we need to form. 
# Output:
# For each test case, the output is an integer displaying the minimum number of steps required to form that string.


noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    targetString=input()
    dp={}
    for i in range(1,len(targetString)+1):
        #Base Case
        if i==1:
            dp[i]=1
        elif i%2==0 and targetString[0:i//2]==targetString[i//2:i]:
            dp[i]=min(dp[i//2],dp[i-1])+1
        else:
            dp[i]=dp[i-1]+1
    print(dp[len(targetString)])