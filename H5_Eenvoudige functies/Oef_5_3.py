from typing import Any, Union

from termcolor import colored
from math import sqrt, exp, log
import numpy
import GlobaleFuncties as GF
import pcinput as PCI
from random  import random

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