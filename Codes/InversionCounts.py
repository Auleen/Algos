'''
Let A[0...n - 1] be an array of n distinct positive integers. If i < j and A[i] > A[j] then the pair (i, j) 
is called an inversion of A. 
Given n and an array A your task is to find the number of inversions of A.
'''
import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")

def mergelist(arr,left,right,mid):
	i,count=left,0
	j=mid+1
	output_arr=[]

	while i<=mid and j<=right:
		if arr[i]>arr[j]:
			output_arr.append(arr[j])
			j+=1
			count+=(mid-i+1)
			swap_logsheet.append(i)
		else:
			output_arr.append(arr[i])
			i+=1
	

	while i<=mid :
		output_arr.append(arr[i])
		i+=1
	while j<=right:
		output_arr.append(arr[j])
		j+=1

	k = 0
	for i in range(left, right+1):
		arr[i] = output_arr[k]
		k += 1

	return count


def mergesort(arr,left,right):
	if left==right:
		return 0

	mid=left+(right-left)//2
	leftcount=mergesort(arr,left,mid)
	rightcount=mergesort(arr,mid+1,right)
	mergecount=mergelist(arr,left,right,mid)

	count_sum=leftcount+rightcount+mergecount
	return count_sum


arr=[int(x) for x in input().split()]
swap_logsheet=[]
left=0
right=len(arr)-1
swaps=mergesort(arr,left,right)
print(swaps)