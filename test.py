from utils import *
from mitchain import *

# test p4
Fp = GF(13)
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

# test p11 (practice 4)
Fp = GF(97)
assert Fp(95) * Fp(45) * Fp(31) == Fp(23)
assert Fp(17) * Fp(13) * Fp(19) * Fp(44) == Fp(68)
assert Fp(12)**7 * Fp(77)**49 == Fp(63)

# test p11 (practice 5)
print("<practice 5 p11>")
Fp = GF(19)
ks = [1,3,7,13,18]
for k in ks:
    print(f"k = {k} [", end="")
    for i in range(19):
        print(Fp(i) * Fp(k), end=" ")
    print("]")

# test p12
Fp = GF(13)
a = Fp(3)
b = Fp(12)
c = Fp(10)
assert a * b == c

# test p13 (practice 7)
print()
print("<practice 7 p13>")
ps = [7, 11, 17, 31]
for p in ps:
    Fp = GF(p)
    print(f"p = {p} [", end="")
    for i in range(1, p):
        print(Fp(i)**(p - 1), end=" ")
    print("]")

# test p16 (practice 8)
Fp = GF(31)
assert Fp(3) / Fp(24) == Fp(4)
assert Fp(17)**(-3) == Fp(29)
assert Fp(4)**(-4) * Fp(11) == Fp(13)

Fp = GF(13)
E = EllipticCurve(Fp, 2, 2)
P = E(2, 1)
print(P)

# test p28 (practice 1)
E = EllipticCurve(float, 5, 7)
assert not E.is_on_curve(2, 4)
assert E.is_on_curve(-1, -1) 
assert E.is_on_curve(18, 77)
assert not E.is_on_curve(5, 7)

# test p35
P = E(18, 77)
Q = -P
assert P + Q == E.zero()

# test p37 (practice 4)
E = EllipticCurve(float, 5, 7)
P = E(2, 5)
Q = E(-1, -1)
assert P + Q == E(3, -7)

# test p40 (practice 6)
E = EllipticCurve(float, 5, 7)
P = E(-1, -1)
assert P + P == E(18, 77)

# ------------------------------------

# test p45 (practice 1)
Fp = GF(223)
E = EllipticCurve(Fp, 0, 7)
assert E.is_on_curve(192, 105)
assert E.is_on_curve(17, 56)
assert not E.is_on_curve(200, 119)
assert E.is_on_curve(1, 193)
assert not E.is_on_curve(42, 99)

# test p49 (practice 2)
assert E(170, 142) + E(60, 139) == E(220, 181)
assert E(47, 71) + E(17, 56) == E(215, 68)
assert E(143, 98) + E(76, 66) == E(47, 71)

# test p52 (practice 4)
assert 2 * E(192, 105) == E(49, 71)
assert 2 * E(143, 98) == E(64, 168)
assert 2 * E(47, 71) == E(36, 111)
assert 4 * E(47, 71) == E(194, 51)
assert 8 * E(47, 71) == E(116, 55)
assert 21 * E(47, 71) == E.zero()

# test p58 (practice 5)
P = E(15, 86)
for i in range(1, 7):
    assert i * P != E.zero()
assert 7 * P == E.zero()

# test sec256k1 order
E = SECP256K1()
G = E.gen()
assert E.order() * G == E.zero()

# test p68 
E = SECP256K1()
G = E.gen()
Fp = GF(E.order())
z = 0xbc62d4b80d9e36da29c16c5d4d9f11731f36052c72401a76c23c0fb5a9b74423
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
px = 0x04519fac3d910ca7e7138f7013706f619fa8f033e6ec6e09370ea38cee6a7574
py = 0x82b51eab8c27c66e26c858a079bcdf4f1ada34cec420cafc7eac1a42216fb6c4
P = E(px, py)
u = (Fp(z) / Fp(s)).value
v = (Fp(r) / Fp(s)).value
assert (u*G + v*P).x.value == r

# test p69
P = E(0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c, 0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34)
ecdsa = ECDSA(E)
# signature 1
z = 0xec208baa0fc1c19f708a9ca96fdeff3ac3f230bb4a7ba4aede4942ad003c0f60
r = 0xac8d1c87e51d0d441be8b3dd5b05c8795b48875dffe00b7ffcfac23010d3a395
s = 0x68342ceff8935ededd102dd876ffd6ba72d6a427a3edb13d26eb0781cb423c4
sig = ECDSASignature(r, s)
assert ecdsa.verify(P, z, sig)
# signature 2
z = 0x7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
r = 0xeff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
s = 0xc7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6
sig = ECDSASignature(r, s)
assert ecdsa.verify(P, z, sig)

# test p71 (practice 7)
secret = 12345
z = int.from_bytes(hash256(b"Programming Bitcoin!"), "big")
priv = ecdsa.gen_private_key(secret)
sig = priv.sign(z)
assert ecdsa.verify(priv.point, z, sig)
