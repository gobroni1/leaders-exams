# 3) Remove Duplicates from a List (3 ქულა)
# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']

#მარტივია, list --> set, no dupes!!

def no_dups (ls):
    return list(set(ls))
print(no_dups([1, 2, 2, 3, 4, 4, 5]))

#with set it is not ordered noooooo


def comeon (ls):
    seen =set()
    unq = []
    for i in ls:
        if i not in seen:
            unq.append(i)
            seen.add(i)
    return unq
print(comeon(['a', 'b', 'a', 'c']))