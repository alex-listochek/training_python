"""
    Модуль main - главный модуль программы для взаимодействия с пользователем.
    Методы:
        main() -> None - запрашивает у пользователя имя файла с типом .py в котором нужно удалить комментарии.
    Импортируемые методы:
        generate_unique_filename, process_file из модуля processing
"""

from processing import generate_unique_filename, process_file


def main():
    """
        Метод запрашивает у пользователя имя файла с типом .py в котором нужно удалить комментарии.
        
        Параметры:
            running:bool - флаг для работы цикла.
            user_input:str - принимает имя файла из которого нужно удалить комментарии.
            is_exit:bool - хранит функцию, которая завершает программу при вводе команды exit.
            source_path:str - принимает имя файла, который ввёл пользователь.
            dest_path:str - хранит функцию генерации файла с удалёнными комментариями.
            error_message:str|None - принимает ошибку, которая могла произойти в работе с программой или её отсутствие.
            output_message:str - сообщение с именем нового файла с вырезанными комментариями.
    """
    running = True

    while running:
        user_input = input("Введите имя исходного файла (<имя>.py) или 'exit' для выхода из программы: ").strip()
        is_exit = user_input.lower() == "exit"

        if is_exit:
            print("Выход из программы.")
            running = False
        else:
            source_path = user_input
            dest_path = generate_unique_filename(source_path)
            error_message = process_file(source_path, dest_path)

            output_message = error_message if error_message else f"Новый файл сохранён как {dest_path}"
            print(output_message)


if __name__ == "__main__":
    main()