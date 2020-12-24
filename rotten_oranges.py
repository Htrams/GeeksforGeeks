# My Rating = 6
# https://practice.geeksforgeeks.org/problems/rotten-oranges/0

from collections import deque

def valAtLoc(row,col):
    global mat,r,c
    if row>=r or col>=c or row<0 or col<0:
        return 0
    return mat[row*c + col]

n = int(input())
for testCase in range(n):
    r,c = [int(i) for i in input().split()]
    mat = [int(i) for i in input().split()]
    
    frontier = deque()
    level = {}
    for i in range(r):
        for j in range(c):
            if valAtLoc(i,j)==2:
                frontier.append((i,j))
                level[i,j]=0
    maxLevel=0
    while frontier:
        currentCellr,currentCellc = frontier.popleft()
        adj=[(currentCellr+1,currentCellc),(currentCellr-1,currentCellc),(currentCellr,currentCellc+1),(currentCellr,currentCellc-1)]
        for ir,ic in adj:
            if (ir,ic) not in level:
                if valAtLoc(ir,ic) == 1:
                    level[ir,ic] = level[currentCellr,currentCellc]+1
                    if level[ir,ic] > maxLevel:
                        maxLevel=level[ir,ic]
                    frontier.append((ir,ic))
                    mat[ir*c + ic] = 2
    
    flag=0
    for i in range(r*c):
        if mat[i]==1:
            print(-1)
            flag=1
            break
    if not flag:
        print(maxLevel)