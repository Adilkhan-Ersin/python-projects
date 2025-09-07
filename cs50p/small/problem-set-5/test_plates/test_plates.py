from plates import is_valid
def main():
    test_char()
    test_numbers()
    test_middle()
    test_zero()
    test_dot()


def test_char():
    assert is_valid('AA') == True
    assert is_valid('AAJ092H') == False
    assert is_valid('A') == False

def test_numbers():
    assert is_valid('AAA222') == True
    assert is_valid('50CS') == False
    assert is_valid('123456') == False
    assert is_valid('AAA22A') == False

def test_middle():
    assert is_valid('AAJ392') == True
    assert is_valid('AA092H') == False

def test_zero():
    assert is_valid('0HFSB') == False
    assert is_valid('HFSB08') == False
    assert is_valid('FHK054') == False

def test_dot():
    assert is_valid('PI3.14') == False
    assert is_valid('AAJ,2H') == False
    assert is_valid('AA 09?') == False

if __name__ == "__main__":
    main()
