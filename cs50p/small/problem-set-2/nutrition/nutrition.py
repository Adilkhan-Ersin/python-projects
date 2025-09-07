d = {"apple": 130, "avocado": 50, "banana": 110, "grapefruit": 60, "sweet cherries": 100, "kiwifruit": 90, "pear": 100}

k = input("Item: ").lower()
if k in d:
    print(f"Calories {d[k]}")
