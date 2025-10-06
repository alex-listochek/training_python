from exceptions import is_valid_integer, is_reasonable_number
from processing import generate_numbers, sort_numbers, count_negatives


def main_loop():
    print("Программа генерирует N случайных чисел в диапазоне [-26; 13], сортирует их по убыванию и подсчитывает количество отрицательных чисел.")
    
    input_valid = False
    while not input_valid:
        n_str = input("\nПожалуйста, введите целое положительное число N (максимум 1 000 000): ")
        
        if not is_valid_integer(n_str):
            print("Ошибка: Некорректный ввод. Введите целое число.")
            continue
            
        n = int(n_str)
        if not is_reasonable_number(n):
            print("Ошибка: Слишком большое число. Максимальное допустимое значение - 1 000 000.")
        elif n <= 0:
            print("Ошибка: N должно быть положительным.")
        else:
            input_valid = True

    numbers = generate_numbers(n)
    sorted_numbers = sort_numbers(numbers)
    negative_count = count_negatives(sorted_numbers)

    print("\nОтсортированные числа по убыванию:")
    print(' '.join(map(str, sorted_numbers)))
    print(f"\nКоличество отрицательных чисел: {negative_count}")


def main():
    """Точка входа в программу."""
    running = True
    while running:
        main_loop()
        
        restart = input("\nХотите выполнить еще один расчет? (да/нет): ").lower()
        while restart not in {'да', 'нет'}:
            restart = input("Некорректный ввод. Пожалуйста, введите 'да' или 'нет': ").lower()
            
        running = (restart == 'да')

    input("\nНажмите Enter для завершения работы программы...")


if __name__ == "__main__":
    main()