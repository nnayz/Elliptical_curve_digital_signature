from computations import compute_e
from methods import double_and_add_method, add_points

# Define constants
a = 0; b = 7
G = (55066263022277343669578718895168534326250603453777594175500187360389116729240,
     32670510020758816978083085130507043184471273380659243275938904335757337482424)
p = pow(2, 256) - pow(2, 32) - pow(2, 9) - pow(2, 8) - pow(2, 7) - pow(2, 6) - pow(2, 4) - 1
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337

Q = eval(input("Enter the public key: "))

# Input the message from the user
text = input("Enter the message: ")
message = text.encode('utf-8')

r, s = eval(input("Enter (r, s) signature: "))


# 1. Verify if r and s are in the range [1, n-1]
if r > n - 1 or r < 1 or s > n - 1 or s < 1:
    raise ValueError("Invalid Signature")

e = compute_e(message)
w = pow(s, -1, n)
u1 = (e*w) % n
u2 = (r*w) % n

u1xG = double_and_add_method(G=G, k=u1, p=p)
u2xQ = double_and_add_method(G=Q, k=u2, p=p)

X = add_points(u1xG, u2xQ, p)

# X is point at infinity, reject
if X is None:
    raise ValueError("Invalid Signature")
x1, y1 = X
v = x1 % n

if v == r:
    print("Singature verified!!")
else:
    print("Wrong Signature!!")
