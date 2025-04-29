from typing import Any

def revers_list(lst: list[Any]) -> list[Any]:
    """Функция переворачивает список."""
    return lst[::-1]

def reverse_string(string: str) -> str:
    """Функция переворачивает строку."""
    return string[::-1]


def func(lst: list[Any], my_type: type) -> int:
    if isinstance(lst, list):
        return len([x for x in lst if isinstance(x, my_type)])
    raise TypeError("Ошибка: должен быть список!")


def max_num(lst: list[int | float]) -> int | float:
    if isinstance(lst, list):
        return max(lst)
    raise TypeError("Должен быть список!")