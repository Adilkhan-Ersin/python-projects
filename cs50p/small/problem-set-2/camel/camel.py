a = input("camelCase: ")

print("snake_case: ", end="")

for l in a:
    if l.isupper():
        print("_" + l.lower(), end="")
    else:
        print(l, end="")
print()
