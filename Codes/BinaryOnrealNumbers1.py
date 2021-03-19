def findX(c):
	'''
	x^2 + x^1/2=c
	'''
	lo=0.0
	hi=c
	counter=0
	ans=0.0
	while lo<=hi:
		counter+=0
		mid=lo+(hi-lo)/2
		val=(mid**2.0 + mid**0.5)
		if val==c:
			ans=mid
			break
		elif val>c:
			hi=mid
		else:
			lo=mid
		if counter==100:
			print("infinite Loop")
	return ans

print(findX(15.6))