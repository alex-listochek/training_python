"""
    Модуль file_reader - извлекает первые 10 строк из текстового файла формата UTF-8.
    Методы:
        get_head_lines() -> str - возвращает массив строк их текстового файла.
"""


def get_head_lines(filename: str, lines_count: int = 10) -> list[str]:
    """
        Метод извлекает первые 10 строк из текстового файла формата UTF-8.
        
        Параметры:
            lines:list - массив для хранения извлечённых строк.
            lines_read:int - число начала отсчёта кол-ва строк для вывода.
            read_more:bool - флаг для выхода из цикла.
        Возвращает:
            lines:list - массив с первыми 10 строками из текстового файла.
    """

    lines = []
    lines_read = 0
    read_more =True
    
    with open(filename, 'r', encoding='utf-8') as file:
        while read_more and lines_read < lines_count:
            line = file.readline()
            if line:
                lines.append(line.rstrip("\n"))
                lines_read += 1
            else:
                read_more = False

    return lines