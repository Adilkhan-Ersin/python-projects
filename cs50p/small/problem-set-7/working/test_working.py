from working import convert
import pytest

def main():
    test_wrong_f()
    test_time()
    test_wrong_h()
    test_wrong_m()

def test_wrong_f():
    with pytest.raises(ValueError):
        convert('9 AM - 9 PM')

def test_time():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

def test_wrong_h():
    with pytest.raises(ValueError):
        convert('14 PM to 18 PM')

def test_wrong_m():
    with pytest.raises(ValueError):
        convert('9:60 AM to 8:60 PM')
