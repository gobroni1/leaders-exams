def two_ls (ls1, ls2):
    ls3 = [] #create list to store numbers to return
    for i in ls1:#iterate over them
        if i in ls2 and i not in ls3: #this is wery easy but I added not in ls3 because test case was returning [1,1]
            ls3.append(i)
    return ls3

print(two_ls([1, 2, 3], [2, 3, 4]))
print(two_ls([1, 1, 2], [1, 3]))
print(two_ls([], [1, 2]))
