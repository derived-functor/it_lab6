import pytest
import math
from src.exp_complex import ExpComplex
from main import calculate_y


class TestFinalFormula:
    def test_y_at_zero(self):
        """Контрольная точка 1: z = 0
        y(0) = 0/2 + ch(1 + 0) = ch(1)
        Результат: ≈ 1.54308
        """
        z = ExpComplex(0.0, 0.0)
        res = calculate_y(z)
        re, im = res.to_cartesian()

        assert re == pytest.approx(math.cosh(1.0))
        assert im == pytest.approx(0.0)

    def test_y_at_minus_one(self):
        """Контрольная точка 2: z = -1
        В экспоненциальной форме: r=1, phi=pi
        y(-1) = -0.5 + ch(1 - 1) = -0.5 + ch(0) = -0.5 + 1 = 0.5
        """
        z = ExpComplex(1.0, math.pi)
        res = calculate_y(z)
        re, im = res.to_cartesian()

        print(re, im)

        assert re == pytest.approx(0.5)
        assert im == pytest.approx(0.0)

    def test_y_complex_value(self):
        """Контрольная точка 3: z = i * pi
        В экспоненциальной форме: r=pi, phi=pi/2
        y(i*pi) = (i*pi)/2 + ch(1 + i*pi)
        ch(1 + i*pi) = ch(1)cos(pi) + i*sh(1)sin(pi) = -ch(1)
        Итого: -ch(1) + i * (pi/2)
        """
        z = ExpComplex(math.pi, math.pi / 2)
        res = calculate_y(z)
        re, im = res.to_cartesian()

        expected_re = -math.cosh(1.0)
        expected_im = math.pi / 2

        assert re == pytest.approx(expected_re)
        assert im == pytest.approx(expected_im)

    def test_y_is_instance_of_complex(self):
        """Проверка, что функция возвращает именно объект нашего класса"""
        z = ExpComplex(1.0, 1.0)
        res = calculate_y(z)
        assert isinstance(res, ExpComplex)
