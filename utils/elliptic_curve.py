
# --------------------------------------------------------------------------------------------
# Elliptic Curve y^2 = x^3 + a*x + b over base_field
# --------------------------------------------------------------------------------------------
class EllipticCurve:
    def __init__(self, base_field, a, b):
        self.base = base_field
        self.a = base_field(a)
        self.b = base_field(b)

    def __str__(self):
        return f"Elliptic Curve defined by y^2 = x^3 + {self.a}*x + {self.b} over {self.base}"
