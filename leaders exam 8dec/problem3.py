def missing (ls):
    if len(ls) == 1:
        return 0
    ls2 =[]
    for i in range(min(ls),max(ls)): #create a list that contains all number based on what is the maximum of the first list
        ls2.append(i) 
    for i in ls2:#iterate over the filled list to finde if any number from given list is not in this filled list to return      
        if i not in ls:
            return i

print(missing([2]))
print(missing([3, 5, 6, 1, 2]))
print(missing([1, 2, 4, 5]))