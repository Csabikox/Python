#1.feladat: 50-100 között írjuk ki a páratlan számokat
"""
kezdet = 50

while kezdet <= 100:
    
    if kezdet % 2 != 0:
        print(kezdet)
    kezdet = kezdet + 1

"""

#2.feladat: 100x írd ki egymás alá a keresztneved! ("Sorszámozva")

"""

hanyadik = 1

while hanyadik <= 100:
    
    print(f" {hanyadik}. : Szabolcs")
    hanyadik = hanyadik + 1
    
"""


#3.feladat: Bekérünk egy user nevet és passwordot és addig fusson, amig nem kapjuk meg a helyes user neve és passwordot

u = input("Kérem a felhasználó neved:")

p = input("Kérem a jelszavad:")

username = "TesztElek"
password = "alma123"

while u != username or p != password:
    u = input("Kérem a felhasználó neved:")
    p = input("Kérem a jelszavad:")

print("Vége!")





