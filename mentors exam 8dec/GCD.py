# a = 10
# b = 19
# left = 0
# while b:
#     a, b = b, a % b
# print(a) 

#-^^^^^^thinking--------

def GCD (a, b):
    while b: #stop the loop when b is none (AKA 0)
        a, b = b, a % b #this replacec a with b and b with a % b-ის ნაშთით (for every iteration)
    return a

print(GCD(10, 4))