# https://practice.geeksforgeeks.org/problems/coin-piles/0
# There are N piles of coins each containing  Ai (1<=i<=N) coins.  Now, you have to adjust
# the number of coins in each pile such that for any two pile, if a be the number of coins 
# in first pile and b is the number of coins in second pile then |a-b|<=K. In order to do 
# that you can remove coins from different piles to decrease the number of coins in those 
# piles but you cannot increase the number of coins in a pile by adding more coins. Now, 
# given a value of N and K, along with the sizes of the N different piles you have to tell 
# the minimum number of coins to be removed in order to satisfy the given condition.
# Note: You can also remove a pile by removing all the coins of that pile.

import math
noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    noOfPiles,k=[int(i) for i in input().split()]
    coinsInPile = [int(i) for i in input().split()]
    coinsInPile.sort()
    temp=0
    minCoinsRemoved=math.inf
    tempSum=0
    for j in range(0,noOfPiles):
        cutoffValue = coinsInPile[j] + k
        coinsRemoved=tempSum
        tempSum=tempSum+coinsInPile[j]
        for i in range(j,noOfPiles):
            if coinsInPile[i]>cutoffValue:
                coinsRemoved=coinsRemoved+coinsInPile[i]-cutoffValue
        if coinsRemoved<minCoinsRemoved:
            minCoinsRemoved=coinsRemoved
    print(min(minCoinsRemoved,tempSum))