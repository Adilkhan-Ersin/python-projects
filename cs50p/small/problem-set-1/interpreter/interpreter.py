exp=input('Expression: ')
x, y, z = exp.split(" ")

n_x = float(x)
n_z = float(z)

if y == "+" :
    result = n_x + n_z

if y == "-" :
    result = n_x - n_z

if y == "*" :
    result = n_x * n_z

if y == "/" :
    result = n_x / n_z
print(result)
