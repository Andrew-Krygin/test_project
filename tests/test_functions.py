from src.functions import revers_list


def test_reverse_list(number_list):
    assert revers_list(number_list) == [5, 4, 3, 2, 1]

def test_reverse_list_empty():
    assert revers_list([]) == []