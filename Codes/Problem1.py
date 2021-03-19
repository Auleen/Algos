"""
You are given a sorted list of numbers and an integer X.
Find the first element in the list >= X.
"""
def findX(arr,x):
	l=0
	r=len(arr)-1
	ans=0
	while r>=l:
		mid=(r+l)//2
		# print(mid,"mid")
		# print(arr[mid],"-->",x)
		if arr[mid]>=x:
			'''
			if arr[mid]>=x then it is poosible to find
			another number to the left of mid which also satisfies the
			condition.

			hence we save the the mid index as prospective answer
			in the variable ans and if we find another nummber 
			satisfying the condition on its left we will
			update ans with the new index.

			hence whenever this conditon is met,we move our 'right'
			index to point at the index (mid-1).
			
			'left'index is left untouched as the lower limit of our search
			can not be still narrowed down
			'''
			ans=mid
			r=mid-1
			continue
		else:
			'''
			if the condintion is false, therefore we mean that arr[mid]<x.
			Hence it is possible for some number at right of mid to satisfy the condition.
			Thus we start from the index (mid+1) and go on till the end of list.
			hence l=arr[mid+1]
			'''
			l=mid+1
		
	print(arr[ans])

arr=list(map(int, input().split()))
x=int(input())
findX(arr,x)