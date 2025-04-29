import pytest


from src.functions import revers_list, reverse_string, func


def test_reverse_list(number_list):
    assert revers_list(number_list) == [5, 4, 3, 2, 1]


def test_reverse_list_empty():
    assert revers_list([]) == []


@pytest.mark.parametrize("string, expected_result", [
    ("hello", "olleh"),
    ("world", "dlrow"),
    ("12345", "54321"),
    ("", ""),
])
def test_reverse_string(string, expected_result):
    assert reverse_string(string) == expected_result


def test_func():
    assert func([1, 2, 3, [3, 4], {}, (4,), "12", "ghb"], int) == 3
    assert func([], str) == 0
    assert func(["1232213"], float) == 0
    with pytest.raises(TypeError):
        func(123, str)
