from __future__ import annotations

from math import atan2, cos, sin, sqrt

Real = float | int


class ExpComplex:
    """Class that represents exponential form of complex number

    :cvar ZERO_PRECISION: precision with which we
        conclude that the float number is zero.

    :ivar r: modulus of complex number.
    :ivar phi: argument of complex number.
    """

    ZERO_PRECISION = 1e-8

    def __init__(self, r: float, phi: float) -> None:
        self.r = r
        self.phi = phi

    def __str__(self) -> str:
        return f'{self.r:.4f} * e^( i * {self.phi:.4f} )'

    def __repr__(self) -> str:
        return self.__str__()

    def __mul__(self, other: ExpComplex | Real) -> ExpComplex:
        """Default complex number multiplication"""

        other = ExpComplex._to_complex(other)

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

        other = ExpComplex._to_complex(other)

        if abs(other.r) < self.ZERO_PRECISION:
            raise ZeroDivisionError('Modulus cannot be equal to zero')

        r_new = self.r / other.r
        phi_new = self.phi - other.phi

        return ExpComplex(r_new, phi_new)

    def __add__(self, other: ExpComplex | Real) -> ExpComplex:
        """Default complex number addition

        To perform addition we first transform complex numbers to algebraic
        form and then return new number in exponential form.
        """

        other = ExpComplex._to_complex(other)

        x1, y1 = self.to_cartesian()

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

        other = ExpComplex._to_complex(other)

        x1, y1 = self.to_cartesian()

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

    @staticmethod
    def _to_complex(value: ExpComplex | Real) -> ExpComplex:
        """Convert real number to ExpComplex"""
        return (
            value
            if isinstance(value, ExpComplex)
            else ExpComplex.from_cartesian(value, 0)
        )
