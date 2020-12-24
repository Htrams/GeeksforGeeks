# Not completed code
import heapq
import math
class Node:
    def __init__(self):
        i=None
        j-None


def coord2val(i,j):
    global gridSize
    if i>=0 and i<gridSize and j>=0 and j<gridSize:
        return gridSize*i+j
    else:
        return 0

def dikastra(i,j):
    global matrix,priortyHeap,processed,nodeWeights
    nodeWeights[0]=0
    heapq


noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    gridSize=int(input())
    matrix=[int(i) for i in input().split()]
    processed=[0]*gridSize*gridSize
    nodeWeights=[math.inf]*gridSize*gridSize
    priortyHeap = []
    dikastra(0,0)