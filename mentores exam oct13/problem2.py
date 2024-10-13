#2. Write a function to find the longest common prefix among an array of strings. If there is no common prefix, return an empty string.
#2. ["flower", "flow", "flight"] -> "fl", ["dog", "racecar", "car"] -> "", ["apple", "apple", "apple"] -> "apple"
def prefix (st):
    pr = st[0]
    for s in st[1:]:
        while s[:len(pr)] != pr:
            pr = pr[:-1]
            if not pr:
                return ""
    return pr
print(prefix(["flower", "flow", "flight"]))

