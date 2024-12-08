def xbonacci (x, n):
    result = x[:]
    for i in range(len(x),n):
        result.append(sum(result[i - len(x):i]))
    return result
print(xbonacci([1,1,2], 10))