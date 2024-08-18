def is_divisible(*args):
    arr = list(args)
    T = 0
    list1 = []
    if len(arr) <= 1:
        return True
    for i in arr:
        if arr[0] % i != 0:
            T += 1
    if T != 0:
        return False
    else:
        return True
print(is_divisible([12,2,5,4]))