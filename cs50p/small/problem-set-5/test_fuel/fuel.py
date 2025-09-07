def main():
    frac = input("Fraction: ")
    frac_con = convert(frac)
    output = gauge(frac_con)
    print(output)

def convert(fraction):
    while True:
        try:
            num, den = fraction.split("/")
            new_num = int(num)
            new_den = int(den)
            f = new_num / new_den
            if f <= 1:
              percentage = int(f * 100)
              return percentage
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{(percentage)}%"

if __name__ == "__main__":
    main()
