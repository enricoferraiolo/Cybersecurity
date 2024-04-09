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

print("gcd(57,93):")
print(euclidean_algorithm(57,93))