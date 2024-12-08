# ls = [0]
# ls2= []
# sum = 0

# if max(ls) == 0:
#     sum +=1
# for i in range(max(ls)+1):
#     ls2.append(i)
# for i in ls2:
#     if i <= 1 and i in ls:
#         sum += 1
#     if i in ls and i-1 in ls:
#         sum += 1  
# print(sum)


def prob8 (ls):
    ls2 = []
    sum =0
    if max(ls) == 0:
        return 1
    for i in range(max(ls)+1):
        ls2.append(i)
    for i in ls2:
        if i <= 1 and i in ls:
            sum += 1
        if i in ls and i-1 in ls:
            sum += 1
    return sum
print(prob8([9, 1, 4, 7, 3, 2, 8, 5, 6]))
print(prob8([0, 0]))
print(prob8([100, 4, 200, 1, 3, 2]))