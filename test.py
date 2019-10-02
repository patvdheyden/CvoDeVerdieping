def place_value(number):
    return "{:,}".format(number)


aantalDagenInweek = 7
aantalUrenInDag = 24
aantalMinutenInUur = 60
aantalSecondenInMinuut = 60
resultaat = aantalDagenInweek * aantalUrenInDag * aantalMinutenInUur * aantalSecondenInMinuut
print("Er zijn", place_value(resultaat), "seconden in een week")

print(3 * "zefrzf")
