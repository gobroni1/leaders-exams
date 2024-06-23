def capitalize(s):
    length = len(s)
    even = []
    odd = []
    for i in range (length):
        if i % 2 == 0 or i ==0:
            even.append(s[i].capitalize())
            odd.append(s[i])
        else:
            odd.append(s[i].capitalize())
            even.append(s[i])
    return [''.join(even), ''.join(odd)]
#gobroni tsitlauri




    
        