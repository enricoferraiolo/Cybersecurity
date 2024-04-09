




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






