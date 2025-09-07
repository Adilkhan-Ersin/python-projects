from datetime import date
import inflect
import sys
import re

p = inflect.engine()


def main():
    birthday = input("Date of Birth: ")
    try:
        year, month, day = check_birth(birthday)
    except:
        sys.exit("Invalid Date")

    date_birth = date(int(year), int(month), int(day))
    date_today = date.today()
    real = date_today - date_birth
    minute = real.days * 24 * 60
    out = p.number_to_words(minute, andword="")
    print(out.capitalize() + " minutes")


def check_birth(birthday):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthday):
        year, month, day = birthday.split("-")
        return year, month, day



if __name__ == "__main__":
    main()
