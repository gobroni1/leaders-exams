def problem4 (txt):
    indexes = {}
    var = 0
    ret = 0

    for i in range(len(txt)):
        if txt[i] in indexes and indexes[txt[i]] >= var:
            var = indexes[txt[i]] + 1
        indexes[txt[i]] = i
        
        ret = max(ret, i - var +1)
    return ret

print(problem4("abcabcbb"))
print(problem4("bbbbb"))
print(problem4(""))
print(problem4("pwwkew"))
