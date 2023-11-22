import pytest

@pytest.fixture()
def coord1():
    return "37.7891838", "-122.4033522"


@pytest.fixture()
def text1():
    return "One Montgomery Tower"

@pytest.fixture()
def good_word():
    return "table"

@pytest.fixture()
def bad_word():
    return "tabbl"