#4. Write a function to return the nth number in the Fibonacci sequence. Solve it both recursively and iteratively.
#4. 0 -> 0, 5 -> 5, 10 -> 55




def FN (n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return FN(n-1) + FN(n-2)

print(FN(10))

# secong exp

def FN2 (n):
    if n <=0:
        return 0
    elif n ==1:
        return 1
    x, y = 0, 1
    for _ in range(2, n+1):
        x, y = y, x + y
    return y
print(FN2(10))