# https://practice.geeksforgeeks.org/problems/distinct-occurrences/1
# Given two strings S and T of length n and m respectively. find count of distinct occurrences of T in S as a sub-sequence. 

# Example 1:
# Input:
# S = "banana" , T = "ban"
# Output: 3
# Explanation: There are 3 sub-sequences:
# [ban], [ba n], [b an].

# Your Task:
# You don't need to read input or print anything.Your task is to complete the function subsequenceCount() which
# takes two strings as argument S and T and returns the count of the sub-sequences modulo 109 + 7.

# Your task is to complete this function
# Function should return Integer
def sequenceCount(arr1, arr2):
    # Code here
    str1Length=len(arr1)
    str2Length=len(arr2)
    dp={}
    for i in range(-1,str1Length):
        dp[i,-1]=1
        for j in range(str2Length):
            if i==-1:
                dp[i,j]=0
                continue
            if arr1[i]==arr2[j]:
                dp[i,j]=dp[i-1,j-1]+dp[i-1,j]
            else:
                dp[i,j]=dp[i-1,j]
    return dp[str1Length-1,str2Length-1]%1000000007

#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends