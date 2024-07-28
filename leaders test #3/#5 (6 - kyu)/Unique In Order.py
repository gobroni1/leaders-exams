def unique_in_order(sequence):
    if not sequence:
        return []
    the_list = [sequence[0]]
    for i in range (1,len(sequence)):
        if sequence[i] != sequence[i-1]:
            the_list.append(sequence[i])
    return the_list
#gobroni