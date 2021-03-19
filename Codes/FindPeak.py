""""
Given an unsorted list find any element a[i] ,s.t,

a[i-1]<a[i]>a[i+1]

NOTE: Multiple values may be possible. Return any one for simplicity
"""
import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")
sys.stdout=open("D:\\Py\\OutputBox.txt","w")

def isPeak(arr,x):
	return ((arr[x]>arr[x+1]) and (arr[x-1]<arr[x]))

def findPeak(arr):
	'''	
	
	If we try to ananlyse the values of the list vs list indices ,graphically
	we may get a graph consecutive increasing and decreasing slopes.
	
	Now we define a mid value and check if it is on an increasing slope or decreasing slope.
	
	For increasng slope:
		We bring the end value to mid-1 to reduce our search space.
	For Decreasing slope:
		We bring the start value to mid+1 to reduce the search space.

	If mid hits a peak,we return mid.

	Now if now peak is hit during this binary search , it may be possible that the list is sorted
	or has multiple occureneces of equal values.

	These two cases can be handled separately.


	'''
	start=0 
	end=len(arr)-2
	
	while start<=end:
		mid=start+(end-start)//2
		if isPeak(arr,mid):
			return mid
		elif arr[mid+1]>arr[mid]:
			#increasing slope
			start=mid+1
		else:
			#decreasing slope
			end=mid-1

	if arr[len(arr)-1]>arr[len(arr)-2]:
		#i.e the list is increasingly sorted
		return len(arr)-1
	elif arr[0]>arr[1]:
		#i.e the list is decreasingly sorted
		return 0
	else:
		#multiple occureneces of equal values.
		return -1

arr = list(map(int, input().split()))
# print(findPeak.__doc__)
peak_index=findPeak(arr)
if peak_index>=0:
	print("Peak at index:",peak_index,"\nValue:",arr[peak_index])
else:
	print("No peak value found.")