
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
