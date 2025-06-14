# Generate public and private key pair
import random
from methods import double_and_add_method

G = (55066263022277343669578718895168534326250603453777594175500187360389116729240,
     32670510020758816978083085130507043184471273380659243275938904335757337482424)
p = pow(2, 256) - pow(2, 32) - pow(2, 9) - pow(2, 8) - pow(2, 7) - pow(2, 6) - pow(2, 4) - 1
d = random.getrandbits(256) # private key
Q = double_and_add_method(G=G, k=d, p=p) # public key

print(f"Your Public key: {Q}")
print(f"Your private key: {d}")
