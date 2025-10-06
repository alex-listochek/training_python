"""
    Модуль main - запускаемая программа для вывода первых 10 строк текстового файла.
    Методы:
        main() -> None - запрашивает у пользователя имя текстового файла с его типом.
    Импортируемые методы:
        safe_get_head_lines из модуля error_handler
"""
from error_handler import safe_get_head_lines


def main() -> None:
    """
        Метод запрашивает у пользователя имя текстового файла с типом txt и выводит первые 10 строк из этого файла.
        
        Параметры:
            filename:str - принимает имя текстового файла с типом txt.
            lines, error:str - вывод первые 10 строк заданного текстового файла или ошибку в работе с программой.
            i:bool - флаг для выхода из циклов.
    """
    print("Программа выводит первые 10 строк указанного файла.")
    print("Файл должен находиться в одной папке с модулями программы.\n")
    
    i = True                
    while i:
        filename = input("Введите имя файла (или *exit* для выхода): ")

        if filename.lower() == "exit":
            print ("Выход из программы.")
            i = False

        elif not filename:
            print("Ошибка: имя файла не может быть пустым.")
            i = False

        lines, error = safe_get_head_lines(filename)

        if error:
            print(f"\n{error}")
        else:
            print(f"\nПервые 10 строк файла {filename}: ")
            for line in lines:
                print(line)

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()