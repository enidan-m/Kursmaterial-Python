#==================================THEMA: DICTIONARIES==================================
#
# AUFGABE 1: TELEFONBUCH (SEHR EINFACH)
#

phonebook = {}

name1 = input("Name 1: ")
nummer1 = input("Telefonnummer 1: ")
phonebook[name1] = nummer1

name2 = input("Name 2: ")
nummer2 = input("Telefonnummer 2: ")
phonebook[name2] = nummer2

name3 = input("Name 3: ")
nummer3 = input("Telefonnummer 3: ")
phonebook[name3] = nummer3

print("Telefonbuch:", phonebook)

suche = input("Welchen Namen suchst du? ")
if suche in phonebook:
    print(suche, "hat die Nummer", phonebook[suche])
else:
    print(suche, "nicht gefunden")


#
# AUFGABE 2: NOTENSPEICHER (SEHR EINFACH)
#

grades = {}

fach1 = input("Fach 1: ")
note1 = float(input("Note 1: "))
grades[fach1] = note1

fach2 = input("Fach 2: ")
note2 = float(input("Note 2: "))
grades[fach2] = note2

fach3 = input("Fach 3: ")
note3 = float(input("Note 3: "))
grades[fach3] = note3

print("Noten:")
for fach, note in grades.items():
    print(fach + ":", note)

durchschnitt = sum(grades.values()) / len(grades)
print("Durchschnitt:", durchschnitt)


#
# AUFGABE 3: LÄNDER-HAUPTSTÄDTE (SEHR EINFACH)
#

countries = {"Deutschland": "Berlin", "Frankreich": "Paris", "Italien": "Rom"}

print("Länder:", ", ".join(countries.keys()))

land = input("Gib ein Land ein: ")
if land in countries:
    print("Die Hauptstadt von", land, "ist", countries[land])
else:
    print(land, "nicht gefunden")


#
# AUFGABE 4: WÖRTERBUCH ERWEITERN (SEHR EINFACH)
#

my_dict = {}

my_dict["name"] = "Anna"
my_dict["alter"] = 25
my_dict["stadt"] = "Berlin"
print("Nach Hinzufügen:", my_dict)

my_dict["alter"] = 26
print("Nach Ändern:", my_dict)

del my_dict["stadt"]
print("Nach Löschen:", my_dict)


#
# AUFGABE 5: EINKAUFSZETTEL (EINFACH MIT SCHLEIFE)
#

shopping_list = {}

for i in range(3):
    produkt = input("Produkt " + str(i+1) + ": ")
    menge = input("Menge: ")
    shopping_list[produkt] = menge

print("Einkaufszettel:", shopping_list)

loeschen = input("Möchtest du ein Produkt löschen? (ja/nein): ")
if loeschen.lower() == "ja":
    produkt_loeschen = input("Welches Produkt? ")
    if produkt_loeschen in shopping_list:
        del shopping_list[produkt_loeschen]
        print("Neuer Einkaufszettel:", shopping_list)
    else:
        print(produkt_loeschen, "nicht gefunden")