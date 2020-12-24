# My Rating = 2
# # https://practice.geeksforgeeks.org/problems/row-with-max-1s/0
# Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the 
# first row that has the maximum number of 1's.

class Solution:
    def rowWithMax1s(self,arr, m, n):
	    # n = Cols , m = rows
        maxIndex=n-1
        maxRow=-1
        for i in range(n):
            if arr[0][i] == 1:
                maxIndex=i-1
                maxRow=0
                break
        if maxIndex==-1:
            return 0
        for i in range(1,m):
            while maxIndex>=0 and arr[i][maxIndex]!=0:
                maxIndex -= 1
                maxRow = i
            if maxIndex==-1:
                return i
        return maxRow
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends