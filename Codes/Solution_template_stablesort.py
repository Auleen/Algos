# you can use this less than comparator operator in the choose_pivot, if you would like
# keep in mind that this is the comparator used in the quick sort implementation given
def lessthan(x, y):
    return x[0] < y[0]

# complete this function
# the return value is wrong, you are to complete this function so that the return value is correct
# arr is a list of tuples where each tuple contains the pair (x, y)
def choose_pivot(arr):
    possible=[]
    values={}
    for i in range(len(arr)):
    	values.setdefault(arr[i][0],[])
    	update=values[arr[i][0]]
    	update.append(i)
    	values[arr[i][0]]=update

    for i in values.values():
    	possible.append(i[0])

    return possible
    	


# ---------------------------- Do not modify code below this line ------------------------------------
n = int(input())
arr_strip = list(map(int, input().split()))
arr = []
for i in range(0, 2*n, 2):
    arr.append((arr_strip[i], arr_strip[i+1]))

candidates = choose_pivot(arr)

print(len(candidates))
print(*candidates)
