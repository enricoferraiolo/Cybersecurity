def extended_gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def multiplicative_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"The multiplicative inverse of {a} modulo {m} does not exist.")
    else:
        return x % m

# (a) Compute the multiplicative inverse of 17 modulo 101
inverse_a = multiplicative_inverse(17, 101)
print("(a) Multiplicative inverse of 17 modulo 101:", inverse_a)

# (b) Compute the multiplicative inverse of 357 modulo 1234
inverse_b = multiplicative_inverse(357, 1234)
print("(b) Multiplicative inverse of 357 modulo 1234:", inverse_b)

# (c) Compute the multiplicative inverse of 3125 modulo 9987
inverse_c = multiplicative_inverse(3125, 9987)
print("(c) Multiplicative inverse of 3125 modulo 9987:", inverse_c)
