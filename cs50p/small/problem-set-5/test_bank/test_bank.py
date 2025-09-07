from bank import value
def main():
    test_0()
    test_20()
    test_100()
def test_0():
    assert value('hello') == 0
    assert value('HELLO') == 0
def test_20():
    assert value('Hey') == 20
    assert value('Hi') == 20
def test_100():
    assert value('Whatup') == 100
    assert value('Wow') == 100
if __name__ == "__main__":
    main()
