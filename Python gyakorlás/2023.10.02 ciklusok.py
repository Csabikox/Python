# for-ciklus 1-10 közötti számok kiíratása!
"""
for x in range(1,11,1):
    print(x)
    
"""

# 1 és 100 között minden 3. szám kiíratása!
"""
for x in range(1,101,3):
    print(x)
    
"""


# 100-50 között csökkenőbe!
"""
for x in range(100,49,-1):
    print(x)
"""

# 100. írjuk ki a keresztnevünket ( + legyen sorszámozva )

"""

for x in range(1,101,1):
    print(f"{x}. kör: Szabolcs")

"""

# 5 szám bekérése és kiértékelés 3-mal oszthatósága!
"""
for x in range(1,6,1):
    
    szam = int(input(f"Kérem a(z) {x}. számot:"))
    if szam % 3 == 0:
        print(f"A(z) {szam} osztható 3-mal!")
    else:
        print(f"A(z) {szam} NEM osztható 3-mal!")
"""

# 500-1000 között írjuk ki a 3-mal és 5-el osztható számokat!

"""

for x in range(500,1001,1):
    if x % 3 == 0 and x % 5 == 0:
        print(x)
        
"""

#1.feladat: Kérjünk be a felhasználótól 10 db egész számot, vizsgáljuk meg, hogy a megadott érték osztható e 2-vel vagy 3-mal (" teljes kiértékelés ")
""""
for x in range(1,11,1):
    
    szam = int(input("Kérlek add meg a {x}. számot:"))
    
    if szam % 2 == 0 and szam % 3 == 0:
        print(f"Osztható 2-vel vagy 3-mal!")
    else:
        print(f"Nem osztható 2-vel vagy 3-mal!")
        
"""



#2.feladat: Kérjünk be a felhasználótól 5 db zöldség nevet és megkellene vizsgálni, hogy az első és az utolsó karakter ugyan az e (" teljes kiértékelés ")
"""
for x in range(1,6,1):
    z = input("Kérlek add meg a zöldség nevet:")
    if z[0] == z[-1]:
        print("Egyforma az első és utolsó!")
    else:
        print("Különböző!")
     
"""

#3.feladat: 20-30 között adjuk össze a páratlan értékeket és írjuk ki
"""
osszeguk = 0

for x in range(20,31,1):
    if x % 2 != 0:
        osszeguk = osszeguk + x
print(f"Az összegük a páratlanoknak: {osszeguk}")
"""