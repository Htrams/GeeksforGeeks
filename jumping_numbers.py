# https://practice.geeksforgeeks.org/problems/jumping-numbers/0
# Given a positive number X. Find all Jumping Numbers smaller than or equal to X. 
# Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

memo=[0,1,2,3,4,5,6,7,8,9]
appendList={0:[1],1:[0,2],2:[1,3],3:[2,4],4:[3,5],5:[4,6],6:[5,7],7:[6,8],8:[7,9],9:[8]}
noOfTestCases=int(input())
for testCase in range(noOfTestCases):
    X=int(input())
    if memo[-1]<X:
        memo=[0,1,2,3,4,5,6,7,8,9]
    i=1
    while memo[-1]<X:
        lastDig=memo[i]%10
        for j in appendList[lastDig]:
            memo.append(memo[i]*10+j)
        i=i+1
    for i in memo:
        if i>X:
            break
        print(i,' ',sep='',end='')
    print()