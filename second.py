def cislo_text(cislo):
    if cislo>100:
        return "Číslo mimo rozsah"
    mapa = {1: "jedna", 2: "dva", 3:"tři", 4: "čtyři", 5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9:"devět", 10: "deset", 11:"jedenáct", 12:"dvanáct", 13:"třináct", 14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct", 20: "dvacet", 30: "třicet", 40: "čtyřicet", 50: "padesát", 60: "šedesát", 70: "sedmdesát", 80: "osmdesát", 90: "devadesát", 100: "sto"}
    if cislo<=20:
        return mapa[cislo]
    prvnicislo = cislo//10 
    druhecislo = cislo%10

    if (druhecislo == 0):
        return mapa[prvnicislo * 10]
    
    return mapa[prvnicislo * 10] + mapa[druhecislo]



print (cislo_text(100))

    