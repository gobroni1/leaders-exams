# ls = [7,10,4,3,20,15] #on 3 should retunrn 7

# # def kth_smallest(k, ls):

# k = 3

# ls = sorted(ls)
# print(ls)
# print(ls[k-1])


#^^^^^testing------

def kth_smallest(ls, k):
    ls = sorted(ls) #sort so kth smallest number is number on  k-1 index
    return ls[k-1] #k-1 because indexing starts from zero 

print(kth_smallest([7,10,4,3,20,15], 3))
print(kth_smallest([3, 2, 1, 5, 6, 4], 2))
print(kth_smallest([3, 2, 1, 5, 6, 4], 4))