# --------------------------------------------------------------------------------------------
# Factory Element
# --------------------------------------------------------------------------------------------
class IntegerModRingElement:
    def __init__(self, value: int, parent):
        self.__parent = parent
        self.__order = parent.order()
        self.value = value % self.__order

    # --------------------------------------------------------------------------------------------
    # Calculatable Type
    # --------------------------------------------------------------------------------------------
    def is_calcable(self, other):
        if isinstance(other, self.__class__):
            if self.__parent == other.__parent:
                return True
        return False

    # --------------------------------------------------------------------------------------------
    # Arithmetic Operators
    # --------------------------------------------------------------------------------------------
    def __add__(self, other):
        if self.is_calcable(other):
            return IntegerModRingElement((self.value + other.value) % self.__order, self.__parent)
        raise TypeError(f"Unsupported operand for +: '{str(self.__parent)}' and '{str(other.__parent)}'")
    def __sub__(self, other):
        if self.is_calcable(other):
            return IntegerModRingElement((self.value - other.value) % self.__order, self.__parent)
        raise TypeError(f"Unsupported operand for -: '{str(self.__parent)}' and '{str(other.__parent)}'")
    def __mul__(self, other):
        if self.is_calcable(other):
            return IntegerModRingElement((self.value * other.value) % self.__order, self.__parent)
        raise TypeError(f"Unsupported operand for *: '{str(self.__parent)}' and '{str(other.__parent)}'")

    # --------------------------------------------------------------------------------------------
    # Comparison Operators
    # --------------------------------------------------------------------------------------------
    def __eq__(self, other):
        if self.is_calcable(other):
            return (self.value == other.value)
        raise TypeError(f"Unsupported operand for ==: '{str(self.__parent)}' and '{str(other.__parent)}'")
    
    def __ne__(self, other):
        if self.is_calcable(other):
            return (self.value != other.value)
        raise TypeError(f"Unsupported operand for !=: '{str(self.__parent)}' and '{str(other.__parent)}'")

    # --------------------------------------------------------------------------------------------
    # Other Special Method
    # --------------------------------------------------------------------------------------------
    def __str__(self):
        return str(self.value)

# --------------------------------------------------------------------------------------------
# Type Factory
# --------------------------------------------------------------------------------------------
class IntegerModRing:
    def __init__(self, order: int):
        self.__order = order

    def order(self):
        return self.__order

    def __call__(self, value):
        return IntegerModRingElement(value, self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.__order == other.__order)
        return False
    
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return (self.__order != other.__order)
        return True

    def __str__(self):
        return f"ring of integers modulo {self.__order}"

Zmod = IntegerModRing
