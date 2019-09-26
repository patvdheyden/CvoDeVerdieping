from termcolor import colored
from math import sqrt

import GlobaleFuncties as GF

print ("")
print ("### Oef 5.1: Bereken de lengte van een string ###")

te_bewerken_string = input("Geef een string in: ")
resultaat1 = "De ingegeven string " + str(te_bewerken_string) + " heeft een lengte van "
resultaat2 = str(len(te_bewerken_string)) + " karakters"

print(GF.box(5, 1, resultaat1 + resultaat2))

print ("")
print ("### Oef 5.2: Bereken de lengte van een string ###")
rechtezijde1 = input ("Geef de lengte van de eerste rechte zijde")