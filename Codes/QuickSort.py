import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")
sys.stdout=open("D:\\Py\\OutputBox.txt","w")

from random import randrange
def partition(arr, left, right):
	m = left

	pivot_index = randrange(left, right)
	# we chose the pivot randomly (from left to right)
	pivot = arr[pivot_index]
	
	arr[right], arr[pivot_index] = arr[pivot_index], arr[right]
	#pushing the pivot to the end

	for i in range(left, right):
		if(arr[i] <= pivot):
			arr[i], arr[m] = arr[m], arr[i]
			m += 1
			
	arr[m], arr[right] = arr[right], arr[m]
	# The last index is never achieved,
	#hence manually swap the pivot pushed at the last index to the boundary index m
	return m

def quicksort(arr, left, right):
	if left >= right:
		return

	pivot_index = partition(arr, left, right)
	quicksort(arr, left, pivot_index - 1)
	quicksort(arr, pivot_index+1, right)

	return

arr = list(map(int, input().split()))
n = len(arr)
quicksort(arr, 0, n-1)

print(li)
