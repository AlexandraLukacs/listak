""" 1. Írj metódust, ami paraméterben kapott lista elemeit kiírja a képernyőre"""
def kiiras(lista):
    print("1. Feladat")
    for i in range(0, len(lista), 1):
        print(f"{i}. elem: {lista[i]}")


""" 2. Mennyi a pozitív számok összege? - Összegzés """
def pozitiv(lista):
    print("2. Feladat")
    osszeg:int = 0
    for i in range(0, len(lista), 1):
        if lista[i] > 0:
            osszeg += lista[i]
    return osszeg


""" 3. Hány negatív szám van? - Számlálás """
def negativ(lista):
    print("3. Feladat")
    db:int = 0
    for i in range(0, len(lista), 1):
        if lista[i] < 0:
            db += 1
    return db


""" 4. Hány nem egész szám van a számok között? - Számlálás """
def nemegeszszam(lista):
    print("4. Feladat")
    db:int = 0
    for i in range(0, len(lista), 1):
        if round(lista[i]) != lista[i]:
            db += 1
    return db


""" 5. Mennyi a hárommal osztható számok átlaga? - Összegzés - Számlálás """
def atlag(lista):
    print("5. Feladat")
    osztas:int = 0
    atlag:int = 0 
    for i in range(0, len(lista), 1):
        if lista[i] % 3 == 0:
            osztas += lista[i]
            atlag += 1
    return (osztas / atlag)


""" 6. Mekkora a legnagyobb szám? - Max """
def max(lista):
    print("6. Feladat")
    max:int = lista[0]
    for i in range(0, len(lista), 1):
        if max < lista[i]:
            max = lista[i]
    return max


""" 7. Mekkora a legkisebb szám? - Max """
def min(lista):
    print("7. Feladat")
    min:int = lista[0]
    for i in range(0, len(lista), 1):
        if min > lista[i]:
            min = lista[i]
    return min


""" 8. Mekkora a legkisebb és a legnagyobb szám különbsége?"""
def kulonbseg(lista):
    print("8. Feladat")
    max:int = lista[0]
    min:int = lista[0]
    for i in range(0, len(lista), 1):
        if min > lista[i]:
            min = lista[i]
        elif max < lista[i]:
            max = lista[i]
    return (max - min)