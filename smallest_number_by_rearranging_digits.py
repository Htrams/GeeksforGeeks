# My Rating = 2
# https://practice.geeksforgeeks.org/problems/smallest-number-by-rearranging-digits-of-a-given-number/0
# Find the Smallest number (Not leading Zeros) which can be obtained by rearranging the digits of given 
# number.

n=int(input())
for testCase in range(n):
    num=list(input())
    num.sort()
    if num[0]=='0':
        for i in range(1,len(num)):
            if num[i]!='0':
                num[0]=num[i]
                num[i]='0'
                break
    for dig in num:
        print(dig,end="")
    print()



# Code 2 - Runs in O(N) but is slower due to more constants
# n=int(input())
# for testCase in range(n):
#     num=input()
#     rec=[0]*10
#     minDig=10
#     for dig in num:
#         temp=int(dig)
#         rec[temp] += 1
#         if minDig!=1 and temp<minDig and temp:
#             minDig=temp
#     print(minDig,end="")
#     rec[minDig] -= 1
#     for i in range(10):
#         for _ in range(rec[i]):
#             print(i,end="")
#     print()