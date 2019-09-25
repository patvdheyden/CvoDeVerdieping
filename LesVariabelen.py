from termcolor import colored

def avg(l):
    return sum(l, 0.0) / len(l)

print ("Oefening 4.1")
lijst = [15,26,36]
print ("Het gemiddelde van " + str(lijst) + " is " + str("{:.2f}".format(avg(lijst)))) # afronden print 2 dec
print("")
print ("Oefening 4.2")

straal = 5
PI = 3.14159
oppervlakte = (straal**2)*PI
print ( "De oppervlakte van een cirkel met een straal van " + str(straal) + " is " + str("{:.2f}".format(oppervlakte)) )

print("")
print ("Oefening 4.3")

aantal_centen = 1287

resultaat_dollar = aantal_centen // 100
rest_dollar = aantal_centen % 100

resultaat_kwartjes = rest_dollar // 25
rest_kwartjes = rest_dollar % 25

resultaat_dubbeltjes = rest_kwartjes // 10
rest_dubbeltjes = rest_kwartjes % 10

resultaat_stuivers = rest_dubbeltjes // 5
resultaat_centjes =  rest_dubbeltjes % 5

print ("In het bedrag " + str(aantal_centen))
print ("zitten er " + str(resultaat_dollar) +" dollars")
print ("zitten er " + str(resultaat_kwartjes) + " kwartjes")
print ("zitten er " + str(resultaat_dubbeltjes) + " dubbeltjes")
print ("zitten er " + str(resultaat_stuivers) + " stuivers")
print ("zitten er " + str(resultaat_centjes) + " centjes")


print("")
print ("Oefening 4.4")
waarde1 = 45
waarde2 = 96
print ("waardes voor de switch", waarde1, waarde2)
waarde1,waarde2 = waarde2,waarde1
print ("waardes na de switch", waarde1, waarde2)

print("")
print ("Oefening 4.5")

fahrenheit = 50
celsius = (fahrenheit-32)/1.8
print (str(fahrenheit) +" graden fahrenheit = " +str(celsius) + " graden celsius")
print (colored('test','red'))
