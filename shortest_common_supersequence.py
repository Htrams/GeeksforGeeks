# https://practice.geeksforgeeks.org/problems/shortest-common-supersequence/0
# Given two strings str1 and str2, find the length of the smallest string which has both, str1 and str2 as its sub-sequences.
# Note: str1 and str2 can have both uppercase and lowercase letters.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Each test case contains two space-separated strings.

# Output:
# For each testcase, in a new line, output the length of the required string.

noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    str1,str2=input().split()
    slength1=len(str1)-1
    slength2=len(str2)-1
    currentIndex1=0
    currentIndex2=0
    dp={}
    for i in range(-1,slength1+1):
        for j in range(-1,slength2+1):
            if i==-1:
                dp[i,j]=j+1
                continue
            elif j==-1:
                dp[i,j]=i+1
                continue
            if str1[i]==str2[j]:
                dp[i,j]=dp[i-1,j-1]+1
            else:
                dp[i,j]=min(
                    dp[i-1,j]+1,
                    dp[i,j-1]+1
                )
    print(dp[slength1,slength2])