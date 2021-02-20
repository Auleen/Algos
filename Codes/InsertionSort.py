import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")

def InsertionSort(arr):
	for i in range(1,len(arr)):
		primary_val=arr[i]
		j=i-1
		while j>=0and primary_val<arr[j]:
			'''
			for any i-th index we check the values from the index (i-1)
			to at max 0th index.

			if for any j , arr[j]>key, we shift the list from j onwards
			one place to the right.

			when we get key>arr[j],we insert key at the (j+1)th index and hance get a inserted arr[i]
			in the correct position in the list for that iteration.
			'''
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=primary_val

arr=[int(i) for i in input().split()]
InsertionSort(arr)
print(arr)