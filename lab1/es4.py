"""
The RSA Cryptosystem: an example
Now, suppose Alice wants to encrypt the plaintext 9726
to send to Bob. She will compute 97263533 mod 11413
and send the ciphertext c over the channel.
- Please determine c’s value using the square and
multiply algorithm (Algorithm 6.5 at slide #10 )
When Bob receives the ciphertext c, he uses his secret
decryption exponent a to compute the plaintext sent by
Alice.
"""


"""
Computation of x^c mod n 
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


