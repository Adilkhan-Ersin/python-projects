import pytest
from fuel import convert, gauge

def main():
    test_zero()
    test_value()
    test_correct()

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_value():
    with pytest.raises(ValueError):
        convert('cat/dog')

def test_correct():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

if __name__ == "__main__":
    main()
