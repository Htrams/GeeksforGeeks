# https://practice.geeksforgeeks.org/problems/sum-tree/1
# Given a Binary Tree. Check whether it is a Sum Tree or not.
# A Binary Tree is a Sum Tree in which value of each node x is equal to sum of nodes present in its left 
# subtree and right subtree . An empty tree is also a Sum Tree as sum of an empty tree can be considered 
# to be 0. A leaf node is also considered as a Sum Tree.

# Example 1:
# Input:
#     3
#   /   \    
#  1     2
# Output: 1
# Explanation: The given tree is a sum 
# tree so return a boolean true.

# Example 2:
# Input:
#           10
#         /    \
#       20      30
#     /   \ 
#    10    10
# Output: 0
# Explanation: The given tree is not a sum
# tree. For the root node, sum of elements
# in left subtree is 40 and sum of elements
# in right subtree is 30. Root element = 10
# which is not equal to 30+40.



'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return True is Tree is SumTree else return False
def isSumTree(root):
    # Code here
    temp=0
    if root.right == None and root.left == None:
        return 1
    if root.left != None:
        if root.left.left == None and root.left.right==None:
            #Leaf Node
            temp=temp+root.left.data
        elif isSumTree(root.left):
            temp=temp+2*root.left.data
        else:
            return 0
    if root.right != None:
        if root.right.left == None and root.right.right==None:
            #Leaf Node
            temp=temp+root.right.data
        elif isSumTree(root.right):
            temp=temp+2*root.right.data
        else:
            return 0
    if root.data==temp:
        return 1
    else:
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        if isSumTree(root):
            print(1) 
        else:
            print(0)
# } Driver Code Ends