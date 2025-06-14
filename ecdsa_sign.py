# %%
# Elliptical Curve Digital Signature Algorithm
#
# The curve is represented in the Weierstrass form
# y^2 = x^3 + ax + b, where 4A^3 + 27B^2 != 0
# For this case we take A as 0 and B as 7
# Visualise the curve first
from typing import Tuple
from hashlib import sha1
# %%
# Define the constants
a = 0; b = 7
# %%
# Point addition
def add_points(P, Q, p) -> Tuple:
    # Handle special cases
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P; x2, y2 = Q
    if x1 == x2 and (y1 + y2) % p == 0:
        return None, None
    # Both the points are same
    # Point doubling
    if P == Q:
    # differentiate the curve and get beta
        beta = ((3*x1*x2 + a) % p) * pow(2*y1, -1, p)
    else:
    # If the points are different
        beta = ((y2 - y1) % p) * pow(x2 - x1, -1, p)

    x3 = (beta**2 - x1 - x2) % p
    y3 = (beta * (x1 - x3) - y1) % p

    return (x3, y3)
# %%
# function to check if a point is on the curve
def is_on_curve(P, p) -> bool:
    x, y = P
    return (y ** 2) % p == (x ** 3 + a * x + b) % p
# %%
# Double and add method
def double_and_add_method(G, k, p) -> Tuple:
    target_point = G
    k_binary = bin(k)[2:] # 0b101011110
    for i in range(1, len(k_binary)):
        current_bit = k_binary[i]
        target_point = add_points(target_point, target_point, p)
        if current_bit == '1':
            target_point = add_points(target_point, G, p)
    if not is_on_curve(target_point, p):
        raise ValueError("Error: the resulting point does not lie on the curve")
    return target_point
# %%
G = (55066263022277343669578718895168534326250603453777594175500187360389116729240,
     32670510020758816978083085130507043184471273380659243275938904335757337482424)
p = pow(2, 256) - pow(2, 32) - pow(2, 9) - pow(2, 8) - pow(2, 7) - pow(2, 6) - pow(2, 4) - 1
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
is_on_curve(G, p)
# %%
# print(f"Point at infinity: {n*G}") # Overflow error
#
# Select a random number k in range 1 to n -1
import random

k = random.randint(1, n - 1)

# Compute k.G
kG = double_and_add_method(G=G, k=k, p=p)
x1, y1 = kG

# %%
# Convert x1 to x1_bar or r
r = x1 % n
if r == 0:
    raise ValueError("r = 0, bad k, retry with different k")

# %%
# Covert k inverse mod n
k_inverse_mod_n = pow(k, -1, n)
def compute_e(m: bytes) -> int:
    # Compute SHA1 of the message as bytes
    h: bytes = sha1(m).digest()
    e: int = int.from_bytes(h, byteorder='big')
    return e
m = b"Hello World"
e = compute_e(m)
print(f"{e}")
# %%
def compute_s(e: int, r: int, d: int, k: int, n: int) -> int:
    """
    e: integer from SHA-1(m)
    r: x1 mod n from step 3
    d: private key
    k: the ephemeral nonce you chose (1 <= k <= n-1)
    n: curve order
    """
    # 1) modular inverse of k
    k_inv = pow(k, -1, n)

    # 2) compute s
    s = (k_inv * (e + d * r)) % n

    # 3) if s == 0, you must abort and pick a fresh k
    if s == 0:
        raise ValueError("s = 0, choose a new k and retry")

    return s

# %%
# Generation of public and private key pair
d = random.getrandbits(256) # Private key
Q = double_and_add_method(G=G, k=d, p=p) # public key
s = compute_s(e=e, r=r, d=d, k=k, n=n)
if s == 0:
    raise ValueError("S = 0, bad k, select different k")
print(f"s: {s}")
print(f"Signature is (r, s): {(r, s)}")
