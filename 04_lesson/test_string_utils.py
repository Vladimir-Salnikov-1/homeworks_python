import pytest
from string_utils import StringUtils


@pytest.mark.parametrize("string, result",
                         [("привет бобер", "Привет бобер"),
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


@pytest.mark.parametrize("string", [None, 123, ["1", "2", "3"]])
def test_negative_capitilize(string):
    string1 = StringUtils()
    with pytest.raises(AttributeError):
        string1.capitilize(string)


@pytest.mark.parametrize("string, result", [(" привет", "привет"),
                                            ("    здрасьте", "здрасьте"),
                                            ("привет", "привет"),
                                            (" Привет", "Привет"),
                                            ("   ", "")])
def test_positive_trim(string, result):
    trim = StringUtils()
    res = trim.trim(string)
    assert res == result


@pytest.mark.parametrize("string, delimeter, result",
                         [("1,2,3", ",", ["1", "2", "3"]),
                          ("ш е р с т ь", " ",
                           ["ш", "е", "р", "с", "т", "ь"]),
                          ("1.2.3", ".", ["1", "2", "3"]),
                          ("1,2,3", None, ["1", "2", "3"]),
                          ("", ",", [])])
def test_positive_to_list(string, delimeter, result):
    to_list = StringUtils()
    if delimeter is None:
        res = to_list.to_list(string)
    else:
        res = to_list.to_list(string, delimeter)
        assert res == result


@pytest.mark.parametrize("string, symbol, bool", [("привет", "р", True),
                                                  ("Привет", "П", True),
                                                  ("привет", "П", False),
                                                  ("", "ф", False),
                                                  ("здоровья", "о", True),
                                                  ("кит", "о", False),
                                                  ("Привет Сима", " ", True)])
def test_positive_contains(string, symbol, bool):
    contains = StringUtils()
    res = contains.contains(string, symbol)
    assert res == bool


@pytest.mark.parametrize("string, symbol, bool", [("медведь", "ь", True),
                                                  ("Bear", "r", True),
                                                  ("bear 2", "2", True),
                                                  ("dog ", " ", True),
                                                  ("", "", True),
                                                  ("dog", "G", False),
                                                  ("dog!!!", "!", True),
                                                  ("bot", "o", False)])
def test_positive_end_with(string, symbol, bool):
    end_with = StringUtils()
    res = end_with.end_with(string, symbol)
    assert res == bool


@pytest.mark.parametrize("string, bool", [("", True),
                                          ("    ", True),
                                          ("dog", False),
                                          ("65", False),
                                          (".", False),
                                          ("дом", False),
                                          ("65 hh f", False),
                                          ("   !    ", False)])
def test_positive_is_empty(string, bool):
    is_empty = StringUtils()
    res = is_empty.is_empty(string)
    assert res == bool


@pytest.mark.parametrize("lst, joiner, result", [
    ([1, 2, 3], None, "1, 2, 3"),
    (["жили", "были"], "-", "жили-были"),
    (["жили", "были"], "", "жилибыли"),
    (["жили", "были"], " ", "жили были"),
    (["жили", "были"], "34", "жили34были"),
    (["жили", "были"], " ! ", "жили ! были"),
    (["жили", "были"], "да", "жилидабыли")
    ])
def test_positive_list_to_string(lst, joiner, result):
    list_to_string = StringUtils()
    if joiner is None:
        res = list_to_string.list_to_string(lst)
    else:
        res = list_to_string.list_to_string(lst, joiner)
        assert res == result
