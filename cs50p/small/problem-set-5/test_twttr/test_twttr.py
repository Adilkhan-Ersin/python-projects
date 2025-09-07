from twttr import shorten
def main():
    test_lower()
    test_num()

def test_lower():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwIttEr') == 'Twttr'

def test_num():
    assert shorten('1234') == '1234'

def test_pun():
    assert shorten('!?.,') == '!?.,'

if __name__ == "__main__":
    main()
