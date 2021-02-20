
'''
We are given an unsorted list.
We have to return a sorted list.
'''
import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")
sys.stdout=open("D:\\Py\\OutputBox.txt","w")

def MergeLists(alist,blist):
	'''
	For the documentation of the MergeLists() function , refer to the program file
	MergeLists.py
	'''

	clist = [0]*(len(alist)+len(blist))
	i=0
	j=0
	k=0	
	while (i<len(alist) and j<len(blist)) :
		if alist[i]<blist[j]:
			clist[k]=alist[i]
			i+=1			
		else:			
			clist[k]=blist[j]
			j+=1
		k+=1
	while(i<len(alist)):
			clist[k]=alist[i]
			k+=1
			i+=1	
	while(j<len(blist)):
			clist[k]=blist[j]
			k+=1
			j+=1
	return clist

def MergeSort(arr,l,r):
	'''
	
	Our approach is to recursively sort the array.
	We keep on dividing the array into two smaller arrays and sort the smaller arrays.
	Then we merge the two sorted arays to get the final sorted array.

	BASE CASE: An array of length=1 is consider sorted.

	RECURSION TASK: Dividing the larger array into two smaller arrays

	SELF WORK: Merging the two sorted smaller list to form a larger sorted list

	arr-> unsorted array
	l->leftmost index of arr
	r->rightmost index of arr
	
	'''

	if l==r:
		return [arr[l]]
	
	mid=(l+r)//2
	'''
	We define a mid index to help us divide the bigger array into two
	smaller arrays ,wiz. LeftSideArray and RightSideArray.

	left_arr=arr[l:mid] 		(both indices inclusive)
	right_arr=arr[mid+1,r]		(both indices inclusive)

	We go on dividing till we get a array of length 1 i.e both the l and r 
	point at the same index. We return the value at that index as a list.

	When we get the return value at the left_arr and right_arr, we merge the lists
	using the MergeLists() function defined by us to get a larger sorted array.

	The debugging of the program is helpful in giving an insight for the same.
	(UNCOMMENT THE CODE PARTS OF <DEBUG LINES> AND RUN THE PROGRAM)
	'''
	
	# print("left_arr:",arr[l:mid+1])		#<DEBUG LINE>
	# print("right_arr:",arr[mid+1:r+1],"\n")		#<DEBUG LINE>
	left_arr=MergeSort(arr,l,mid)
	right_arr=MergeSort(arr,mid+1,r)
	# print("Arrays to be merged:",left_arr,"+",right_arr)		#<DEBUG LINE>
	output=MergeLists(left_arr,right_arr)
	# print("Merged array:",output,"\n")		#<DEBUG LINE>
	return output

arr=[int(i) for i in input().split()]
l=0
r=len(arr)-1
X=MergeSort(arr,l,r)
print("Final Merged Array:",X)
