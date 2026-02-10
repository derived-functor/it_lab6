import pytest
from math import pi, sqrt
from src.exp_complex import ExpComplex


class TestExpComplex:
    def test_initialization(self):
        """Проверка инициализации атрибутов"""
        z = ExpComplex(5.0, pi / 2)
        assert z.r == 5.0
        assert z.phi == pi / 2

    def test_str_representation(self):
        """Проверка строкового вывода"""
        z = ExpComplex(2.0, 1.0)
        assert str(z) == "2.0000 * e^( i * 1.0000 )"

    def test_to_cartesian(self):
        """Проверка перевода в декартову форму"""
        z1 = ExpComplex(1.0, 0.0)
        re1, im1 = z1.to_cartesian()
        assert re1 == pytest.approx(1.0)
        assert im1 == pytest.approx(0.0)

        z2 = ExpComplex(1.0, pi / 2)
        re2, im2 = z2.to_cartesian()
        assert re2 == pytest.approx(0.0)
        assert im2 == pytest.approx(1.0)

    def test_from_cartesian(self):
        z = ExpComplex.from_cartesian(1.0, 1.0)
        assert z.r == pytest.approx(sqrt(2))
        assert z.phi == pytest.approx(pi / 4)

    def test_multiplication_complex(self):
        """Умножение объекта на объект"""
        z1 = ExpComplex(2.0, 0.5)
        z2 = ExpComplex(3.0, 1.0)
        res = z1 * z2
        assert res.r == pytest.approx(6.0)
        assert res.phi == pytest.approx(1.5)

    def test_multiplication_scalar(self):
        """Умножение на число (int/float)"""
        z = ExpComplex(2.0, 0.5)
        res = z * 3
        assert res.r == pytest.approx(6.0)
        assert res.phi == pytest.approx(0.5)

    def test_division_complex(self):
        """Деление объекта на объект"""
        z1 = ExpComplex(10.0, 2.0)
        z2 = ExpComplex(2.0, 0.5)
        res = z1 / z2
        assert res.r == pytest.approx(5.0)
        assert res.phi == pytest.approx(1.5)

    def test_division_zero(self):
        """Проверка исключения при делении на ноль"""
        z1 = ExpComplex(5.0, 1.0)
        z2 = ExpComplex(0.0, 0.0)

        with pytest.raises(ZeroDivisionError):
            _ = z1 / z2
        with pytest.raises(ZeroDivisionError):
            _ = z1 / 0.0

    def test_addition(self):
        """Сложение двух комплексных чисел"""
        z1 = ExpComplex(1.0, 0.0)
        z2 = ExpComplex(1.0, pi / 2)
        res = z1 + z2
        assert res.r == pytest.approx(sqrt(2))
        assert res.phi == pytest.approx(pi / 4)

    def test_subtraction_complex(self):
        """Вычитание объекта из объекта"""
        z1 = ExpComplex(2.0, 0.0)
        z2 = ExpComplex(1.0, 0.0)
        res = z1 - z2
        assert res.r == pytest.approx(1.0)
        assert res.phi == pytest.approx(0.0)

    def test_subtraction_scalar(self):
        """Вычитание числа из объекта"""
        z = ExpComplex(2.0, 0.0)
        res = z - 1.5
        assert res.r == pytest.approx(0.5)
        assert res.phi == pytest.approx(0.0)

    def test_quadrant_handling(self):
        """Проверка корректности углов в разных четвертях (тест atan2)"""
        z = ExpComplex.from_cartesian(-1.0, -1.0)
        assert z.phi == pytest.approx(-3 * pi / 4)
