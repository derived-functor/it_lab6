import pytest
import math
from src.exp_complex import ExpComplex

from src import HyperbolicCosine


@pytest.fixture
def cosh_fn():
    return HyperbolicCosine()


class TestCosh:
    def test_cosh_zero(self, cosh_fn):
        """ch(0) = 1"""
        z = ExpComplex(0.0, 0.0)
        res = cosh_fn(z)
        re, im = res.to_cartesian()
        assert re == pytest.approx(1.0)
        assert im == pytest.approx(0.0)

    def test_cosh_real(self, cosh_fn):
        """ch(1) должен быть равен math.cosh(1)"""
        z = ExpComplex(1.0, 0.0)
        res = cosh_fn(z)
        re, im = res.to_cartesian()
        assert re == pytest.approx(math.cosh(1.0))
        assert im == pytest.approx(0.0)

    def test_cosh_pure_imaginary(self, cosh_fn):
        """ch(i * pi) = cos(pi) = -1"""
        z = ExpComplex(math.pi, math.pi / 2)
        res = cosh_fn(z)
        re, im = res.to_cartesian()
        assert re == pytest.approx(-1.0)
        assert im == pytest.approx(0.0)

    def test_cosh_complex_value(self, cosh_fn):
        """ch(1 + i*pi/4) = ch(1)cos(pi/4) + i*sh(1)sin(pi/4)"""
        z = ExpComplex.from_cartesian(1.0, math.pi / 4)
        res = cosh_fn(z)
        re, im = res.to_cartesian()

        expected_re = math.cosh(1.0) * math.cos(math.pi / 4)
        expected_im = math.sinh(1.0) * math.sin(math.pi / 4)

        assert re == pytest.approx(expected_re)
        assert im == pytest.approx(expected_im)

    def test_cosh_symmetry(self, cosh_fn):
        """ch(z) == ch(-z)"""
        z = ExpComplex(2.0, 0.5)
        z_neg = ExpComplex(2.0, 0.5 + math.pi)

        res1 = cosh_fn(z)
        res2 = cosh_fn(z_neg)

        re1, im1 = res1.to_cartesian()
        re2, im2 = res2.to_cartesian()

        assert re1 == pytest.approx(re2)
        assert im1 == pytest.approx(im2)
