# This question was part of a custom geeksforgeeks competition, hence there is no link to the question.
#User function Template for python3
from collections import defaultdict
def checkBounds(i,j):
    global n,m
    if i<n and i>=0 and j<m and j>=0:
        return True
    else:
        return False

def maxCities(grid,n,m):
    # code here
    # returned value will be printed
    cellAdjency=[-2,-1,0,1,2]
    spiritualCities=defaultdict(lambda : None)
    maxCount=0
    if n==1:
        starFlag=0
        dotFlag=0
        for j in range(m):
            if j<m-4+1:
                if grid[0][j]=='*' and grid[0][j+1]=='.' and grid[0][j+2]=='.' and grid[0][j+3]=='*':
                    maxCount=2
                    break
            if grid[0][j]=='*':
                starFlag=1
            elif grid[0][j]=='.':
                dotFlag=1
        if maxCount==0:
            if starFlag==1 and dotFlag==1:
                maxCount=1
            else:
                maxCount=0
        return maxCount
    if m==1:
        starFlag=0
        dotFlag=0
        for i in range(n):
            if i<n-4+1:
                if grid[i][0]=='*' and grid[i+1][0]=='.' and grid[i+2][0]=='.' and grid[i+3][0]=='*':
                    maxCount=2
                    break
            if grid[i][0]=='*':
                starFlag=1
            elif grid[i][0]=='.':
                dotFlag=1
        if maxCount==0:
            if starFlag==1 and dotFlag==1:
                maxCount=1
            else:
                maxCount=0
        return maxCount
    for i in range(n):
        for  j in range(m):
            if grid[i][j]=='*':
                count=0
                alreadyCountedCenter=[]
                verifiedAndChecked=[]
                for row in cellAdjency:
                    for col in cellAdjency:
                        if row==0 and col==0:
                            continue
                        if checkBounds(i+row,j+col):
                            if grid[i+row][j+col]=='*':
                                # Holy
                                continue
                            elif spiritualCities[i+row,j+col]==None:
                                if row!=2 and row!=-2 and col!=-2 and col!=2:
                                    count=count+1
                                    verifiedAndChecked.append((i+row,j+col))
                            elif spiritualCities[i+row,j+col][0]==0:
                                # Spiritual
                                if spiritualCities[(i+row,j+col)][2] not in alreadyCountedCenter:
                                    count=count+spiritualCities[i+row,j+col][1]
                                    alreadyCountedCenter.append(spiritualCities[(i+row,j+col)][2])
                                    verifiedAndChecked=verifiedAndChecked + spiritualCities[(spiritualCities[i+row,j+col][2])][1]
                for k in verifiedAndChecked:
                    spiritualCities[k]=[0,count,(i,j)]
                spiritualCities[i,j]=[1,verifiedAndChecked]

                if count>maxCount:
                    maxCount=count
    return maxCount
                




#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**4)

if __name__=="__main__":
    for _ in range(int(input())):
        n,m = (int(x) for x in input().split())
        
        grid = []
        for _ in range(n):
            grid.append( [ x for x in input().strip() ] )
        
        print( maxCities(grid,n,m) )

# } Driver Code Ends