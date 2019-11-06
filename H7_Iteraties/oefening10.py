for x in range(2, 101):
    deelbaar = True
    for j in range(2, x+1):
        if x % j == 0 and x != j:
            deelbaar = False
            break
    if deelbaar:
        print("Het getal", str(x), "is een priem getal")
    # print("I:",str(i))
    deelbaar = False
