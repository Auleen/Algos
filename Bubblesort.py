arr=[]
for char in (input("Enter the array elements with space gaps").split(' ')):
	arr.append(int(char))
l=len(arr)
for j in range(0,l):
	for i in range(0,l-j-1):
		if arr[i]>arr[i+1]:
			temp=arr[i]
			arr[i]=arr[i+1]
			arr[i+1]=temp
print("Sorted: ",arr)
