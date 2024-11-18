import pytest
from string_utils import StringUtils


@pytest.mark.parametrize("string, result", [
    ("привет бобер", "Привет бобер"),
    ("где григорий?", "Где григорий?"),
    ("барабан", "Барабан"),
    ("123", "123"),
    (" ", " "),
    ("white", "White"),
    ])
def test_positive_capitilize(string, result):
    string1 = StringUtils()
    res = string1.capitilize(string)
    assert res == result


@pytest.mark.parametrize("string", [
    None,
    123,
    ["1", "2", "3"]
    ])
def test_negative_capitilize(string):
    string1 = StringUtils()
    with pytest.raises(AttributeError):
        string1.capitilize(string)


@pytest.mark.parametrize("string, result", [
    (" привет", "привет"),
    ("    здрасьте", "здрасьте"),
    ("привет", "привет"),
    (" Привет", "Привет"),
    ("   ", "")
    ])
def test_positive_trim(string, result):
    trim = StringUtils()
    res = trim.trim(string)
    assert res == result


@pytest.mark.parametrize("string", [
    None,
    123,
    ["1", "2", "3"]
    ])
def test_negative_trim(string):
    trim = StringUtils()
    with pytest.raises(AttributeError):
        trim.trim(string)


@pytest.mark.parametrize("string, delimeter, result", [
    ("1,2,3", ",", ["1", "2", "3"]),
    ("ш е р с т ь", " ", ["ш", "е", "р", "с", "т", "ь"]),
    ("1.2.3", ".", ["1", "2", "3"]),
    ("1,2,3", None, ["1", "2", "3"]),
    ("", ",", [])
    ])
def test_positive_to_list(string, delimeter, result):
    to_list = StringUtils()
    if delimeter is None:
        res = to_list.to_list(string)
    else:
        res = to_list.to_list(string, delimeter)
        assert res == result


@pytest.mark.parametrize("string, delimeter", [
        (None, ","),
        (123, ","),
        (["1", "2", "3"], "-"),  # возможно баг в стр 71: вроде должно быть
                                 # TypeError уточнить отличия)
        ("Лос", 123),
        ("Реал", ["1", "2", "3"])
    ])
def test_negative_to_list(string, delimeter):
    to_list = StringUtils()
    with pytest.raises((AttributeError, TypeError)):
        to_list.to_list(string, delimeter)


@pytest.mark.parametrize("string, symbol, bool", [
    ("привет", "р", True),
    ("Привет", "П", True),
    ("привет", "П", False),
    ("", "ф", False),
    ("здоровья", "о", True),
    ("кит", "о", False),
    ("Привет Сима", " ", True)
    ])
def test_positive_contains(string, symbol, bool):
    contains = StringUtils()
    res = contains.contains(string, symbol)
    assert res == bool


@pytest.mark.parametrize("string, symbol", [
        (None, "g"),
        (123, "d"),
        # (["1", "2", "3"], "-"),  # строка принимает массив (баг?)
        ("Лос", 123),
        ("Реал", ["1", "2", "3"]),
    ])
def test_negative_contains(string, symbol):
    contains = StringUtils()
    with pytest.raises((AttributeError, TypeError)):
        contains.contains(string, symbol)


@pytest.mark.parametrize("string, symbol, bool", [
    ("медведь", "ь", True),
    ("Bear", "r", True),
    ("bear 2", "2", True),
    ("dog ", " ", True),
    ("", "", True),
    ("dog", "G", False),
    ("dog!!!", "!", True),
    ("bot", "o", False)
    ])
def test_positive_end_with(string, symbol, bool):
    end_with = StringUtils()
    res = end_with.end_with(string, symbol)
    assert res == bool


@pytest.mark.parametrize("string, symbol", [
    (None, "g"),
    (123, "g"),
    (["1", "2", "3"], "g"),
    ("dog", None),
    ("dog", 1),
    ("dog", ["1", "2", "3"])
    ])
def test_negative_end_with(string, symbol):
    end_with = StringUtils()
    with pytest.raises((AttributeError, TypeError)):  # добавить TypeError
        end_with.end_with(string, symbol)


@pytest.mark.parametrize("string, bool", [
    ("", True),
    ("    ", True),
    ("dog", False),
    ("65", False),
    (".", False),
    ("дом", False),
    ("65 hh f", False),
    ("   !    ", False)
    ])
def test_positive_is_empty(string, bool):
    is_empty = StringUtils()
    res = is_empty.is_empty(string)
    assert res == bool


@pytest.mark.parametrize("string", [
    None,
    123,
    ["1", "2", "3"]
    ])
def test_negative_is_empty(string):
    is_empty = StringUtils()
    with pytest.raises(AttributeError):
        is_empty.capitilize(string)


@pytest.mark.parametrize("lst, joiner, result", [
    ([1, 2, 3], None, "1, 2, 3"),
    (["жили", "были"], "-", "жили-были"),
    (["жили", 1], "", "жили1"),
    ([0, "были"], " ", "0 были"),
    ([11, "были"], "34", "1134были"),
    (["жили", 99889999977], " ! ", "жили ! 99889999977"),
    (["жили", "были"], "да", "жилидабыли")
    ])
def test_positive_list_to_string(lst, joiner, result):
    list_to_string = StringUtils()
    if joiner is None:
        res = list_to_string.list_to_string(lst)
    else:
        res = list_to_string.list_to_string(lst, joiner)
        assert res == result


@pytest.mark.parametrize("lst, joiner", [
    (None, "g"),
    (123, "g"),
    (["1", "AS", "0"], None),
    (["!", "22", "100"], 1)
    ])
def test_negative_list_to_string(lst, joiner):
    list_to_string = StringUtils()
    with pytest.raises((AttributeError, TypeError)):
        list_to_string.list_to_string(lst, joiner)
