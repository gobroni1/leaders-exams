#3. Given an array of size n, find the majority element. The majority element is the element that appears more than n // 2 times. You may assume that the array is non-empty and the majority element always exists in the array.
#3. [3, 2, 3] -> 3, [2, 2, 1, 1, 2] -> 2, [1, 1, 1, 1, 1] -> 1

def size_n (ls):
    amount = {}

    n = len(ls)
    for i in ls:
        if i in amount:
            amount[i] += 1
        else:
            amount[i] = 1
        if amount[i] > n//2:
            return i
print(size_n([2, 2, 1, 1, 2]))