# https://practice.geeksforgeeks.org/problems/count-number-of-hops/0
# A frog jumps either 1, 2 or 3 steps to go to top. In how many ways can it reach the top.

# Input:
# The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains one line of input N denoting the total number of steps.

# Output:
# For each testcase, in a new line, print the number of ways to reach the top.

# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 50

noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    totalSteps=int(input())
    dp={}
    for i in range(0,totalSteps+1):
        if i>2:
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        elif i==2:
            dp[2]=dp[1]+dp[0]
        elif i==1:
            dp[1]=dp[0]
        else:
            dp[0]=1
    print(dp[totalSteps])