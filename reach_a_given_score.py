# https://practice.geeksforgeeks.org/problems/reach-a-given-score/0
# Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find the number of distinct combinations to reach the given score.

# Input:
# The first line of input contains an integer T denoting the number of test cases. T test cases follow. The first line of each test case is n.

# Output:
# For each testcase, in a new line, print the number of ways/combinations to reach the given score.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).

# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ n ≤ 1000

noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    target=int(input())
    dp=[0]*1001
    dp[0]=1
    for i in range(3,target+1):
        dp[i]=dp[i]+dp[i-3]
    for i in range(5,target+1):
        dp[i]=dp[i]+dp[i-5]
    for i in range(10,target+1):
        dp[i]=dp[i]+dp[i-10]
    print(dp[target])