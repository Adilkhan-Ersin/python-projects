from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1') == False

def test_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'500.34.25.250') == False
    assert validate(r'1.500.25.250') == False
    assert validate(r'1.34.500.250') == False
    assert validate(r'1.34.25.500') == False

if __name__ == "__main__":
    main()
