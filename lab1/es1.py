"""
Greatest Common Divisor (GCD) and the
Euclidean Algorithm
Compute gcd(57, 93) using the Euclidean
algorithm, and find integers s and t such that
57s + 93t = gcd(57, 93).
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

a=int(input("Insert the first number: "))
b=int(input("Insert the second number: "))
print(f"gcd({a},{b}):")
print(euclidean_algorithm(a,b))

"""
now we have to find s and t such that 57s + 93t = gcd(57, 93)
"""

def extended_euclidean_algorithm(a, b):
    A = [a]
    B = [b]
    T = [0]
    t = 1
    S = [1]
    s = 0
    q = A[0] // B[0]
    r = A[0] - q * B[0]
    while r > 0:
        temp = T[0] - q * t
        T[0] = t
        t = temp
        temp = S[0] - q * s
        S[0] = s
        s = temp
        A[0] = B[0]
        B[0] = r
        q = A[0] // B[0]
        r = A[0] - q * B[0]
    r = B[0]
    return (r, s, t)


print("extended_euclidean_algorithm:")
(r,s,t) = extended_euclidean_algorithm(a,b)
print(f"57*{s} + 93*{t} = {r}")