from math import *

def pos_sum (ls):
    sum = 0
    for i in ls:
        if i > 0:
            sum += floor(i)
    return sum 

print(pos_sum([1, -4, 7, 12]))
print(pos_sum([-1.5, 2.7, -3.3, 4.8]))
print(pos_sum([-1, -2, -3]))