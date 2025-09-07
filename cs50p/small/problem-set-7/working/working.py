import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    correct = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if correct:
        p = correct.groups()
        if int(p[1]) > 12 or int(p[5]) > 12:
            raise ValueError
        time = format(p[1], p[2], p[3])
        sec_time = format(p[5], p[6], p[7])
        return time + ' to ' + sec_time
    else:
        raise ValueError


def format(hour, minute, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            h = 12
        else:
            h = int(hour) + 12
    else:
        if int(hour) == 12:
            h = 0
        else:
            h = int(hour)
    if minute == None:
        m = ':00'
        t = f"{h:02}" + m
    else:
        t = f"{h:02}" + ":" + minute
    return t


if __name__ == "__main__":
    main()
