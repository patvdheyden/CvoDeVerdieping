from random import randint
from pcinput import getInteger
cijfer_percent = 0

for i in range(10):
    cijfer1 = randint(0, 1000)
    cijfer2 = randint(0, 1000)
    som = cijfer1 + cijfer2
    antwoord_str = "{:4}".format(str(cijfer1)) +  " + " + "{:4}".format(str(cijfer2)) +  " = ? "
    antwoord = getInteger(antwoord_str)
    if int(antwoord) == som:
        cijfer_percent += 10

print("U heeft", cijfer_percent, "% behaald")

