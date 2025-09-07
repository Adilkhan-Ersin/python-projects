import random

while True:
    try:
        lvl = int(input("Level: "))
        r_ans = random.randint(1, lvl)
        if lvl < 1:
            pass
        if lvl < 101:
            break
    except ValueError:
        pass

while True:
    try:
        gue = int(input("Guess: "))
        if gue < r_ans:
            print("Too small!")
        elif gue > r_ans:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass

