kostPrijsBoek = 24.95
kortingInkoop = 0.40
verzendingEersteBoek = 3
verzendingRest = 0.75
aantalBoeken = 60
kostVoorBoeken = (aantalBoeken * kostPrijsBoek * (1 - kortingInkoop)) + verzendingEersteBoek + ((aantalBoeken - 1) * verzendingRest)

print("De kostprijs voor de boeken is ", kostVoorBoeken)
