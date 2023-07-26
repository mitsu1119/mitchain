from utils import *

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
