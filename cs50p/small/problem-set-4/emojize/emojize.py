import emoji

user_input = input("Input: ")
emot = emoji.emojize(f'Output: {user_input}', language='alias')
print(emot)
