from utils import *

class SECP256K1Point(EllipticCurvePoint):
    # --------------------------------------------------------------------------------------------
    # Arithmetic Operators
    # --------------------------------------------------------------------------------------------
    def __rmul__(self, coef: int):
        coef %= self.parent.order()
        return super().__rmul__(coef)

    # --------------------------------------------------------------------------------------------
    # Other Special Method
    # --------------------------------------------------------------------------------------------
    def __repr__(self):
        return "({:x} : {:x} : {:x})".format(self.x, self.y, self.z)

class SECP256K1(EllipticCurve):
    def __init__(self):
        p = pow(2, 256) - pow(2, 32) - 977
        Fp = GF(p)
        super().__init__(Fp, 0, 7)

        Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
        self.__gen = self(Gx, Gy)
        self.__order = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

    def __call__(self, x, y):
        if self.is_on_curve(x, y):
            return SECP256K1Point(x, y, 1, self)
        raise TypeError(f"Coordinates ({x} : {y} : 1) do not define a point on {self}")

    def zero(self):
        return SECP256K1Point(0, 1, 0, self)

    def gen(self):
        return self.__gen

    def order(self):
        return self.__order
