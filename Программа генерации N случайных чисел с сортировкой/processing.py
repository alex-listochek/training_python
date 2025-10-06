import random


def generate_numbers(n: int) -> list[int]:

    return [random.randint(-26, 13) for _ in range(n)]


def sort_numbers(numbers: list[int]) -> list[int]:
    
    return sorted(numbers, reverse=True)


def count_negatives(numbers: list[int]) -> int:

    return sum(1 for num in numbers if num < 0)