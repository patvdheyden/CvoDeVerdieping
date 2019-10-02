from typing import Any, Union

from termcolor import colored
from math import sqrt, exp, log
import numpy
import GlobaleFuncties as GF
import pcinput as PCI
from random  import random

# Oefening 5.5 #
print("")
print("### Oef 5.5: Print een random getal tss van 1 tot 10 met enkel random()  ###")

random_getal = "Een random geheel getal tussen 1 en 10 is " + str(int(random()*10+1))

print(GF.box(5, 5, random_getal))
