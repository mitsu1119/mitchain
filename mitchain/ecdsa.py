from mitchain.secp256k1 import *
from hashlib import sha256
from random import randint

def hash256(bs):
    return sha256(sha256(bs).digest()).digest()

class ECDSASignature:
    def __init__(self, r, s):
        self.r = r
        self.s = s

    def __repr__(self):
        return "Signature of ECDSA (r, s) = ({:x}, {:x})".format(self.r, self.s)

class ECDSAPrivateKey:
    def __init__(self, ecdsa, secret):
        self.ecdsa = ecdsa
        self.secret = secret
        self.point = secret * ecdsa.gen

    def sign(self, z):
        Fo = GF(self.ecdsa.order)
        k = randint(0, self.ecdsa.order - 1)
        k = 1234567890
        r = (k * self.ecdsa.gen).x.value
        s = Fo(z + r * self.secret) / Fo(k)
        if s.value > self.ecdsa.order / 2:
            s = Fo(self.ecdsa.order - s.value)
        return ECDSASignature(r, s.value)

    def hex(self):
        return "{:x}".format(self.secret)

# order must be prime
class ECDSA:
    def __init__(self, E):
        self.E = E
        self.gen = E.gen()
        self.order = E.order()

    def gen_private_key(self, secret):
        return ECDSAPrivateKey(self, secret)

    def verify(self, P, z, sig):
        assert self.E.is_on_curve(P.x, P.y)
        Fp = GF(self.order)
        u = (Fp(z) / Fp(sig.s)).value
        v = (Fp(sig.r) / Fp(sig.s)).value
        return (u * self.gen + v * P).x.value == sig.r

