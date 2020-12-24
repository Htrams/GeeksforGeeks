# https://practice.geeksforgeeks.org/problems/minimum-deletitions/0
# https://practice.geeksforgeeks.org/problems/longest-palindromic-subsequence/0
# Given a string of S as input. Your task is to write a program to remove or delete minimum number of characters from the string so that the resultant string is palindrome.

# Note: The order of characters in the string should be maintained.

# Input:
# First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. First line of each test case contains a string S.

# Output:
# For each test case, print the deletions required to make the string palindrome.

# Constraints:
# 1<=T<=100
# 1<=length(S)<=10000

noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    S=input()
    Slength=len(S)
    dp={}
    for i in range(0,Slength+1):
        for j in range(0,Slength-i+1):
            # subarray j to j+i-1
            if i==0:
                dp[i,j]=0
            elif i==1:
                dp[i,j]=0
            elif S[j]==S[j+i-1]:
                dp[i,j]=dp[i-2,j+1]
            else:
                dp[i,j]=min(
                    dp[i-1,j]+1,
                    dp[i-1,j+1]+1,
                )
            if i>2:
                del dp[i-3,j]
    print(dp[Slength,0])