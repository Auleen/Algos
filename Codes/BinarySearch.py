import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")
# sys.stdout=open("D:\\Py\\OutputBox.txt","w")


def BinarySearch(arr,target):
	#first off all we need to define our search space
	n=len(arr)
	left,right=0,n-1
	ans=0
	while(left<=right):
		#loop runs till left is less than or equal to right,i.e,there are some elements in the search space
		mid=(left+right)//2
		if target==arr[mid]:
			ans+=1
			left=mid+1
		elif arr[mid]<target:
			left=mid+1
		else:
			right=mid-1
	return ans
	#if not found then we will reach this code


def BinarySearchOnRotatedArr(arr,target):
	n=len(arr)
	start=0
	end=n-1
	while start<=end:
		mid = start + (end-start)//2
		# print("Start:",start,":Value",arr[start]) #<DEBUG LINE>
		# print("End:",end,":Value",arr[end])		#<DEBUG LINE>
		# print("\nMid index:",mid,"value:",arr[mid])#<DEBUG LINE>

		if arr[mid]==target:
			return mid
		elif arr[start] <= arr[mid]:
			# print("Case1")	#<DEBUG LINE>
			#case 1:
			if target>=arr[start] and target<arr[mid]:
				end=mid-1
			else:
				start=mid+1

		else:
			#case 2 (i.e,arr[mid]<arr[start])
			# print("Case2")	#<DEBUG LINE>
			if target<=arr[end] and target>arr[mid]:
				start=mid+1
			else:
				end=mid-1
	return False


arr=[int(i) for i in input().split()]
target=int(input())
found_index=BinarySearch(arr,target)
print("Element found at index:",found_index)

