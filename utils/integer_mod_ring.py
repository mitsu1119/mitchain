# --------------------------------------------------------------------------------------------
# Factory Element
# --------------------------------------------------------------------------------------------
class IntegerModRingElement():
    def __init__(self, value: int, parent):
        self.parent = parent
        self.order = parent.order
        self.value = value % self.order

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
            return self.__class__((self.value + other.value) % self.order, self.parent)
        raise TypeError(f"Unsupported operand for +: '{str(self.parent)}' and '{str(other.parent)}'")
    def __sub__(self, other):
        if self.is_calcable(other):
            return self.__class__((self.value - other.value) % self.order, self.parent)
        raise TypeError(f"Unsupported operand for -: '{str(self.parent)}' and '{str(other.parent)}'")
    def __mul__(self, other):
        if self.is_calcable(other):
            return self.__class__((self.value * other.value) % self.order, self.parent)
        raise TypeError(f"Unsupported operand for *: '{str(self.parent)}' and '{str(other.parent)}'")
    def __pow__(self, exponent: int):
        return self.__class__(pow(self.value, exponent, self.order), self.parent)

    # --------------------------------------------------------------------------------------------
    # Comparison Operators
    # --------------------------------------------------------------------------------------------
    def __eq__(self, other):
        if self.is_calcable(other):
            return (self.value == other.value)
        raise TypeError(f"Unsupported operand for ==: '{str(self.parent)}' and '{str(other.parent)}'")
    
    def __ne__(self, other):
        if self.is_calcable(other):
            return (self.value != other.value)
        raise TypeError(f"Unsupported operand for !=: '{str(self.parent)}' and '{str(other.parent)}'")

    # --------------------------------------------------------------------------------------------
    # Other Special Method
    # --------------------------------------------------------------------------------------------
    def __str__(self):
        return str(self.value)

# --------------------------------------------------------------------------------------------
# Type Factory
# --------------------------------------------------------------------------------------------
class IntegerModRing():
    def __init__(self, order: int):
        self.order = order

    def __call__(self, value):
        return IntegerModRingElement(value, self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.order == other.order)
        return False
    
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return (self.order != other.order)
        return True

    def __str__(self):
        return f"ring of integers modulo {self.order}"

Zmod = IntegerModRing
