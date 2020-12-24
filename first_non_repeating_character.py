# https://practice.geeksforgeeks.org/problems/non-repeating-character/0
# Given a string S consisting of lowercase Latin Letters. Find the first non repeating character in S.

# Input:
# The first line contains T denoting the number of testcases. Then follows description of testcases.
# Each case begins with a single integer N denoting the length of string. The next line contains the string S.

from collections import defaultdict
from collections import OrderedDict
noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    lengthStr=int(input())
    arr = input()
    record=defaultdict(int)
    poss=OrderedDict()
    for i in range(lengthStr-1,-1,-1):
        if record[arr[i]]==0:
            record[arr[i]]=1
            poss[arr[i]]=True
        elif record[arr[i]]==1:
            record[arr[i]]=2
            del poss[arr[i]]
    temp=list(poss.keys())
    if len(temp)!=0:
        print(list(poss.keys())[-1])
    else:
        print(-1)