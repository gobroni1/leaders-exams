#1. Given an array containing n-1 numbers taken from the range 1 to n, write a function to find the missing number. There are no duplicates in the array.
#1. [1, 2, 4, 5] -> 3, [1] -> 2, [2, 3, 1, 5] -> 4


def missing (arr):
    if len(arr) == 1:
        return [arr[0] +1 ]
    ls = []
    fm = min(arr)
    to = max(arr) + 1
    for i in range(fm, to):
        ls.append(i)
    return [i for i in ls if i not in arr]
print(missing([1]))