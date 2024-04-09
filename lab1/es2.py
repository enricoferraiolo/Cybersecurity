"""
Multiplicative inverse and the EXTENDED
EUCLIDEAN ALGORITHM
Compute the following multiplicative inverses:
(a) 17^−1 mod 101
(b) 357^−1 mod 1234
(c) 3125^−1 mod 9987.
"""

def extended_euclidean_algorithm(a, b):
    A = [a]
    B = [b]
    T = [0]
    t=1
    S = [0]
    q=A[0]//B[0]
    r = A[0] - q*B[0]
    while r>0:
        temp = T[0]-q*t
        s=temp
        T[0]=t
        t=temp
        temp = S[0]-q*s
        S[0]=s
        A[0]=B[0]
        q=A[0]//B[0]
        r=A[0]-q*B[0]
    return (r,s,t)

print("extended_euclidean_algorithm:")
print(extended_euclidean_algorithm(17^-1,101))
print(extended_euclidean_algorithm(357^-1,1234))
print(extended_euclidean_algorithm(3125^-1,9987))
