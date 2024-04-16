
"""
The RSA Cryptosystem: an example
Suppose Bob chooses p = 101 and q = 113. Then n
= 11413 and φ(n) = 100 × 112 = 11200. 
Since 11200 = 2^6*5^2*7, an integer b can be used as an encryption
exponent if and only if b is not divisible by 2, 5, or 7.
(In practice, however, Bob will not factor φ(n). He will
verify that gcd(φ(n), b) = 1 using the Euclidean
Algorithm, slide #7)
Suppose Bob chooses b = 3533.
- Please verify that gcd(φ(n), b) = 1 using the
Euclidean Algo.
- Now compute Bob’s secret decryption exponent, a,
using the Multiplicative Inverse Algorithm (Algorithm
6.3, at slide #9).
Bob publishes n = 11413 and b = 3533 in a directory. 
"""
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
        

def phi(p,q):
    return (p-1)*(q-1) 


#p=101
#q=113
#n=11413

print("insert the values of p, q and n")
p = int(input("p (101): "))
q = int(input("q (113): "))
n = p * q #calcoliamo la public key
print(f"n: {n}")
# b = 3533

b = int(input("b (3533): "))
# print(f"b: {b}")



print("The RSA Cryptosystem")

"""
Please verify that gcd(φ(n), b) = 1 using the
Euclidean Algo.
"""
print(f"gcd(φ(n), b):  {euclidean_algorithm(phi(p,q),b)[1]}")
# print(euclidean_algorithm(phi(p,q),b))
"""
Now compute Bob’s secret decryption exponent, a,
using the Multiplicative Inverse Algorithm (Algorithm
6.3, at slide #9).
"""
a = mult_inverse(phi(p,q),b)
print(f"a: {a}")
