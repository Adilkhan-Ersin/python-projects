# dictionary
d = {}
#input
while True:
    try:
        k = input().lower()
        if k in d:
          d[k] += 1
        else:
          d[k] = 1
    except EOFError:
      for k in sorted(d.keys()):
        print(d[k], k.upper())
      break
