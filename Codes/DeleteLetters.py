def check_substring(string,substring):
	check=[]
	index=[]
	for k in substring:
		if k in string:
			check.append(k)
			index.append(string.index(k))
			continue
	intermed_str=''.join(check)
	if intermed_str==substring:
		if index == sorted(index):
			return True


def delete_letters(string,substring,arr):
	for position in arr:
		index=position-1
		for i in range(len(string)):
			if i!=index:
				newstring.append()


