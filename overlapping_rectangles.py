# GeeksforGeeks test case checker is wrong.

noOfTestCases = int(input())
for testcase in range(noOfTestCases):
    tx1,ty1,bx1,by1 = [int(i) for i in input().split()]
    xmin1=min(tx1,bx1)
    xmax1=max(tx1,bx1)
    ymin1=min(ty1,by1)
    ymax1=max(ty1,by1)
    temp1=[(tx1,ty1),(bx1,by1),(tx1,by1),(bx1,ty1)]
    tx2,ty2,bx2,by2 = [int(i) for i in input().split()]
    xmin2=min(tx2,bx2)
    xmax2=max(tx2,bx2)
    ymin2=min(ty2,by2)
    ymax2=max(ty2,by2)
    temp2=[(tx2,ty2),(bx2,by2),(tx2,by2),(bx2,ty2)]
    flag=0
    for coord in temp1:
        if coord[0]>=xmin2 and coord[0]<=xmax2 and coord[1]>=ymin2 and coord[1]<=ymax2:
            flag=1
            break
    for coord in temp2:
        if coord[0]>=xmin1 and coord[0]<=xmax1 and coord[1]>=ymin1 and coord[1]<=ymax1:
            flag=1
            break
    if flag:
        print(1)
    else:
        print(0)