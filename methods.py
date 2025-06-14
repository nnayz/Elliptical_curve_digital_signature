from typing import Tuple

# Define constants
a = 0; b = 7

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

# function to check if a point is on the curve
def is_on_curve(P, p) -> bool:
    x, y = P
    return (y ** 2) % p == (x ** 3 + a * x + b) % p

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
