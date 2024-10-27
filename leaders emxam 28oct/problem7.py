# 7) Fibonacci Sequence Generator (4 ქულა)
# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]

pre = [0,1]

def feb (n):
    for i in range(2,n):
        next = pre[i-1] + pre[i -2]
        pre.append(next)
    return pre
print(feb(5)) 