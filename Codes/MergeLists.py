'''
We are given two sorted arrays A,B.
Our task is to merge them to form a larger sorted array C.

'''
import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")
sys.stdout=open("D:\\Py\\OutputBox.txt","w")



def MergeLists(alist,blist):
	'''
	Our modus operandi is simple.
	Since we are given two sorted lists , for each index of new list C,
	We check them minimum of the smallest numbers from both the arrays A and B(i.e the first unchecked element)
	and append it to the the new list.

	We then remove the appended value from the original list and use this resultant list for further
	comparisons

	Eventually we may encounter a situation where one of the two lists A or B might get exhausted
	before the other. Thus we are left with a few elements of one of the sorted lists.
	Since both lists were sorted and we are also appending according to a sorted manner(i.e comparing the minimums),
	hence we can say that these remaining numbers come at the last of the merged list and are already 
	positioned in a correct order(as they are already sorted,as per given to us).

	Hence we append them in the same order without any further comparison.

	This gives us the final sorted merged list

	'''

	

	clist = [0]*(len(alist)+len(blist))
	i=0
	j=0
	k=0

	'''
	Here we define three varaiables to represent the indices of the three lists : alist,blist,clist .

	i->alist
	j->blist
	k->clist

	We will compare alist[i] and blist[j] for the minimum , and insert the value at clist[k].
	After each comparison , we increase the value of that list's index varaible by 1 so that 
	for our practical purpose we can assume a it to be newlist i.e a list with the last appended value removed.
	(here,appended value means the value that was inserted in the clist after comparison)

	We then again compare alist[i],blist[j] and repeat this till one of the two lists get exhausted.

	Irrespective of which array provide the min value, the value of k is increased by 1 after each comparison
	to point to the next index of the clist where value has to be inserted.

	'''
	


	
	while (i<len(alist) and j<len(blist)) :
		'''
		Condition specified to check if any list in exhausted i.e all values have been compared.
		The value of i or j will become equal to the len(list) after checking the last index.
		Hence loop will stop there.
		'''
		# checking the minimum of the two.		
		if alist[i]<blist[j]:
			# when alist[i] is < blist[j] , insterting the value at clist[k]
			clist[k]=alist[i]
			i+=1
			
		else:
			# when alist[i] is >= blist[j], insterting the value at clist[k]
			clist[k]=blist[j]
			j+=1
		
		print("Value inserted:",clist[k],"i=",i,"j=",j)
		k+=1




	'''
	Appending the remaining values from the unexhausted list.
	Accordingly the loops will run or not.
	(i.e, if i=len(alist) already then it is exhausted as per our convention.And so the first loop won't run according
	to the specified condition.) 
	'''
	while(i<len(alist)):
			clist[k]=alist[i]
			print("Value inserted:",clist[k],"i=",i,"j=",j)
			k+=1
			i+=1
	
	while(j<len(blist)):
			clist[k]=blist[j]
			print("Value inserted:",clist[k],"i=",i,"j=",j)
			k+=1
			j+=1


	return clist


A=[int(i) for i in input().split()]
#inputing the first sorted list
B=[int(i) for i in input().split()]
#inputing the second sorted list

C=MergeLists(A,B)
#the merged lists

print(C)
