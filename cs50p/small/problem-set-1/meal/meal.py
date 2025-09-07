def main():
    answer = input('What time is it? ')
    time = convert(answer)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    if 12.0 <= time <= 13.0:
        print("lunch time")
    if 18.0 <= time <= 19.0:
        print("dinner time")

def convert(time):
    x, y = time.split(":")

    minute = float(y) / 60
    return float(x) + minute


if __name__ == "__main__":
    main()
