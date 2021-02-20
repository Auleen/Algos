import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")
def bubbleSort(arr):
	k=len(arr)
	for i in range(k):
		#the outer loop will run at max K times.
		last_index_to_be_checked=(k-1)-i
		#for any i-th iteration(starting from 0),the value of last index to be checked for comparison.
		for j in range(last_index_to_be_checked):
			''' 
			for each loop , pushing the greatest value to the end.
			After each loop the value of last index to be checked 
			reduces by 1 since the greatest values after each iteration are pushed to the end.
			'''
			if arr[j]>arr[j+1]:
				temp=arr[j]
				arr[j]=arr[j+1]
				arr[j+1]=temp
	print(arr)
 
arr=[int(i) for i in input().split()]
arr=bubbleSort(arr)