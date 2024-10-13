#5. Given an array of integers, find all unique pairs of elements that sum to a given target number.
#5. [1, 2, 3, 2, 4], 5 -> [(1, 4), (2, 3)],    [1, 2, 3], 7 -> [],    [-1, 0, 1, 2, -2, 3], 0 -> [(-1, 1), (-2, 2)]


def u_n (arr, num):
    pr = set()
    s = ()
    
    for i in arr:
        com = num - i
        if com in s:
            pr.add(tuple(sorted((i, com))))
        s.add(i)
    return list(pr)
print(u_n([1, 2, 3, 2, 4], 5))