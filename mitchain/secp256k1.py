from utils import *

class SECP256K1(EllipticCurve):
    def __init__(self):
        p = pow(2, 256) - pow(2, 32) - 977
        Fp = GF(p)
        super().__init__(Fp, 0, 7)

        Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
        self.gen = self(Gx, Gy)
        self.order = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
