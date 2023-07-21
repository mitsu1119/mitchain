from field import *

# test p4
p = 13
Fp = GF(p)
a = Fp(7)
b = Fp(6)
assert not a == b
assert a != b

# test p7
assert Fp(-27) == Fp(12)
