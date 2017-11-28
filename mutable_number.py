#!/usr/bin/python3

import numbers
import math

class MutableNumber(numbers.Integral):
    """Emulate numeric types based on "n" attribute, based on
    https://docs.python.org/3/reference/datamodel.html#basic-customization
    https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types

    This is effectively a mutable container for a number, and can be
    subclassed to provide interesting properties that are related to
    the number.

    To use this class, subclass (if you like) or construct it
    directly, passing the numerical object you wish to make mutable to
    the initializer.

    The current immutable number is the 'n' attribute, and all the
    numeric type dunder methods just delegate to this current number.

    """

    # Basic customization
    def __init__(self, n=None): self.n=n
    def __repr__(self): return repr(self.n)
    def __str__(self): return str(self.n)
    # def __bytes__(self): unimplemented
    def __format__(self, format_spec): self.n.__format__(format_spec)

    def __lt__(self, other): return self.n < other
    def __le__(self, other): return self.n <= other
    def __ne__(self, other): return self.n != other
    def __eq__(self, other): return self.n == other
    def __gt__(self, other): return self.n > other
    def __ge__(self, other): return self.n >= other

    def __hash__(self): return hash(self.n)
    def __bool__(self): return bool(self.n)

    # math functions
    def __ceil__(self): return math.ceil(self.n)
    def __floor__(self): return math.floor(self.n)
    def __trunc__(self): return math.trunc(self.n)

    # Binary arithmetic operations
    def __add__(self, other): return self.n + other
    def __sub__(self, other): return self.n - other
    def __mul__(self, other): return self.n * other
    def __truediv__(self, other): return self.n / other
    def __floordiv__(self, other): return self.n // other
    def __mod__(self, other): return self.n % other
    def __divmod__(self, other): return divmod(self.n, other)
    def __pow__(self, other, modulo=None): return pow(self.n, other, modulo)
    def __lshift__(self, other): return self.n << other
    def __rshift__(self, other): return self.n >> other
    def __and__(self, other): return self.n & other
    def __xor__(self, other): return self.n ^ other
    def __or__(self, other): return self.n | other

    # Right binary operations
    def __radd__(self, other): return other + self.n
    def __rsub__(self, other): return other - self.n
    def __rmul__(self, other): return other * self.n
    def __rtruediv__(self, other): return other / self.n
    def __rfloordiv__(self, other): return other // self.n
    def __rmod__(self, other): return other % self.n
    def __rdivmod__(self, other): return divmod(other, self.n)
    def __rpow__(self, other): return pow(other, self.n)
    def __rlshift__(self, other): return other << self.n
    def __rrshift__(self, other): return other >> self.n
    def __rand__(self, other): return other & self.n
    def __rxor__(self, other): return other ^ self.n
    def __ror__(self, other): return other | self.n

    # In-place binary operations
    def __iadd__(self, other):
        self.n += other
        return self
    def __isub__(self, other):
        self.n -= other
        return self
    def __imul__(self, other):
        self.n *= other
        return self
    def __itruediv__(self, other):
        self.n /= other
        return self
    def __ifloordiv__(self, other):
        self.n //= other
        return self
    def __imod__(self, other):
        self.n %= other
        return self
    def __ipow__(self, other, modulo=None):
        self.n = pow(self.n, other, modulo)
        return self
    def __ilshift__(self, other):
        self.n <<= other
        return self
    def __irshift__(self, other):
        self.n >>= other
        return self
    def __iand__(self, other):
        self.n &= other
        return self
    def __ixor__(self, other):
        self.n ^= other
        return self
    def __ior__(self, other):
        self.n |= other
        return self

    # Unary arithmetic operations
    def __neg__(self): return -self.n
    def __pos__(self): return +self.n
    def __abs__(self): return abs(self.n)
    def __invert__(self): return ~self.n

    # Conversion functions
    def __complex__(self): return complex(self.n)
    def __int__(self): return int(self.n)
    def __float__(self): return float(self.n)
    def __round__(self, n=0): return round(self.n, n)

    def __index__(self): return self.n.__index__()

    # integer functions
    # https://docs.python.org/3/library/stdtypes.html#additional-methods-on-integer-types
    def bit_length(self): return self.n.bit_length()
    def to_bytes(self, length, byteorder, *args, signed=False):
        return self.n.to_bytes(length, byteorder, *args, signed=signed)
    def from_bytes(self, bytes, byteorder, *args, signed=False):
        return self.n.from_bytes(bytes, byteorder, *args, signed=signed)
    def conjugate(self): return self.n.conjugate()

    @property
    def denominator(self): return self.n.denominator
    @property
    def numerator(self): return self.n.numerator

    @property
    def imag(self): return self.n.imag
    @property
    def real(self): return self.n.real

    # float functions
    # https://docs.python.org/3/library/stdtypes.html#additional-methods-on-float
    def as_integer_ratio(self): return self.n.as_integer_ratio()
    def is_integer(self): return self.n.is_integer()
    def hex(self): return self.n.hex()

    @property
    def value(self): return self.n

    @value.setter
    def value(self, n): self.n = n
