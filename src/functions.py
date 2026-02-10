from math import exp
from src.exp_complex import ExpComplex


class HyperbolicCosine:
    """Implementation of cosh function for ExpComplex"""

    def __call__(self, z: ExpComplex) -> ExpComplex:
        x, y = z.to_cartesian()

        first_exp = exp(x) * ExpComplex(1.0, y)
        second_exp = exp(-x) * ExpComplex(1.0, -y)

        return (first_exp + second_exp) / 2
