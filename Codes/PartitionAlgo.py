"""
You are given a list of integers and a pivot element from the list.
Rearrange the data in the list in such a way that the elements smaller that th pivot element are 
on thne left of it while the larger ones are on the right.

NOTE: Arrangement of elements on both the sides does not matter(i.e not necessarily sorted)  
"""
import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")
sys.stdout=open("D:\\Py\\OutputBox.txt","w")

def partitionAlgo(arr,pivot):
	i=m=0

	'''
	i -> general index to iterate over the list and check the value of i-th element
	m -> partition index, i.e , all the elements to the left of this index are less than the pivot
	'''
	for i in range(len(arr)):
		print("x")
		'''
		For any iteration if the value of i becomes == len(arr),
		It implies that there have been no swaps in between (i.e for that iteration)
		Hence the elements are arranged in the required manner.
		'''
		if arr[i]==pivot:
			print("Pivot value hit","pushing")
			pivot_index=i
			arr[i],arr[len(arr)-1]=arr[len(arr)-1],arr[i]
			print("//",arr)
		'''
		Pushing the pivot element at the end of the list.
		'''
			
		if arr[i]<=pivot:
			'''
			If for any arr[i] , we get it to be less than the pivot,we swap it with the
			value at arr[m].
			After that we shift the boundary index,m, a unit rightwards , i.e, we increase its
			value by 1.
			Also for the next iteration we have to start checking from this m-th index as 
			values to the left of it are already less than pivot (hence setting the i at m)
			'''
			arr[i],arr[m]=arr[m],arr[i]
			print("After Swapping",arr)

			m+=1
			print("M pints to ",arr[m])	
			# continue
			'''
			After a swap occurs we again start the iteration with i initialized at m.
			Hence we do not want to move to the next line: i+=1 for now.
			Thus we use continue to skip the remaining part.
			'''
		# print(arr)
		
	# print(arr)
	# if pivot_index>m:
	print(pivot_index,"PI")
	arr[pivot_index],arr[m]=arr[m],arr[pivot_index]
	'''
	Swapping the pivot element with the element at m-th index(boundary index),if the pivot is on
	the right of the boundary index ,so that we have our pivot on the partition between the left side and right side.
	'''
	print(arr)
	print("loops",i)

Arr=[int(i) for i in input().split()]
pivot=int(input())
partitionAlgo(Arr,pivot)