def GCD (a, b):
    while b: #stop the loop when b is none (AKA 0)
        a, b = b, a % b #this replacec a with b and b with a % b-ის ნაშთით (for every iteration)
    return a


def LCM (a,b):
    return abs(a * b) // GCD(a,b) #i mean it is the same thing as in the pdf file i just chaged | | with abs because that is used to calculate absolute vaue
