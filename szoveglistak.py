""" 1. Hány Alma/alma van a listában? """
def alma(sz_lista):
    print("1. Feladat")
    db:int = 0
    for i in range(0, len(sz_lista), 1):
        if sz_lista[i].lower() == "alma":
            db += 1
    return db


""" 2. Hány Sz betűvel kezdődő szöveg van a listában? """
def sz(sz_lista):
    print("2. Feladat")
    db:int = 0
    for i in range(0, len(sz_lista), 1):
        if sz_lista[i][0:2] == "Sz":
            db += 1
    return db


""" 3. Melyik a leghosszabb szó? Mekkora a hossza? 
 Hányadik helyen áll a listában? """
def hossza():
    print("3. Feladat")
    