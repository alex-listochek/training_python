"""
    Модуль errors - работа с файлами с обработкой ошибок.
    Методы:
        read_file(filepath) -> str: обработка ошибок при чтении содержимого файла.
        write_file(filepath, content) -> str: обработка ошибок при записи содержимого файла.
"""

def read_file(filepath):
    """
    Обрабатывает ошибки при чтении файла.
    Параметры:
        content:str - принимает в себя содержимое файла.
        error_message:str - принимает сообщение об ошибке.
    Возвращает:
        str - сообщение об ошибке или содержимое файла.
    """
    content = None
    error_message = None

    try:
        with open(filepath, 'r') as f:
            content = f.readlines()
    except FileNotFoundError:
        error_message = f"Файл '{filepath}' не найден."
    except PermissionError:
        error_message = f"Нет прав на чтение файла '{filepath}'."
    except IOError as e:
        error_message = f"Ошибка ввода/вывода: {str(e)}"
    except Exception as e:
        error_message = f"Неизвестная ошибка: {str(e)}"

    return content, error_message


def write_file(filepath, content):
    """
    Обрабатывает ошибки при записе нового файла.
    Параметры:
        error_message:str - принимает сообщение об ошибке.
    Возвращает:
        str - сообщение об ошибке.
    """
    error_message = None

    try:
        with open(filepath, 'w') as f:
            f.writelines(content)
    except PermissionError:
        error_message = f"Нет прав на запись в файл '{filepath}'."
    except IOError as e:
        error_message = f"Ошибка ввода/вывода: {str(e)}"
    except Exception as e:
        error_message = f"Неизвестная ошибка: {str(e)}"

    return error_message