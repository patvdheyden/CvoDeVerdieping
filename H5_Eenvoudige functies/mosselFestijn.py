import GlobaleFuncties as GF

prijs_mossel_met_frietjes = 20
prijs_koninginne_hapje = 10
prijs_ijs = 3
prijs_drank = 2

aantal_mossel_met_frietjes = input("Geef het aantal mossem met frietjes in: ")
aantal_koninginne_hapje = input("Geef het aantal koninginnehapjes in: ")
aantal_ijs = input("Geef het aantal ijsjes in: ")
aantal_drank = input("Geef het aantal duvels in: ")

aantal_mossel_met_frietjes = int(aantal_mossel_met_frietjes)
aantal_koninginne_hapje = int(aantal_koninginne_hapje)
aantal_ijs = int(aantal_ijs)
aantal_drank = int(aantal_drank)

totaal_te_betalen = aantal_mossel_met_frietjes * prijs_mossel_met_frietjes
totaal_te_betalen += aantal_koninginne_hapje * prijs_koninginne_hapje
totaal_te_betalen += aantal_ijs * prijs_ijs
totaal_te_betalen += aantal_drank * prijs_drank


print("")

str_format = "{:<30}{:>8}{:>8} euro"
str_mosselen = str_format.format("Aantal mosselen-friet", aantal_mossel_met_frietjes , aantal_mossel_met_frietjes * prijs_mossel_met_frietjes)
str_kon_hapje = str_format.format("Aantal koninginnehapje", aantal_koninginne_hapje , aantal_koninginne_hapje * prijs_koninginne_hapje)
str_drank = str_format.format("Aantal drankjes", aantal_drank , aantal_drank * prijs_drank)
str_ijs = str_format.format("Aantal ijs", aantal_ijs , aantal_ijs * prijs_ijs)
str_te_betalen = "{:<38}{:>8} euro".format("Totaal te betalen : " , totaal_te_betalen)
str_lijn = "{:<41}{:>10}".format(".", "==========")

print(GF.box(5,6, str_mosselen, str_kon_hapje, str_drank, str_ijs,str_lijn , str_te_betalen ))
print("")
ontvangen_bedrag = input("Geef het ontvangen bedrag in: ")
ontvangen_bedrag = int(ontvangen_bedrag)

wissel_geld = ontvangen_bedrag - totaal_te_betalen
str_wisselen = "Terug te betalen " + str(wissel_geld) + " euro"


resultaat_200_euro = wissel_geld // 200
rest_200_euro = wissel_geld % 200

resultaat_100_euro = rest_200_euro // 100
rest_100_euro = rest_200_euro % 100

resultaat_50_euro = rest_100_euro // 50
rest_50_euro = rest_100_euro % 50

resultaat_20_euro = rest_50_euro // 20
rest_20_euro = rest_50_euro % 20

resultaat_10_euro = rest_20_euro // 10
rest_10_euro = rest_20_euro % 10

resultaat_5_euro = rest_10_euro // 5
rest_5_euro = rest_10_euro % 5

resultaat_5_euro = rest_10_euro // 5
rest_5_euro = rest_10_euro % 5

resultaat_2_euro = rest_5_euro // 2
resultaat_1_euro = rest_5_euro % 2

str_resultaat_200 = "Terug te geven 200 euro: " + str(resultaat_200_euro)
str_resultaat_100 = "Terug te geven 100 euro: " + str(resultaat_100_euro)
str_resultaat_50 = "Terug te geven 50 euro: " + str(resultaat_50_euro)
str_resultaat_20 = "Terug te geven 20 euro: " + str(resultaat_20_euro)
str_resultaat_10 = "Terug te geven 10 euro: " + str(resultaat_10_euro)
str_resultaat_5 = "Terug te geven 5 euro: " + str(resultaat_5_euro)
str_resultaat_2 = "Terug te geven 2 euro: " + str(resultaat_2_euro)
str_resultaat_1 = "Terug te geven 1 euro: " + str(resultaat_1_euro)


print(GF.box(5,6, str_resultaat_200, str_resultaat_100, str_resultaat_50,str_resultaat_20,str_resultaat_10,str_resultaat_5,str_resultaat_2,str_resultaat_1 ))