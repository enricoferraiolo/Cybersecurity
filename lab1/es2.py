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

print("Multiplicative inverses:")
print(f"17^-1 mod 101 = {mult_inverse(17,101)}")
print(f"357^-1 mod 1234 = {mult_inverse(357,1234)}")
print(f"3125^-1 mod 9987 = {mult_inverse(3125,9987)}")

flag = input("Do you want to insert two numbers to try it out yourself? (y/n): ")
if flag != "y":
    exit()

c=int(input("Insert a: "))
d=int(input("Insert b: "))
print(f"{c}^-1 mod {d} = {mult_inverse(c,d)}")