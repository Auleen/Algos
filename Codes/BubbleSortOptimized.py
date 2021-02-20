import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")
def bubbleSort(arr):
	k=len(arr)
	swap_flag=False
	for i in range(k):
		#the outer loop will run at max K times.
		for j in range(k-i-1):
			''' for each loop , pushing the greatest value to the end.
			After each loop the value of last index to be checked 
			reduces by 1'''
			if arr[j]>arr[j+1]:
				swap_flag=True
				temp=arr[j]
				arr[j]=arr[j+1]
				arr[j+1]=temp

		# print(arr)
		if swap_flag==False:
			break
		#Breaking the loop at a point if there are no swaps done on the array.That is,the array is sorted.
	return arr,(i+1)
 
arr=[int(i) for i in input().split()]
arr,outer_loop=bubbleSort(arr)
print("Bubble Sorted Arr:",arr)
print("Number of outer loops:",outer_loop)