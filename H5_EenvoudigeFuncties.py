from typing import Any, Union

from termcolor import colored
from math import sqrt, exp, log
import numpy
import GlobaleFuncties as GF
import pcinput as PCI
from random  import random
# Oefening 5.1 #
print("")
print("### Oef 5.1: Bereken de lengte van een string ###")

te_bewerken_string = input("Geef een string in: ")
resultaat1 = "De ingegeven string " + str(te_bewerken_string) + " heeft een lengte van "
resultaat2 = str(len(te_bewerken_string)) + " karakters"

print(GF.box(5, 1, resultaat1 + resultaat2))

# Oefening 5.2 #
print("")
print("### Oef 5.2: Bereken de lengte van een string van de schuine zijde van een rechthoekige driehoek ###")
rechte_zijde1 = input("Geef de lengte van de eerste rechte zijde: ")
rechte_zijde1 = float(rechte_zijde1)
rechte_zijde2 = input("Geef de lengte van de tweede rechte zijde: ")
rechte_zijde2 = float(rechte_zijde2)
schuine_zijde = sqrt(pow(rechte_zijde1, 2) + pow(rechte_zijde2, 2))
schuine_zijde = "{:.2f}".format(schuine_zijde)

gegevens = "Lengte zijdes: " + str(rechte_zijde1) + " en " + str(rechte_zijde2)
resultaat = " De lengte van de schuine zijde is : " + str(schuine_zijde)
print(GF.box(5, 2, gegevens, resultaat))

# Oefening 5.3 #
print("")
print("### Oef 5.3: vergelijk getallen en bereken het gemiddelde ###")
getal1 = PCI.getFloat("Geef getal 1 :")
getal2 = PCI.getFloat("Geef getal 2 :")
getal3 = PCI.getFloat("Geef getal 3 :")
gegevens = "De drie getallen zijn : " + str(getal1) + " , " + str(getal2) + " , " + str(getal3)
resultaat_groot = "Het grootste getal is " + str(max(getal1, getal2, getal3))
resultaat_klein = "Het kleinste getal is " + str(min(getal1, getal2, getal3))
resultaat_gem = "Het gemiddelde van de getallen is " + str("{:.2f}".format(sum((getal1, getal2, getal3)) / 3))
print(GF.box(5, 3, gegevens, resultaat_groot, resultaat_klein, resultaat_gem))

# Oefening 5.4 #
print("")
print("### Oef 5.4: Berekenen de waardes van e tot de macht x  ###")


def expformated(a):
    resultaat_ef = "De waarde van e tot de macht " + str(a) + " is " + str("{:.5f}".format(exp(a)))
    return resultaat_ef


print(GF.box(5, 4, expformated(-1), expformated(0), expformated(1), expformated(2), expformated(3)))

# Oefening 5.5 #
print("")
print("### Oef 5.5: Print een random getal tss van 1 tot 10 met enkel random()  ###")

random_getal = "Een random geheel getal tussen 1 en 10 is " + str(int(random()*10+1))

print(GF.box(5, 5, random_getal))
