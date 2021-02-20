import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")
sys.stdout=open("D:\\Py\\OutputBox.txt","w")

def prefixsum(n,val):
	return n+val

def countingSort(arr):
	n=len(arr)
	frequency_list=[0]*(max(arr)+1)
	
	#noting the frequency of each number in arr list.
	for elem in arr:
		frequency_list[elem]+=1
	
	
	#calculating the prefix sums for the elements
	for i in range(1,len(frequency_list)):
		frequency_list[i]=frequency_list[i]+frequency_list[i-1]
	

	'''
	The basic idea of using prefix sums is to maintain stability of the code.
	Suppose you have an array = [1,2,1,9,0,1]
								

	Now,the frequency chart will be [0,3,1,0,0,0,0,0,1]

	We define the prefix sums [0,3,4,4,4,4,4,4,4,4,5]

	for the values present in the arr, their corresponding prefix sum tells the position
	of the last such value in the list.

	e.g prefix sum of 1 is 3. therefore the last '1' from the original arr will be at the position 3 in 
	the sorted list. Similarly, the last '2' in the original arr takes the position 4 in the sorted list
	'''

	#appending values ino the sorted array
	sorted_arr=[0]*n
	last_index_arr=len(arr)-1
	for i in range(last_index_arr,-1,-1):
		k=arr[i]
		position=frequency_list[k]
		index=position-1
		sorted_arr[index]=k
		frequency_list[k]-=1

	'''
	We start checking the values arr from the end as we have to put the last
	occurence of a digit in the position specified by their prefix sum.

	After every aasignment of the value in their position. We decrement the value of their 
	corresponding prefix sum by 1. (This thus gives us the position of the next occurence of that value)
	
	Hence when we encounter another occurence of the same digit,it is put inthe coorect position automatically.	
	'''
	return (sorted_arr)

arr=[int(i) for i in input().split()]
sorted_arr=countingSort(arr)
print(sorted_arr)
