from typing import Any, Union

from termcolor import colored
from math import sqrt, exp, log
import numpy
import GlobaleFuncties as GF
import pcinput as PCI
from random  import random


# Oefening 5.4 #
print("")
print("### Oef 5.4: Berekenen de waardes van e tot de macht x  ###")


def expformated(a):
    resultaat_ef = "De waarde van e tot de macht " + str(a) + " is " + str("{:.5f}".format(exp(a)))
    return resultaat_ef


print(GF.box(5, 4, expformated(-1), expformated(0), expformated(1), expformated(2), expformated(3)))