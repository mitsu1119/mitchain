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
