def euclidean_algorithm(a, b):
    r=[a,b]
    q=[]
    m= 1
    while r[m] != 0:
        q.append(r[m-1] // r[m])  # Use integer division to get the quotient
        r.append(r[m-1] - q[m-1] * r[m])  # Append new remainder to the list
        m= m+1
    m=m-1
    return (q,r[m])

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
        return -1
    else:
        return t
        
"""
Computaion of x^c mod n 
"""
def square_and_multiply(x, c, n):
    #convert c from string to list of integers
    c = [int(i) for i in c[2:]]

    c.reverse()
    y = 1
    for i in range(len(c)):
        y = (y**2) % n
        if c[i] == 1:
            y = (y*x) % n
    return y


"""
Greatest Common Divisor (GCD) and the
Euclidean Algorithm
Compute gcd(57, 93) using the Euclidean
algorithm, and find integers s and t such that
57s + 93t = gcd(57, 93).
""" 
print("gcd(57,93):")
print(euclidean_algorithm(57,93))

"""
Multiplicative inverse and the EXTENDED
EUCLIDEAN ALGORITHM
Compute the following multiplicative inverses:
(a) 17^−1 mod 101
(b) 357^−1 mod 1234
(c) 3125^−1 mod 9987.
"""
print("extended_euclidean_algorithm:")
print(extended_euclidean_algorithm(17^-1,101))
print(extended_euclidean_algorithm(357^-1,1234))
print(extended_euclidean_algorithm(3125^-1,9987))



"""
The RSA Cryptosystem: an example
Suppose Bob chooses p = 101 and q = 113. Then n
= 11413 and φ(n) = 100 × 112 = 11200. 
Since 11200 = 2^6*5^2*7, an integer b can be used as an encryption
exponent if and only if b is not divisible by 2, 5, or 7.
(In practice, however, Bob will not factor φ(n). He will
verify that gcd(φ(n), b) = 1 using the Euclidean
Algorithm, slide #7) 
"""
p=101
q=113
n=11413
def phi(p,q):
    return (p-1)*(q-1) 
b = 3533
print("The RSA Cryptosystem: ")
"""
Please verify that gcd(φ(n), b) = 1 using the
Euclidean Algo.
"""
print(euclidean_algorithm(phi(p,q),b))

"""
Now compute Bob’s secret decryption exponent, a,
using the Multiplicative Inverse Algorithm (Algorithm
6.3, at slide #9).
"""
a = mult_inverse(phi(p,q),b)
print(a)
