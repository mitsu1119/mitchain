from utils import *

# test p4
p = 13
Fp = GF(p)
a = Fp(7)
b = Fp(6)
assert not a == b
assert a != b

# test p7
assert Fp(-27) == Fp(12)

# test p8
Zn = Zmod(57)
assert Zn(44) + Zn(33) == Zn(20)
assert Zn(9) - Zn(29) == Zn(37)
assert Zn(17) + Zn(42) + Zn(49) == Zn(51)
assert Zn(52) - Zn(30) - Zn(38) == Zn(41)
