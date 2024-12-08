from itertools import combinations


def add_zero (ls):
    ls2 = []

    for i in combinations(ls, 3):
        if sum(i) == 0:
            sts = sorted(i)
            if sts not in ls2:
                ls2.append(sts)
    return ls2

print(add_zero([-1, 0, 1, 2, -1, -4]))
print(add_zero([0, 0, 0]))
print(add_zero([1, 2, -2, -1]))


#there is not much to it, i use itertools to make all possible triplets and only filter those that add up to zero