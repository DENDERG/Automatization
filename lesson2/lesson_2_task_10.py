def bank(x, y):
    for i in range(1, y+1):
        count = x + (x / 10)
        x = count
    print(round(count, 4))


bank(int(input("Размер вклада: ")), int(input("Срок вклада: ")))
