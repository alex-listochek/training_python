import calculations
import exceptions


def get_input_type() -> str:
    input_type = ""  # По умолчанию пустая строка
    while input_type not in {"радиус", "диаметр"}:
        input_type = input("Введите 'радиус' или 'диаметр': ").lower()
        if input_type not in {"радиус", "диаметр"}:
            print("Ошибка: допустимые значения - 'радиус' или 'диаметр'.")

    return input_type


def get_positive_number(prompt: str) -> float:
    valid_value = None
    while valid_value is None:
        try:
            user_input = input(prompt)
            value = float(user_input)
            validation_result = exceptions.validate_positive_number(value)
            if isinstance(validation_result, str):
                print(validation_result)
            else:
                valid_value = validation_result
        except ValueError:
            print("Ошибка: введите корректное число.")
        except OverflowError:
            print("Ошибка: Число слишком большое и не поддаётся вычислению.")
            
    return valid_value


def main() -> None:
    print("Программа для вычисления длины окружности и площади круга.")
    
    running = True
    while running:
        input_type = get_input_type()
        value = get_positive_number(f"Введите {input_type}: ")
        
        # Преобразование диаметра в радиус
        radius = value / 2 if input_type == "диаметр" else value
        
        # Вычисления
        circumference = calculations.calculate_circumference(radius)
        area = calculations.calculate_area(radius)
        
        # Проверка на переполнение
        circumference_check = exceptions.check_overflow(circumference)
        area_check = exceptions.check_overflow(area)
        
        # Вывод результатов или сообщений об ошибках
        if isinstance(circumference_check, str):
            print(circumference_check)
        else:
            print(f"\nДлина окружности: {circumference:.4f}")
        
        if isinstance(area_check, str):
            print(area_check)
        else:
            print(f"Площадь круга: {area:.4f}")
        
        # Запрос на повторение
        repeat = input("\nХотите выполнить еще расчет? (да/нет): ").lower()
        if repeat != "да":
            running = False  # Завершение программы
            print("Работа программы завершена.")


if __name__ == "__main__":
    main()