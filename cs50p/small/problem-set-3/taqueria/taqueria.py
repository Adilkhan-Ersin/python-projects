# dictionary
d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
#input
p = 0
while True:
    try:
        k = input("Item: ").title()
        if k in d:
          p += d[k]
          print("Total: $", end="")
          print("{:.2f}".format(p))
    except EOFError:
      print()
      break
