import math


def calculate_circumference(radius: float) -> float:
    result = None
    try:
        result = 2 * math.pi * radius
    except OverflowError:
        result = float('inf')

    return result


def calculate_area(radius: float) -> float:
    result = None
    try:
        result = math.pi * radius ** 2
    except OverflowError:
        result = float('inf')
        
    return result
