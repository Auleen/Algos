#the program optimizes the concept of bubble sort so that the total number of loops runned is minimized
arr=[]
for char in (input("Enter the array elements with space gaps \n").split(' ')):
	arr.append(int(char))
l=len(arr)

for j in range(0,l):  
	count=0
	#count is a variable defined to store the 
	#number of iteration in the sub loop where in no swapping is done
	#i.e number of pair comparisons where sorting is already satisfied
	#now i want if the array is completely sorted then the value of count 
	#should reflect it somehow.Inner loop can at max have (l-j-1) cases where
	#the pairs are sorted. therefore for each such case if we increment the value
	#of count by one we will have count=(l-j-1) for a completely sorted array.
	for i in range(0,l-j-1):
		if arr[i]>arr[i+1]:
			temp=arr[i]
			arr[i]=arr[i+1]
			arr[i+1]=temp
		else:
			count+=1
	if count == (l-j-1):
		break
print("Sorted: ",arr,"\nLoops required :",j)
