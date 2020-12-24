# https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1
# Given a Binary Search Tree (BST) and a range l-h(inclusive), count the number of nodes in the BST that lie in the given range.

# The values smaller than root go to the left side
# The values greater and equal to the root go to the right side

#User function Template for python3

##Structure of node
'''
# Node Class:
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
'''
##Complete this function
def getCountOfNode(root,l,h):
    # inOrderTraversal
    val=root.data
    count=0
    if val<l:
        if root.right!=None:
            count = count + getCountOfNode(root.right,l,h)
    elif val>h:
        if root.left!=None:
            count = count + getCountOfNode(root.left,l,h)
    else:
        count=count+1
        if root.left!=None:
            count = count + getCountOfNode(root.left,l,h)
        if root.right!=None:
            count = count + getCountOfNode(root.right,l,h)
    return count
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class:
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data)
    else:
        root.right=newNode(root.right,data)
        
    return root
    

    
def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
            
        lr=[int(x) for x in input().strip().split()]

        print(getCountOfNode(root,lr[0],lr[1]))
        testcases-=1

if __name__=="__main__":
    main()
# } Driver Code Ends