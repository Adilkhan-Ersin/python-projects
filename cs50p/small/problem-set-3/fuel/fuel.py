while True:
    k = input("Fraction: ")
    try:
          num, den = k.split("/")
          new_num = int(num)
          new_den = int(den)

          f = new_num / new_den

          if f <= 1:
            break

    except (ValueError, ZeroDivisionError):
      pass
p = int(round(f * 100))

if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")
