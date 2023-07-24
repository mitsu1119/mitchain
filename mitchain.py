from utils import *

p = 13
Fp = GF(13)
E = EllipticCurve(Fp, 1, 2)
P = E(2, 5)
Q = E(2, 8)

print(P == Q)
print(P == -Q)
print(P + Q)
