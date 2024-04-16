"""
Multiplicative inverse and the EXTENDED
EUCLIDEAN ALGORITHM
Compute the following multiplicative inverses:
(a) 17^-1 mod 101
(b) 357^-1 mod 1234
(c) 3125^-1 mod 9987.
"""
def mult_inverse(a,b):
    A = [a]
    B = [b]
    T = [0]
    t = 1
    q = A[0]//B[0]
    r = A[0]-(q*B[0])

    while r > 0:
        tmp = (T[0]-(q*t)) % a
        T[0] = t
        t = tmp
        A[0] = B[0]
        B[0] = r
        q = A[0] // B[0]
        r = A[0] - (q * B[0])
    if B[0] != 1:
        print("b has no inverse modulo a" )
    else:
        return t

a = int(input("Insert first number (17, 357, 3125): "))
b = int(input("Insert second number (101, 1234, 9987): "))
print("Multiplicative inverse:")
print(f"{a}^-1 mod {b} = {mult_inverse(b,a)}")
