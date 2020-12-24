# My Rating =6
# https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1
# Given a Matrix consisting of 0s and 1s. Find the number of islands of connected 1s present in the matrix. 
# Note: A 1 is said to be connected if it has another 1 around it (either of the 8 directions).

import sys
sys.setrecursionlimit(100000)
from collections import deque
def bfs_visit(starting,A,R,C):
    frontier = deque()
    frontier.append(starting)
    while frontier:
        currentCellr,currentCellc = frontier.popleft()
        temp=[-1,0,1]
        for i in temp:
            for j in temp:
                if i==0 and j==0:
                    continue
                elif currentCellr+i>=0 and currentCellr+i<R and currentCellc+j>=0 and currentCellc+j<C:
                    if A[currentCellr+i][currentCellc+j]==1:
                        frontier.append((currentCellr+i,currentCellc+j))
                        A[currentCellr+i][currentCellc+j]=0

def dfs_visit(starting,A,R,C):
    currentCellr,currentCellc = starting
    temp=[-1,0,1]
    for i in temp:
        for j in temp:
            if i==0 and j==0:
                continue
            elif currentCellr+i>=0 and currentCellr+i<R and currentCellc+j>=0 and currentCellc+j<C:
                if A[currentCellr+i][currentCellc+j]==1:
                    A[currentCellr+i][currentCellc+j]=0
                    dfs_visit((currentCellr+i,currentCellc+j),A,R,C)
                    
def findIslands(A, R, C):
    islands = 0
    for i in range(R):
        for j in range(C):
            if A[i][j] == 1:
                islands += 1
                dfs_visit((i,j),A,R,C)
    return islands

#{ 
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,m = map(int,input().strip().split())
        cell_info = list(map(int,input().strip().split()))
        a = []
        k = 0 # current index
        # create the boolean matrix from cell information
        for i in range(n):
            row_i = []
            for j in range(m):
                row_i.append(cell_info[k])
                k+=1
            a.append(row_i)
        print(findIslands(a,n,m))
# } Driver Code Ends