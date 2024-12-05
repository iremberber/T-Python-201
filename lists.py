#Veri yapıları

notlar= [90,80,50]
type(notlar)

liste = ["a", 19.3 , 92]

len(liste)

type(liste[0])

tumliste = [notlar, liste]

type(tumliste[1][0])

kisiler = ["ali", "veli", "berkcan", "ayse"]
type(kisiler)

kisiler[1] = "velinin babası"

kisiler

kisiler[0:3] = "alinin babası", "bercanın babası", "aysenin annesi"

kisiler + ["kemal"]

del kisiler[2]
kisiler

kisiler.append("ayca")
kisiler

kisiler.remove("ayca")
kisiler

kisiler.insert(0, "fatma")
kisiler

kisiler.insert(len(kisiler), "beren")


kisiler.pop(2)
kisiler 

kisiler.count("beren")

Kisiler_yedek = kisiler.copy()

sayi= 1,2,3,4,5

kisiler.extend(sayi)
kisiler 

kisiler.index("beren")

kisiler.reverse()
kisiler

newlist = [90, 70, 80, 110]

newlist.sort()
newlist 

newlist.clear()
newlist