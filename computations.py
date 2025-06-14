from hashlib import sha1

def compute_e(m: bytes) -> int:
    # Compute SHA1 of the message as bytes
    h: bytes = sha1(m).digest()
    e: int = int.from_bytes(h, byteorder='big')
    return e
