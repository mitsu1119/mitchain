from utils.integer_mod_ring import *

# --------------------------------------------------------------------------------------------
# Factory Element
# --------------------------------------------------------------------------------------------
class FpElement(IntegerModRingElement):
    def __truediv__(self, other):
        if self.is_calcable(other):
            return self * other.inv()
        raise TypeError(f"Unsupported operand for //: '{str(self.parent)}' and '{str(other.parent)}'")
    def inv(self):
        return FpElement(pow(self.value, -1, self.order), self.parent)
    def __itruediv__(self, other):
        self = self / other
        return self

# --------------------------------------------------------------------------------------------
# Type Factory
# --------------------------------------------------------------------------------------------
class FiniteField(IntegerModRing):
    def __call__(self, value):
        return FpElement(value, self)

    def __str__(self):
        return f"Finite Field of order {self.order}"

GF = FiniteField
