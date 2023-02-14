import random

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        rem = a % b
        a, b = b, rem
    return a

def mod_inverse(e, z):
    d = 2
    while d < z:
        if (e * d) % z == 1:
            return d
        d += 1

def generate_key(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    e = random.randint(2, z - 1)
    while gcd(e, z) != 1:
        e = random.randint(2, z - 1)
    d = mod_inverse(e, z)
    return {
        "public_key": (n, e),
        "private_key": (p, q, d)
    }

def encrypt(message, public_key):
    n, e = public_key
    return "".join(chr(pow(ord(c), e, n)) for c in message)

def decrypt(cipher_text, private_key):
    p, q, d = private_key
    n = p * q
    return "".join(chr(pow(ord(c), d, n)) for c in cipher_text)

if __name__ == "__main__":
    # key = generate_key(151, 157)
    print(generate_key(151, 157))
