def extended_gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

# Find gcd(57, 93) using the Euclidean algorithm
gcd_value = gcd_euclidean(57, 93)
print("gcd(57, 93) =", gcd_value)

# Find integers s and t such that 57s + 93t = gcd(57, 93)
gcd, s, t = extended_gcd(57, 93)
print("s =", s)
print("t =", t)

