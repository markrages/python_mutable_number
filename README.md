mutable_number.py
-----------------

A class for representing mutable numbers in Python.

This makes a mutable version of a number (integer, complex, float)
with all the special methods delegated to the underlying number.

This allows the number to have auxiliary information attached to it.

Example
-------
```
Python 3.5.2 (default, Nov 17 2016, 17:05:23)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mutable_number
>>> m = mutable_number.MutableNumber(3)
>>> m
3
>>> id(m)
140611097008224
>>> m+=1
>>> m
4
>>> id(m)
140611097008224
>>> class UnitNumber(mutable_number.MutableNumber):
...    def __init__(self, n, units):
...       super().__init__(n)
...       self.units = units
...    def __repr__(self):
...       return super().__repr__()+' '+self.units
...
>>> un = UnitNumber(4, 'Volts')
>>> un
4 Volts
>>> un + 8
12
>>> un += 1
>>> un
5 Volts
>>> un *= 1j
>>> un
5j Volts
```

Notes
-----

Has this basic idea been done before?  Please let me know what I've
re-invented.
