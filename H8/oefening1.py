from pcinput import getInteger

intGetal = getInteger("Geef een getal kleiner of gelijk aan 10: ")
printRegel =""
for i in range(1,intGetal+1):

    for j in range(1,intGetal+1):
        printRegel += "  {:8} |".format(str(j)+"x"+str(i)+" = "+ str(i*j))

    print(printRegel)
    printRegel = ""

