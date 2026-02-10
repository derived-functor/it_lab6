from src import ExpComplex
from src.functions import HyperbolicCosine
from math import pi


def calculate_y(z: ExpComplex) -> ExpComplex:
    cosh = HyperbolicCosine()

    term1 = z / 2
    term2 = cosh(1 + z)

    return term1 + term2


def main():
    print("y(z) = z/2 + cosh(1 + z)")

    try:
        r = float(input("Введите модуль комплексного числа (r): "))
        phi = float(input("Введите аргумент (phi) в радианах: "))

        z = ExpComplex(r, phi)
        print(f"\nСоздано число z: {z}")
        z_x, z_y = z.to_cartesian()
        print(f"В декартовых координатах: ({z_x:.4f}, {z_y:.4f})")

        result = calculate_y(z)

        print(f"Результат функции y(z):")
        print(f"y = {result}")
        result_x, result_y = result.to_cartesian()
        print(f"y (декартовы): ({result_x:.4f}, {result_y:.4f})")

        print("\nДемонстрация работы арифметики:")
        z2 = ExpComplex(2, pi / 4)
        print(f"Второе число z2: {z2}")
        print(f"z + z2 = {z + z2}")
        print(f"z * z2 = {z * z2}")
        print(f"z / 2  = {z / 2}")
        print(f"1 + z  = {1 + z}")

    except ValueError:
        print("Ошибка: введите корректные числовые значения.")
    except ZeroDivisionError as e:
        print(f"Ошибка деления: {e}")


if __name__ == "__main__":
    main()
