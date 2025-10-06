"""
    Модуль error_handler - обрабатывает ошибки возникающие при работе с программой или возвращает первые 10 строк текстового файла.
    Методы:
        safe_get_head_lines() -> str - обрабатывает ошибки и возвращает сообщение с типом ошибки или выводит первые 10 строк текствого файла при корректной работе.
    Импортируемые методы:
        typing из модуля Tuple
        file_reader из модуля get_head_lines
"""
from typing import Tuple
from file_reader import get_head_lines


def safe_get_head_lines(filename: str) -> Tuple[list[str], str]:
    """
        Метод обрабатывает ошибки возникающие при работе с программой 
        
        Параметры:
            error_message:str - хранит и принимает сообщения об ошибке.
            lines:list - массив с первыми 10 строками из текстового файла.
        Возвращает:
            lines:list - массив с первыми 10 строками из текстового файла.
            error_message:str - сообщение с описанием ошибки.
    """
    error_message = ""
    lines = []

    try:
        lines = get_head_lines(filename)
    except FileNotFoundError:
        error_message = "Ошибка: файл не существует." 
    except PermissionError:
        error_message = "Ошибка: недостаточно прав для чтения файла."
    except Exception as e:
        error_message = f"Неизвестная ошибка: {str(e)}"

    return lines, error_message