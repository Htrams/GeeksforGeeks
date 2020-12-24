# https://practice.geeksforgeeks.org/problems/number-of-unique-paths/0
# Given a M X N matrix with your initial position at the top-left cell, find the number of possible unique paths to reach the bottom-right cell of the matrix from the initial position.

# Note: Possible moves can be either down or right at any point in time, i.e., we can move to matrix[i+1][j] or matrix[i][j+1] from matrix[i][j].

# Input:
# The first line contains an integer T, depicting the total number of test cases. Then following T lines contain two integers M and N depicting the size of the grid.

# Output:
# Print the number of unique paths to reach the bottom-right cell from the top-left cell.

# Expected Time Complexity: O(M*N).
# Expected Auxiliary Space: O(M*N).

noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    m,n = [int(i) for i in input().split()]
    dp={}
    for i in range(m,0,-1):
        for j in range(n,0,-1):
            if i==m and j==n:
                dp[(i,j)]=1
            elif i==m:
                dp[(i,j)]=dp[(i,j+1)]
            elif j==n:
                dp[(i,j)]=dp[(i+1,j)]
            else:
                dp[(i,j)]=dp[(i+1,j)]+dp[(i,j+1)]
    print(dp[(1,1)])