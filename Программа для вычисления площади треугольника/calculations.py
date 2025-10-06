import math


def area_by_three_sides(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area


def area_by_two_sides_and_angle(a: float, b: float, angle: float) -> float:
    rad = math.radians(angle)
    area = 0.5 * a * b * math.sin(rad)
    
    return area
