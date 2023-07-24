from utils import *

p = 13
Fp = GF(13)
E = EllipticCurve(Fp, 1, 2)
P = E(2, 5)
O = E.zero()

print(P == P)
