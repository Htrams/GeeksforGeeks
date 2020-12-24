# https://practice.geeksforgeeks.org/problems/count-of-strings-that-can-be-formed-using-a-b-and-c-under-given-constraints/0

# Given a length n, count the number of strings of length n that can be made using ‘a’, ‘b’ and ‘c’ with at-most one ‘b’ and two ‘c’s allowed.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains an integer N denoting the length of the string.

# Output:
# Output the count of the strings that can be formed under the given constraint.

# Constraints:

# 1<= T <=100
# 1<= N <=1000

bAllowed=1
cAllowed=2
noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    totalLength=int(input())
    dp={}
    for b in range(bAllowed+1):
        for c in range(cAllowed+1):
            dp[(0,b,c)]=0
    dp[(0,0,0)]=1
    for i in range(1,totalLength+1):
        for b in range(bAllowed+1):
            for c in range(cAllowed+1):
                temp=dp[(i-1,b,c)]
                if b>0:
                    temp=temp+dp[(i-1,b-1,c)]
                if c>0:
                    temp=temp+dp[(i-1,b,c-1)]
                dp[(i,b,c)]=temp
    sum=0
    for b in range(bAllowed+1):
        for c in range(cAllowed+1):
            sum=sum+dp[(totalLength,b,c)]
    print(sum)