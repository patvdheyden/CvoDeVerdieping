from random import randint
from pcinput import getInteger
cijfer_percent = 0
resultaat_str = ""
for i in range(5):
    cijfer1 = randint(0, 1000)
    cijfer2 = randint(0, 1000)
    som = cijfer1 + cijfer2
    antwoord_str = "{:4}".format(str(cijfer1)) +  " + " + "{:4}".format(str(cijfer2)) +  " = "
    resultaat_str += antwoord_str + str(som) + "\n"
    antwoord = getInteger(antwoord_str + "?")
    if int(antwoord) == som:
        cijfer_percent += 20
print ("")
print(resultaat_str)
print("U heeft", cijfer_percent, "% behaald")
if cijfer_percent >= 50:
    print("u bent geslaagt")
else:
    print("Helaas niet geslaagd")

