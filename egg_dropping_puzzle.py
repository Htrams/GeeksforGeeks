# https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle/0
# You are given K eggs, and you have access to a building with N floors from 1 to N. 
# Each egg is identical in function, and if an egg breaks, you cannot drop it again.
# You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.
# Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 
# Your goal is to know with certainty what the value of F is.
# What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

from collections import defaultdict
import math
noOfTestCases = int(input())
for testcase in range(noOfTestCases):
    totalEggs,totalFloors=[int(i) for i in input().split()]
    dp=defaultdict(int)
    for e in range(1,totalEggs+1):
        dp[e,1]=1
        for j in range(2,totalFloors+1):
            minValue=math.inf
            if e==1:
                dp[e,j]=j
                continue
            for k in range(1,j+1):
                temp = max(
                    dp[e-1,k-1],
                    dp[e,j-k]
                ) + 1
                if temp<minValue:
                    minValue=temp
            dp[e,j]=minValue
    print(dp[totalEggs,totalFloors])