import math


def validate_positive_number(value: float) -> str | float:
    result = None
    if math.isinf(value):
        result = "Ошибка: Число слишком большое и не поддаётся вычислению."
    elif value <= 0:
        result = "Ошибка: Значение должно быть положительным."
    else:
        result = value

    return result


def check_overflow(result: float) -> str | float:
    output = result
    if math.isinf(result):
        output = "(!) Предупреждение: Результат вычислений слишком большой."
        
    return output

