# --------------------------------------------------------------------------------------------
# Point of Elliptic Curve
# --------------------------------------------------------------------------------------------
class EllipticCurvePoint:
    def __init__(self, x, y, z, parent):
        self.parent = parent
        self.x = parent.base(x)
        self.y = parent.base(y)
        self.z = parent.base(z)

        if (self.x, self.z) == (parent.base(0), parent.base(0)) and self.y != parent.base(0):
            self.y = parent.base(1)
            return

        if self.z != parent.base(0):
            self.x = self.x / self.z
            self.y = self.y / self.z
            self.z = parent.base(1)
            return

        raise TypeError(f"Coordinates ({self.x} : {self.y} : {self.z}) do not define a point on {self.parent}")

    def is_zero(self):
        if self.x == self.parent.base(0) and self.y != self.parent.base(0) and self.z == self.parent.base(0):
            return True
        return False

    # --------------------------------------------------------------------------------------------
    # Calculatable Type
    # --------------------------------------------------------------------------------------------
    def is_calcable(self, other):
        if isinstance(other, self.__class__):
            if self.parent == other.parent:
                return True
        return False

    # --------------------------------------------------------------------------------------------
    # Arithmetic Operators
    # --------------------------------------------------------------------------------------------
    def __add__(self, other):
        if self.is_calcable(other):
            if self.is_zero():
                return other
            elif other.is_zero():
                return self
        raise TypeError(f"Unsupported operand for +: '{str(self.parent)}' and '{str(other.parent)}'")
    def __sub__(self, other):
        if self.is_calcable(other):
            if self.is_zero():
                return other.inv()
            elif other.is_zero():
                return self
        raise TypeError(f"Unsupported operand for -: '{str(self.parent)}' and '{str(other.parent)}'")
    def inv(self):
        return self.__class__(self.x, -self.y, self.z, self.parent)

    def __str__(self):
        return f"({self.x} : {self.y} : {self.z})"

# --------------------------------------------------------------------------------------------
# Elliptic Curve y^2 = x^3 + a*x + b over base_field
# --------------------------------------------------------------------------------------------
class EllipticCurve:
    def __init__(self, base_field, a, b):
        self.base = base_field
        self.a = base_field(a)
        self.b = base_field(b)

    def __call__(self, x, y):
        if self.is_on_curve(x, y):
            return EllipticCurvePoint(x, y, 1, self)
        raise TypeError(f"Coordinates ({x} : {y} : 1) do not define a point on {self}")

    def zero(self):
        return EllipticCurvePoint(0, 1, 0, self)

    def is_on_curve(self, x, y):
        xx = self.base(x)
        yy = self.base(y)
        if pow(yy, 2) == pow(xx, 3) + self.a * xx + self.b:
            return True
        return False

    def __str__(self):
        return f"Elliptic Curve defined by y^2 = x^3 + {self.a}*x + {self.b} over {self.base}"
