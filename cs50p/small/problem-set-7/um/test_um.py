from um import count

def main():
    test_upper_lower_case()
    test_um()
    test_space()


def test_upper_lower_case():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2

def test_um():
    assert count('yummi') == 0
    assert count('umbrella') == 0

def test_space():
    assert count('Hello um alex?') == 1
    assert count('Hello um?') == 1

if __name__ == "__main__":
    main()
