#Not Complete
#User function Template for python3
# design the class in the most optimal way

from collections import defaultdict
from collections import deque

class LRUdata:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class LRUCache:
    def __init__(self,cap):
        # cap:  capacity of cache
        #Intialize all variable
        #code here
        self.cap=cap
        self.elementMap=defaultdict(lambda : None)
        self.elementQueueStart=None
        self.elementQueueEnd=None
    
    def placeAtStart(self,lruData):
        if lruData.left!=None:
            lruData.left.right=lruData.right
        if lruData.right!=None:
            lruData.right.left=lruData.left
        if lruData==self.elementQueueEnd:
            self.elementQueueEnd=lruData.left
        self.elementQueueStart.left=lruData
        lruData.right=self.elementQueueStart
        lruData.left=None
        self.elementQueueStart=lruData
    
    def popLast(self):
        temp=self.elementQueueEnd
        if temp.left!=None:
            temp.left.right=None
            self.elementQueueEnd=temp.left
            del self.elementMap[temp]
            del temp
        else:
            if temp==None:
                print('Nothing to be popped Out')
            else:
                del temp
                del self.elementMap[temp]

    
    #This method works in O(1)
    def get(self, key):
        #code here
        temp=self.elementMap[key]
        if temp != None:
            self.placeAtStart(temp)
            return temp.data
        else:
            return -1
        
    #This method works in O(1)   
    def set(self, key, value):
        #code here
        if self.elementQueueStart==None:
            temp=LRUdata(value)
            self.elementMap[key]=temp
            self.elementQueueStart=temp
            self.elementQueueEnd=temp
            self.cap=self.cap-1
        else:
            temp=self.elementMap[key]
            if temp != None:
                self.placeAtStart(temp)
                temp.data=value
            else:
                temp=LRUdata(value)
                self.placeAtStart(temp)
                self.elementMap[key]=temp
                self.cap=self.cap-1
                if self.cap==-1:
                    self.popLast()
                    self.cap=self.cap+1






#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru=LRUCache(cap)
        
       
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends