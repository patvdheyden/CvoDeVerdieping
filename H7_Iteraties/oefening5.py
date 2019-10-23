from pcinput import getInteger
geheel_getal = getInteger("Geef een geheel getal in:")
som = 0
for x in range (1, geheel_getal +1 ):
    som += x

print("De totale som is", som )

