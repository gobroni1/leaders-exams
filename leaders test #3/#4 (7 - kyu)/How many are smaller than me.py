def smaller(arr):   
    arr2 = [0] * len(arr)
    the_len = len(arr)
    for i in range(the_len):
        count = 0
        for x in range(i+1,the_len):
            if arr[x] < arr[i]:
                count += 1
        arr2[i] = count
    return arr2
#gobroni