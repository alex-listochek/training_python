import math
import calculations
import exceptions


def main() -> None:
    print("Программа для вычисления площади треугольника.")
    print("Вам предлагается рассчитать площадь треугольника либо по трем сторонам, "
          "либо по двум сторонам и углу между ними.")
    finished = False
    while not finished:
        print("\nВыберите способ вычисления площади:")
        print("1 - По трем сторонам (формула Герона)")
        print("2 - По двум сторонам и углу между ними")
        
        # Выбор метода
        method = -1
        while method not in (1, 2):
            method = exceptions.get_int("Введите 1 или 2: ")
            if method not in (1, 2):
                print("Неверный выбор. Повторите ввод.")

        # Метод 1: По трем сторонам
        if method == 1:
            a = exceptions.get_float("Введите длину стороны a: ")
            b = exceptions.get_float("Введите длину стороны b: ")
            c = exceptions.get_float("Введите длину стороны c: ")
            
            # Проверка существования треугольника
            triangle_valid = (a + b > c) and (a + c > b) and (b + c > a)
            if not triangle_valid:
                print("Введенные стороны не могут образовать треугольник.")
            else:
                area = calculations.area_by_three_sides(a, b, c)
                if math.isinf(area):
                    print("Результат слишком большой.")
                else:
                    print(f"Площадь треугольника: {area:.4f}")

        # Метод 2: По двум сторонам и углу
        else:
            a = exceptions.get_float("Введите длину стороны a: ")
            b = exceptions.get_float("Введите длину стороны b: ")
            angle = exceptions.get_float("Введите угол между сторонами (в градусах): ")
            
            # Проверка угла
            angle_valid = False
            while not angle_valid:
                if 0 < angle < 180:
                    angle_valid = True
                else:
                    print("Угол должен быть в диапазоне (0, 180).")
                    angle = exceptions.get_float("Введите угол между сторонами (в градусах): ")
            
            area = calculations.area_by_two_sides_and_angle(a, b, angle)
            if math.isinf(area):
                print("Результат слишком большой.")
            else:
                print(f"Площадь треугольника: {area:.4f}")

        # Запрос на завершение
        exit_option = -1
        while exit_option not in (0, 1):
            exit_option = exceptions.get_int("Завершить программу? (1 - Да, 0 - Нет): ")
            if exit_option not in (0, 1):
                print("Неверный выбор. Повторите ввод.")
        
        finished = (exit_option == 1)

    print("Завершение программы. До свидания!")


if __name__ == "__main__":
    main()