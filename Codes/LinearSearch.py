import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")
sys.stdout=open("D:\\Py\\OutputBox.txt","w")


def LinearSearch(Arr,target):
	for i in range(len(Arr)):
		if Arr[i]==target:
			return i

	return False

Arr=[int(i) for i in input().split()]
Target=int(input())

if LinearSearch(Arr,Target):
	print("Found at index:",LinearSearch(Arr,Target))
else:
	print("Not Found")