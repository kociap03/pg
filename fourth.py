def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    radek, sirka = figurka["pozice"]
    cil_radek, cil_sirka = cilova_pozice

    if cil_radek < 1 or cil_radek > 8 or cil_sirka < 1 or cil_sirka > 8:
        return False

    if (cil_radek, cil_sirka) in obsazene_pozice:
        return False

    if typ == "pěšec":
        if cil_sirka == sirka and cil_radek == radek + 1:
            return True
        if radek == 2 and cil_sirka == sirka and cil_radek == radek + 2 and (radek+1, sirka) not in obsazene_pozice:
            return True
        return False

    if typ == "jezdec":
        dr = cil_radek - radek
        ds = cil_sirka - sirka
        if (dr == 2 and ds == 1) or (dr == 2 and ds == -1) or \
           (dr == -2 and ds == 1) or (dr == -2 and ds == -1) or \
           (dr == 1 and ds == 2) or (dr == 1 and ds == -2) or \
           (dr == -1 and ds == 2) or (dr == -1 and ds == -2):
            return True
        return False

    if typ == "věž":
        if radek == cil_radek:
            step = 1 if cil_sirka > sirka else -1
            col = sirka + step
            while col != cil_sirka:
                if (radek, col) in obsazene_pozice:
                    return False
                col += step
            return True
        if sirka == cil_sirka:
            step = 1 if cil_radek > radek else -1
            row = radek + step
            while row != cil_radek:
                if (row, sirka) in obsazene_pozice:
                    return False
                row += step
            return True
        return False

    if typ == "střelec":
        dr = cil_radek - radek
        ds = cil_sirka - sirka
        if dr == ds or dr == -ds:
            step_r = 1 if cil_radek > radek else -1
            step_s = 1 if cil_sirka > sirka else -1
            row = radek + step_r
            col = sirka + step_s
            while row != cil_radek and col != cil_sirka:
                if (row, col) in obsazene_pozice:
                    return False
                row += step_r
                col += step_s
            return True
        return False

    if typ == "dáma":
        if je_tah_mozny({"typ": "věž", "pozice": (radek, sirka)}, (cil_radek, cil_sirka), obsazene_pozice):
            return True
        if je_tah_mozny({"typ": "střelec", "pozice": (radek, sirka)}, (cil_radek, cil_sirka), obsazene_pozice):
            return True
        return False

    if typ == "král":
        dr = cil_radek - radek
        ds = cil_sirka - sirka
        if dr in (-1, 0, 1) and ds in (-1, 0, 1) and not (dr == 0 and ds == 0):
            return True
        return False

    return False



if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True