# %%
# Elliptical Curve Digital Signature Algorithm
#
# The curve is represented in the Weierstrass form
# y^2 = x^3 + ax + b, where 4A^3 + 27B^2 != 0
# For this case we take A as 0 and B as 7
from computations import compute_e, compute_s
from methods import double_and_add_method
# %%
# Define the constants
a = 0; b = 7

# %%
G = (55066263022277343669578718895168534326250603453777594175500187360389116729240,
     32670510020758816978083085130507043184471273380659243275938904335757337482424)
p = pow(2, 256) - pow(2, 32) - pow(2, 9) - pow(2, 8) - pow(2, 7) - pow(2, 6) - pow(2, 4) - 1
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
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
# Input the private key from the user
user_input = input("Enter your 256-bit private key as an integer: ")
d = int(user_input)
if d.bit_length() > 256:
    raise ValueError("Private key exceeds 256 bits")
Q = double_and_add_method(G=G, k=d, p=p) # public key


text = input("Enter a message: ")
m = text.encode('utf-8')
e = compute_e(m)
s = compute_s(e=e, r=r, d=d, k=k, n=n)
if s == 0:
    raise ValueError("S = 0, bad k, select different k")
print(f"Signature is (r, s): {(r, s)}")
