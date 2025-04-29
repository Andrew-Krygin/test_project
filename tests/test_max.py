import pytest


def test_max(number_list):
    # Проверяем, что максимальное число в списке равно 5
    assert max(number_list) == 5

    with pytest.raises(TypeError):
        test_max(123)