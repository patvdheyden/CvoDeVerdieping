from math import sqrt

import GlobaleFuncties as GF

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