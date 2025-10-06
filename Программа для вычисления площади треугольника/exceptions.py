def get_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Число не может быть отрицательным. Повторите ввод.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


def get_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Число не может быть отрицательным. Повторите ввод.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")