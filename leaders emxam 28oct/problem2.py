# 2) Decimal --> Binary Conversion (2 ქულა)

# Create a program which receives a decimal number and converts it to binary.

# Examples:
# 17 --> 10001
# 15 --> 1111


def D_to_B (num):
    num2 = bin(int(num))[2:] # they sad no bin 😥
    return num2
print(D_to_B(17))

#sulution 2

def B_to_B2 (Dnum):
    Bnum = ""
    while Dnum > 0:
        Bnum = str(Dnum%2) + Bnum
        Dnum //=2
    return Bnum
print(B_to_B2(17))

#niceeeeeeee it work both ways 