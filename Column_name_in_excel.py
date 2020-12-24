# https://practice.geeksforgeeks.org/problems/column-name-from-a-given-column-number/0
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# MS Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, column 1 is named as “A”, column 2 as “B”, column 27 as “AA”.
noOfTestCases = int(input())
for testcase in range(noOfTestCases):
    colNum=int(input())
    alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    quot=colNum
    ans=[]
    while quot!=0:
        ans.append(quot%26-1)
        if quot%26==0:
            quot=quot-1
        quot=quot//26
    for i in range(len(ans)-1,-1,-1):
        print(alphabets[ans[i]],sep='',end='')
    print()
