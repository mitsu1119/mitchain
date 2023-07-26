from mitchain.secp256k1 import *

class ECDSASignature:
    def __init__(self, r, s):
        self.r = r
        self.s = s

    def __repr__(self):
        return "Signature of ECDSA (r, s) = ({:x}, {:x})".format(self.r, self.s)

# order must be prime
class ECDSA:
    def __init__(self, E):
        self.E = E
        self.gen = E.gen()
        self.order = E.order()

    def verify(self, P, z, sig):
        assert self.E.is_on_curve(P.x, P.y)
        Fp = GF(self.order)
        u = (Fp(z) / Fp(sig.s)).value
        v = (Fp(sig.r) / Fp(sig.s)).value
        return (u * self.gen + v * P).x.value == sig.r
