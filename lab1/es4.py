

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

def dec_to_binary(n):
  if n == 0:
    return "0"
  binary = ""
  while n > 0:
    binary = str(n % 2) + binary
    n //= 2
  return binary


"""
Computation of x^c mod n 
"""
def square_and_multiply(x, c, n):
    #convert c from string to list of integers
    c = dec_to_binary(c)
    y = 1
    for i in range(0, len(c)):
        y = (y**2) % n
        if c[i] == '1':
            y = (y*x) % n
    return y

x = 9726 
b = 3533
n = 11413


print(f"alece wants to send the plaintext {x} to bob")


cyphertext= square_and_multiply(x, b, n)
print(f"cyphertext {cyphertext}")


a = 6597
print(f"bob wants to decrypt the cyphertext {cyphertext} using the secret decryption exponent a: {a}")

plaintext = square_and_multiply(cyphertext, a, n)

print(f"plaintext {plaintext}")