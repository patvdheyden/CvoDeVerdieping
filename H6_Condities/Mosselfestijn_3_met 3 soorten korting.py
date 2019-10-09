from pcinput import getInteger
from pcinput import getLetter

aantal_mosselen = getInteger("Geef het aantal mosselen-friet in: ")
aantal_khapje = getInteger("Geef het aantal koninginnehapjes in: ")
aantal_drank = getInteger("Geef het aantal drankjes in: ")
aantal_ijsjes = getInteger("Geef het aantal ijsjes in: ")

bedrag_mosselen = aantal_mosselen * 20
bedrag_khapje = aantal_khapje * 10
bedrag_drank = aantal_drank * 2
bedrag_ijsjes = aantal_ijsjes * 3
bedrag_totaal = bedrag_mosselen + bedrag_khapje + bedrag_drank + bedrag_ijsjes

print("\n")
vorm = "{:25}{:>2}{:<6}{:>8.2f} euro"
print(vorm.format("Mosselen - friet", aantal_mosselen, " stuks", bedrag_mosselen))
print(vorm.format("Koninginnehapje - friet", aantal_khapje, " stuks", bedrag_khapje))
print(vorm.format("drankjes", aantal_drank, " stuks", bedrag_drank))
print(vorm.format("ijsjes", aantal_ijsjes, " stuks", bedrag_ijsjes))
print("{:25}{:>2}{:<6}{:>8}".format("", "", "", "============="))
# -print(vorm.format("","","________"))
print(vorm.format("Totaal te betalen:", "", "", bedrag_totaal))
print("*" * len(vorm.format("", "", "", 0)))

# Berekenen korting
# indien aantal_mosselen >= 2 dan korting --> 150=20€, 100=12€ en 50=5€
bedrag_tebetalen = bedrag_totaal
bedrag_korting = 0
if aantal_mosselen >= 2:
    if bedrag_totaal >= 150:
        bedrag_korting = 20
    elif bedrag_totaal >= 100:
        bedrag_korting = 12
    elif bedrag_totaal >= 50:
        bedrag_korting = 5
    bedrag_tebetalen = bedrag_totaal - bedrag_korting
if bedrag_korting > 0:
    print(vorm.format("Toegekende korting:", "", "", - bedrag_korting))
    print(vorm.format("Totaal te betalen:", "", "", bedrag_tebetalen))
    print("-" * len(vorm.format("", "", "", 0)))

# Uitbreiding 1 - ontvangen bedrag
bedrag_ontvangen = getInteger("Ontvangen bedrag: ")
bedrag_terug = bedrag_ontvangen - bedrag_tebetalen
print(vorm.format("Terug te geven: ", "", "", bedrag_terug))

# Uitbreiding 2 - terug te geven waarden
terug_20 = bedrag_terug // 20
rest = bedrag_terug % 20
terug_10 = rest // 10
rest = rest % 10
terug_5 = rest // 5
rest = rest % 5
terug_2 = rest // 2
rest = rest % 2
terug_1 = rest // 1

# print(terug_20,"x20€, ",terug_10,"x10€, ",terug_5,"x5€, ",terug_2,"x2€, ",terug_1,"x1€")
vorm = "{:25}{:>2}{:>17}"
print(vorm.format("", "", "20€ x"), terug_20)
print(vorm.format("", "", "10€ x"), terug_10)
print(vorm.format("", "", "5€ x"), terug_5)
print(vorm.format("", "", "2€ x"), terug_2)
print(vorm.format("", "", "1€ x"), terug_1)


