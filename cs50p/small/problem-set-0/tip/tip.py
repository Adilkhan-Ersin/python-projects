def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    a=d.replace('$','')
    return float(a)

def percent_to_float(p):
    # TODO
    b=p.replace('%','')
    c=float(b)/100
    return c

main()