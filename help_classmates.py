# This question was part of a custom geeksforgeeks competition, hence there is no link to the question.
# Professor X wants his students to help each other in the chemistry lab. He suggests that every student should help out a classmate who scored less marks than him in chemistry and whose roll number appears after him. But the students are lazy and they don't want to search too far. They each pick the first roll number after them that fits the criteria. Find the marks of the classmate that each student picks. If a student is unable to find anyone print -1.
# Note: one student may be selected by multiple classmates.

# Input:
# First line of input contains number of testcases T. For each testcase, there will be two lines, first of which contains N denoting the number of students in the class. Second line contains N space separated integers denoting the marks of each student roll number wise.

# Output:
# For each roll number, print the marks of the student he choses to help.

#User function Template for python3

def help_classmate(arr,n):
    # code here
    result=[-1]*n
    currentMax=arr[-1]
    currentMin=arr[-1]
    for i in range(n-2,-1,-1):
        if arr[i]>currentMax:
            currentMax=arr[i]
            result[i]=arr[i+1]
        elif arr[i]<currentMin:
            currentMin=arr[i]
            continue
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                result[i]=arr[j]
                break
    return result



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        
        result = help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()

# } Driver Code Ends