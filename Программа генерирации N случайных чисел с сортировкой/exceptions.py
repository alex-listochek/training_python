MAX_REASONABLE_NUMBER = 1_000_000


def is_valid_integer(s: str) -> bool:

    return s.lstrip('-').isdigit()


def is_reasonable_number(n: int) -> bool:

    return abs(n) <= MAX_REASONABLE_NUMBER