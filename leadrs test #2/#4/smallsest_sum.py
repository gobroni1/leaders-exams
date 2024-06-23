def min_sum(arr):

    arr = sorted(arr)
    L = len(arr)
    N=[]
    for i in range (L-1):
        if i != L:
           N.append(arr[i] + arr[L])
    sum = 0
    for i in N:
        sum = sum + i
        return sum
    

