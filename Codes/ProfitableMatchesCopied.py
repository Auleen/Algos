import sys
sys.stdin=open("D:\\Py\\INPUTBOX.txt","r")

n = int(input())
teamcode = list(map(int, input().split()))
npfm = 0
li = teamcode[:]

def merge_two_sorted_lists(a, b):
    m = len(a)
    n = len(b)

    global npfm
    npf = False

    output = [0]*(m+n)
    i, j, k = 0, 0, 0

    while i<m and j<n:
        if a[i] == b[j]:
            npf = True
        
        if a[i] < b[j]:
            output[k] = a[i]
            i+=1
            k+=1
        else:
            output[k] = b[j]
            j+=1
            k+=1
    while j<n:
        output[k] = b[j]
        j+= 1
        k+=1
    while i<m:
        output[k] = a[i]
        i += 1
        k+=1
    
    if npf:
        npfm+=1
    return output

def merge_sort(arr, left, right):
    if left == right:
        return [arr[left]]
    mid = (left+right)//2
    left_half = merge_sort(arr, left, mid)
    right_half = merge_sort(arr, mid+1, right)
    
    output = merge_two_sorted_lists(left_half, right_half)
    return output

merge_sort(teamcode, 0, len(teamcode)-1)
print(n-npfm-1)