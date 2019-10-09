from math import exp

import GlobaleFuncties as GF

# Oefening 5.4 #
print("")
print("### Oef 5.4: Berekenen de waardes van e tot de macht x  ###")


def expformated(a):
    str_format = "De waarde van e tot de macht {:>2} is "
    #  resultaat_ef = str_format.format(str(a)) + " is " + str("{:2.5f}".format(exp(a)))
    resultaat_ef = str_format.format(str(a)) +  str(f'{exp(a):9.5f}') # centreren op dec punt

    return resultaat_ef


print(GF.box(5, 4, expformated(-1), expformated(0), expformated(1), expformated(2), expformated(3)))