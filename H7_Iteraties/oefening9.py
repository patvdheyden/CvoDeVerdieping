from pcinput import getInteger
tafel_van = getInteger("Van welk getal wilt u de tafel zien?")

for i in range (1,11):
    print("{:2}".format(i),"*", tafel_van, "=", tafel_van * i)

