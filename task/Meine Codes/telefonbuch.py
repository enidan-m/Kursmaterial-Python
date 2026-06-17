#
# AUFGABE 1: TELEFONBUCH (SEHR EINFACH)
#
# Erstelle ein Wörterbuch, das Namen als Schlüssel und Telefonnummern als Wert speichert.
#
# 0. Leeres Wörterbuch anlegen: phonebook = {}
# 1. Der Benutzer gibt 3 Namen und Telefonnummern ein (OHNE Schleife)
# 2. Jeder Eintrag wird im Wörterbuch gespeichert
# 3. Gib das gesamte Telefonbuch aus
# 4. Frage den Benutzer nach einem Namen und gib die dazugehörige Nummer aus
#
# BEISPIEL:
# Eingabe: Name = "Anna", Nummer = "0123456789"
# Eingabe: Name = "Ben", Nummer = "9876543210"
# Eingabe: Name = "Clara", Nummer = "5551234567"
# Ausgabe: Telefonbuch: {'Anna': '0123456789', 'Ben': '9876543210', 'Clara': '5551234567'}
# Suche: "Anna" -> Anna hat die Nummer 0123456789
#
#

# phonebook = {
#    "Anna": "01759124912",
#    "Colgate": "0177907210",
#    "Dr Pepper": "017891928"
# }
# to_call = input("Wen willst du anrufen?\n>>>")
# print(phonebook[to_call])


 #AUFGABE 2: NOTENSPEICHER (SEHR EINFACH)
#
# Erstelle ein Wörterbuch, das Fächer als Schlüssel und Noten als Wert speichert.
#
# 0. Leeres Wörterbuch anlegen: grades = {}
# 1. Der Benutzer gibt 3 Fächer und Noten ein (OHNE Schleife)
# 2. Die Note wird als float gespeichert (TIPP: float() für Umwandlung)
# 3. Gib alle Fächer und Noten aus
# 4. Berechne den Notendurchschnitt (TIPP: sum() und len())
#
# BEISPIEL:
# Eingabe: Fach = "Mathe", Note = 2.0
# Eingabe: Fach = "Deutsch", Note = 1.5
# Eingabe: Fach = "Englisch", Note = 2.5
# Ausgabe: Mathe: 2.0, Deutsch: 1.5, Englisch: 2.5
# Durchschnitt: 2.0

#grades = {}
#grade_math = float(input("Mathenote\n"))
#grade_german = float(input("Deutschnote\n"))
#grade_english = float(input("Englischnote\n"))

#subjects = {
    # "Mathe": grade_math,
     #"Deutsch": grade_german, 
    # "Englisch": grade_english
# }
# #print(subjects)
# average = (subjects["Mathe"] + subjects["Deutsch"] + subjects["Englisch"])/len(subjects)
# print(f"Durchschnitt: {average}")



# AUFGABE 3: LÄNDER-HAUPTSTÄDTE (SEHR EINFACH)
#
# Erstelle ein Wörterbuch mit vordefinierten Ländern und Hauptstädten.
# Der Benutzer soll nach einem Land fragen und die Hauptstadt angezeigt bekommen.
#
# 0. Wörterbuch mit 3 Ländern erstellen: countries = {"Deutschland": "Berlin", "Frankreich": "Paris", "Italien": "Rom"}
# 1. Gib dem Benutzer die Auswahl: Zeige alle Länder an
# 2. Der Benutzer gibt ein Land ein
# 3. Wenn das Land existiert, gib die Hauptstadt aus
# 4. Wenn das Land nicht existiert, gib "Land nicht gefunden" aus
#
# BEISPIEL:
# Länder: Deutschland, Frankreich, Italien
# Eingabe: "Deutschland" -> Die Hauptstadt von Deutschland ist Berlin
# Eingabe: "Spanien" -> Spanien nicht gefunden

map = {}

countries = {
    "Deutschland": "Berlin",
    "Frankreich": "Paris",
    "Italien": "Rom"
}
print(countries.keys())
select_country = input("Wähle ein Land aus\n").capitalize()
if select_country in countries: 
    print(countries[select_country])
else:
    print("Land nicht gefunden")