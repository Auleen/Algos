import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")

def mergelist(arr,left,right,mid):
	i=left
	j=mid+1
	length=(right-left+1)//2
	'''
	w.r.t the arguments passed in the function:

	|left|.|.|mid|  -X-  |mid+1|.|.|right|    
	 0    1 2  3			4   5 6  7			

	LIST TEAM (LEFT)	  LIST TEAM(RIGHT)
	
	The length of each list can be given by (right-left+1)/2
	
	The lists will always be of even length as th eoriginal list is of of the length of 2^m.

	'''
	count=1
	
	'''
	No. of matches possible(b/w two teams)for two lists of k teams = k^2

	'''

	list1_as_set = set(arr[left:mid+1])
	intersection = list1_as_set.intersection(arr[mid+1:right+1])
	

	intersection_as_list = list(intersection)
	# print(intersection_as_list)
	if len(intersection_as_list)!=0:
		count=0
	

			
	
	return count
	

def mergesort(arr,left,right):
	'''

	Using concept similar to the inversion count problem.

	For a sequence of 2^n numbers we can divide the list into to parts : Left and Right

	We keep on recursively doing the task until we hit a list of size 1.

	We return 0 i.e the number of matches possible in a game with only 1 team.

	Similary we get another 1 size list from the recursion of the other side.

	Now we merge these two list to form a list of size 2.

	Number of games possible = 1

	hence return 1.

	..

	Similarly for two k sized lists , each depicting k teams , the number of matches possible for the teams
	in each list to play against the other list teams is given by k^2. 

	Now while merging we check if there is any team in the two lists which represent the same country.
	Such Match is unprofitable and hence we make the count of profitable matches=0.
	Hence return 0


	'''
	if left==right:
		return 0

	mid=left+(right-left)//2
	leftcount=mergesort(arr,left,mid)
	rightcount=mergesort(arr,mid+1,right)
	mergecount=mergelist(arr,left,right,mid)

	count_sum=leftcount+rightcount+mergecount
	return count_sum


n=int(input())
arr=[int(x) for x in input().split()]
left=0
right=len(arr)-1
swaps=mergesort(arr,left,right)
print(swaps)