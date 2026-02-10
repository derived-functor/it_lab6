from __future__ import annotations
from math import cos, sin, sqrt, atan2, pi

Real = float | int


class ExpComplex:
    """Class that represents exponential form of complex number

    :cvar ZERO_PRECISION: precision with which we
        conclude that the float number is zero.

    :ivar r: modulus of complex number.
    :ivar phi: argument of complex number.
    """

    ZERO_PRECISION = 1e-8

    def __init__(self, r: float, phi: float):
        self.r = r
        self.phi = phi

    def __str__(self) -> str:
        return f"{self.r} * e^( i * {self.phi} )"

    def __repr__(self) -> str:
        return self.__str__()

    def __mul__(self, other: ExpComplex | Real) -> ExpComplex:
        """Default complex number multiplication"""

        if isinstance(other, (float, int)):
            return ExpComplex(self.r * other, self.phi)

        r_new = self.r * other.r
        phi_new = self.phi + other.phi

        return ExpComplex(r_new, phi_new)

    def __rmul__(self, other: ExpComplex | Real) -> ExpComplex:
        return self.__mul__(other)

    def __truediv__(self, other: ExpComplex | Real) -> ExpComplex:
        """Default complex number division

        :raise ZeroDivisionError: raises, when modulus
            of second argument is (almost) zero.
        """

        if isinstance(other, (float, int)):
            if abs(other) < self.ZERO_PRECISION:
                raise ZeroDivisionError("Modulus cannot be equal to zero")
            return ExpComplex(self.r / other, self.phi)

        if abs(other.r) < self.ZERO_PRECISION:
            raise ZeroDivisionError("Modulus cannot be equal to zero")

        r_new = self.r / other.r
        phi_new = self.phi - other.phi

        return ExpComplex(r_new, phi_new)

    def __add__(self, other: ExpComplex | Real) -> ExpComplex:
        """Default complex number addition

        To perform addition we first transform complex numbers to algebraic
        form and then return new number in exponential form.
        """
        x1, y1 = self.to_cartesian()

        if isinstance(other, (float, int)):
            x_new = x1 - other
            y_new = y1

            return ExpComplex.from_cartesian(x_new, y_new)

        x2, y2 = other.to_cartesian()

        x_new = x1 + x2
        y_new = y1 + y2

        return ExpComplex.from_cartesian(x_new, y_new)

    def __radd__(self, other: ExpComplex | Real) -> ExpComplex:
        """Right addition implementation"""
        return self.__add__(other)

    def __sub__(self, other: ExpComplex | Real) -> ExpComplex:
        """Default complex number subtraction

        To perform subtraction we first transform complex numbers to algebraic
        form and then return new number in exponential form.
        """

        x1, y1 = self.to_cartesian()

        if isinstance(other, (float, int)):
            x_new = x1 - other
            y_new = y1

            return ExpComplex.from_cartesian(x_new, y_new)

        x2, y2 = other.to_cartesian()

        x_new = x1 - x2
        y_new = y1 - y2

        return ExpComplex.from_cartesian(x_new, y_new)

    def to_cartesian(self) -> tuple[float, float]:
        """Transforms complex number in exponential form to algebraic form"""
        real = self.r * cos(self.phi)
        imaginary = self.r * sin(self.phi)

        return (real, imaginary)

    @classmethod
    def from_cartesian(cls, x: float, y: float) -> ExpComplex:
        """Constructs complex number in exponential form from cartesian coordinates"""

        phi = atan2(y, x)
        r = sqrt(x**2 + y**2)

        return cls(r, phi)
