import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")

def find_min_element(arr,start):
	"""
	funtion to find the minimum value from a list 
	starting from its 'start' index to the last index
	"""
	min_val=arr[start]
	index=start
	for j in range(start,len(arr)):
		'''
		running a loop from start index to last index to check for minimum val.
		'''
		if arr[j]<min_val:
			min_val=arr[j]
			index=j
	return index
	'''
	returning the index of the minimum value found
	'''


def SelectionSort(arr):
	for i in range(len(arr)):
		'''
		running the main loop len(arr) times and performing 
		the below tasks repeatedly. 
		'''
		index=find_min_element(arr,i)
		'''
		for each iteration checking the minimum value in the right side portion
		of the list i.e the unsorted region.
		'''
		if index!=i:
			temp=arr[i]
			arr[i]=arr[index]
			arr[index]=temp
		'''
		if a min. value is found , swapping it with the value on our current position 
		,i.e, the i-th index
		'''
	return arr

arr=[int(i) for i in input().split()]
arr=SelectionSort(arr)
print("Sorted Array:",arr)
