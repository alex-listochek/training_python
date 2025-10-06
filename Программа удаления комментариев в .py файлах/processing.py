"""Модуль обработки файлов, включая генерацию уникального имени и удаление комментариев."""

"""
    Модуль processing - обрабатывает полученный файл с типом .py, удаляет из него комментарии и генерирует его копию без комментариев.
    Методы:
        generate_unique_filename(original_path:str) -> str: генерирует уникальное имя файла, добавляя счетчик к имени.
        remove_comments(line:str) -> str: удаляет комментарии из строки кода.
        process_file(source_path:str, dest_path:str) -> None: обрабатывает файл, удаляя комментарии и сохраняя результат в новый файл.
    Импортируемые методы:
        все методы из модуля os
        read_file, write_file из модуля errors
"""

import os
from errors import read_file, write_file


def generate_unique_filename(original_path):
    """
    Генерирует уникальное имя файла, добавляя счетчик к имени.

    Параметры:
        base:Any, ext:Any - разделяет имя файла на его название и тип.
        counter:int - число, которое будет прибавляться к имени сгенерированного файла.
        new_path:str - новое имя для сгенерированного файла.
    Возвращает:
        str - новое имя для сгенериованного файла.
    """
    base, ext = os.path.splitext(original_path)
    counter = 1
    new_path = f"{base}_{counter}{ext}"

    while os.path.exists(new_path):
        counter += 1
        new_path = f"{base}_{counter}{ext}"

    return new_path


def remove_comments(line):
    """
    Удаляет комментарии из строки кода.

    Параметры:
        comment_pos:Any - поиск сопадения в строках со знаком #
        new_str:Any - ищет комментари после знака # и в последующих строках.
    Возвращает:
        Any - строка без комментариев.
    """
    comment_pos = line.find('#')
    new_str = line[:comment_pos] if comment_pos != -1 else line

    return new_str


def process_file(source_path, dest_path):
    """
    Обрабатывает файл, сохраняя результат в новый файл.

    Параметры:
        content:None, error:str - читает содержимое файла или возвращает ошибку.
        processed_content:str - удаляет комментарии из строк в которых они содержаться.
        error:str|None - пропускает строку без комментариев.
    Возвращает:
        str|None - строку с удалённым комментарием или ничего.
    """
    content, error = read_file(source_path)
    processed_content = None

    if not error:
        processed_content = [remove_comments(line) for line in content]
        error = write_file(dest_path, processed_content)

    return error