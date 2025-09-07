from seasons import check_birth

def main():
    test_check_birthday()


def test_check_birthday():
    assert check_birth('2005-10-11') == ("2005", "10", "11")
    assert check_birth('2005-24-1') == None
    assert check_birth('August 18, 2006') == None


if __name__ == "__main__":
    main()
