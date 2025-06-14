from hashlib import sha1

def compute_e(m: bytes) -> int:
    # Compute SHA1 of the message as bytes
    h: bytes = sha1(m).digest()
    e: int = int.from_bytes(h, byteorder='big')
    return e

def compute_s(e: int, r: int, d: int, k: int, n: int) -> int:
    # 1) modular inverse of k
    k_inv = pow(k, -1, n)

    # 2) compute s
    s = (k_inv * (e + d * r)) % n

    # 3) if s == 0, you must abort and pick a fresh k
    if s == 0:
        raise ValueError("s = 0, choose a new k and retry")

    return s
