def main():
    message = input("Input: ")
    message_wit = shorten(message)
    print("Output: " + message_wit)

def shorten(word):
    word_wit = ""
    for letter in word:
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            word_wit += letter
    return word_wit

if __name__ == "__main__":
    main()
