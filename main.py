#==================================THEMA: DICTIONARIES==================================
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
# AUFGABE 2: NOTENSPEICHER (SEHR EINFACH)
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
#

#
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
#

#
# AUFGABE 4: WÖRTERBUCH ERWEITERN (SEHR EINFACH)
#
# Starte mit einem leeren Wörterbuch und füge nach und nach Einträge hinzu.
#
# 0. Leeres Wörterbuch anlegen: my_dict = {}
# 1. Füge 3 Schlüssel-Wert-Paare hinzu (ohne Benutzereingabe, direkt im Code)
#    TIPP: my_dict["key1"] = "value1"
# 2. Ändere den Wert von einem Schlüssel
#    TIPP: my_dict["key1"] = "neuer_wert"
# 3. Lösche einen Schlüssel mit del
#    TIPP: del my_dict["key2"]
# 4. Gib das fertige Wörterbuch aus
#
# BEISPIEL:
# Start: {}
# Nach Hinzufügen: {"name": "Anna", "alter": 25, "stadt": "Berlin"}
# Nach Ändern: {"name": "Anna", "alter": 26, "stadt": "Berlin"}
# Nach Löschen: {"name": "Anna", "stadt": "Berlin"}
#

#
# AUFGABE 5: EINKAUFSZETTEL (EINFACH MIT SCHLEIFE)
#
# Erstelle ein Wörterbuch für einen Einkaufszettel. Der Benutzer kann Produkte und Mengen eingeben.
#
# 0. Leeres Wörterbuch: shopping_list = {}
# 1. Schleife für die Eingabe (3 Durchgänge)
# 2. Pro Durchgang: Produktname und Menge eingeben
# 3. Speichere im Wörterbuch: shopping_list[produkt] = menge
# 4. Nach der Schleife: Gib den gesamten Einkaufszettel aus
# 5. Frage den Benutzer, ob er ein Produkt löschen möchte (ja/nein)
# 6. Wenn ja: Produktname eingeben und aus Wörterbuch löschen
#
# BEISPIEL:
# 1. Produkt: "Äpfel", Menge: 3
# 2. Produkt: "Milch", Menge: 1
# 3. Produkt: "Brot", Menge: 2
# Einkaufszettel: Äpfel: 3, Milch: 1, Brot: 2
# Löschen? ja
# Welches Produkt? "Milch"
# Neuer Einkaufszettel: Äpfel: 3, Brot: 2
#

#
# ALLGEMEINE TIPS FÜR ALLE AUFGABEN:
#
# - Wörterbücher werden mit {} erstellt
# - Auf Werte zugreifen: dictionary[key]
# - Werte setzen: dictionary[key] = value
# - Auf Existenz prüfen: if key in dictionary:
# - Löschen: del dictionary[key] oder dictionary.pop(key)
# - Alle Schlüssel: dictionary.keys()
# - Alle Werte: dictionary.values()
# - Alle Paare: dictionary.items()
# - Bei Eingaben mit input() immer den richtigen Datentyp verwenden (int, float, str)



#==================================THEMA: FUNKTIONEN==================================
#
# AUFGABE 1: BEGRÜSSUNGS-FUNKTION (SEHR EINFACH)
#
# Schreibe eine Funktion, die einen Namen als Parameter nimmt und eine Begrüßung ausgibt.
#
# 0. Definiere die Funktion: def gruesse(name):
# 1. Die Funktion gibt "Hallo [name]!" aus
# 2. Rufe die Funktion mit 3 verschiedenen Namen auf (OHNE Schleife)
#
# BEISPIEL:
# gruesse("Anna") -> Hallo Anna!
# gruesse("Ben") -> Hallo Ben!
# gruesse("Clara") -> Hallo Clara!
#

#
# AUFGABE 2: SUMME BEREICHNEN (SEHR EINFACH)
#
# Schreibe eine Funktion, die zwei Zahlen als Parameter nimmt und deren Summe zurückgibt.
#
# 0. Definiere die Funktion: def summe(zahl1, zahl2):
# 1. Die Funktion berechnet die Summe und gibt sie mit return zurück
# 2. Rufe die Funktion mit 3 verschiedenen Zahlenpaaren auf
# 3. Gib die Ergebnisse aus
#
# BEISPIEL:
# summe(5, 3) -> 8
# summe(10, 7) -> 17
# summe(2.5, 4.5) -> 7.0
#

#
# AUFGABE 3: QUADRAT-FUNKTION (SEHR EINFACH)
#
# Schreibe eine Funktion, die eine Zahl als Parameter nimmt und das Quadrat zurückgibt.
#
# 0. Definiere die Funktion: def quadrat(zahl):
# 1. Die Funktion berechnet zahl * zahl und gibt es mit return zurück
# 2. Der Benutzer gibt eine Zahl ein (input)
# 3. Rufe die Funktion mit der eingegebenen Zahl auf
# 4. Gib das Ergebnis aus
#
# BEISPIEL:
# Eingabe: 5 -> Das Quadrat von 5 ist 25
# Eingabe: 3 -> Das Quadrat von 3 ist 9
#

#
# AUFGABE 4: GERADE ODER UNGERADE (EINFACH)
#
# Schreibe eine Funktion, die prüft, ob eine Zahl gerade oder ungerade ist.
#
# 0. Definiere die Funktion: def ist_gerade(zahl):
# 1. Die Funktion gibt True zurück, wenn die Zahl gerade ist, sonst False
#    TIPP: Verwende den Modulo-Operator % (zahl % 2 == 0)
# 2. Der Benutzer gibt eine Zahl ein (input)
# 3. Rufe die Funktion mit der eingegebenen Zahl auf
# 4. Gib aus: "Die Zahl ist gerade" oder "Die Zahl ist ungerade"
#
# BEISPIEL:
# Eingabe: 4 -> Die Zahl 4 ist gerade
# Eingabe: 7 -> Die Zahl 7 ist ungerade
#

#
# AUFGABE 5: MEHRERE FUNKTIONEN (EINFACH)
#
# Schreibe 3 Funktionen für einen einfachen Taschenrechner.
#
# 0. Definiere die Funktionen:
#    0.a def addieren(a, b): gibt a + b zurück
#    0.b def subtrahieren(a, b): gibt a - b zurück
#    0.c def multiplizieren(a, b): gibt a * b zurück
# 1. Der Benutzer gibt 2 Zahlen und eine Operation ein (+, -, *)
# 2. Rufe die passende Funktion auf
# 3. Gib das Ergebnis aus
#
# BEISPIEL:
# Erste Zahl: 10
# Zweite Zahl: 5
# Operation: + -> 10 + 5 = 15
# Operation: - -> 10 - 5 = 5
# Operation: * -> 10 * 5 = 50
#

#
# AUFGABE 6: STANDARDWERTE (EINFACH)
#
# Schreibe eine Funktion mit Standardwerten für Parameter.
#
# 0. Definiere die Funktion: def begruessung(name, anrede="Hallo"):
# 1. Die Funktion gibt "[anrede] [name]!" aus
# 2. Rufe die Funktion auf:
#    2.a Mit nur einem Parameter (name) -> Standardwert "Hallo" wird verwendet
#    2.b Mit zwei Parametern (name, anrede) -> Eigener Wert wird verwendet
#
# BEISPIEL:
# begruessung("Anna") -> Hallo Anna!
# begruessung("Ben", "Guten Morgen") -> Guten Morgen Ben!
#

#
# AUFGABE 7: LISTE DURCHGEHEN (MITTEL)
#
# Schreibe eine Funktion, die eine Liste von Zahlen als Parameter nimmt
# und den Durchschnitt berechnet.
#
# 0. Definiere die Funktion: def durchschnitt(zahlen_liste):
# 1. Die Funktion berechnet den Durchschnitt mit sum() und len()
# 2. Die Funktion gibt den Durchschnitt zurück
# 3. Erstelle eine Liste mit 5 Zahlen (OHNE Benutzereingabe)
# 4. Rufe die Funktion mit der Liste auf
# 5. Gib den Durchschnitt aus
#
# BEISPIEL:
# Liste: [4, 5, 6, 7, 8] -> Durchschnitt: 6.0
# Liste: [10, 20, 30, 40, 50] -> Durchschnitt: 30.0
#

#
# AUFGABE 8: MEHRERE RÜCKGABEWERTE (MITTEL)
#
# Schreibe eine Funktion, die mehrere Werte zurückgibt.
#
# 0. Definiere die Funktion: def min_max(zahlen_liste):
# 1. Die Funktion berechnet das Minimum und Maximum der Liste
#    TIPP: min() und max() Funktionen verwenden
# 2. Die Funktion gibt beide Werte zurück (TIPP: return min_wert, max_wert)
# 3. Erstelle eine Liste mit beliebigen Zahlen
# 4. Rufe die Funktion auf und speichere beide Rückgabewerte
# 5. Gib Minimum und Maximum aus
#
# BEISPIEL:
# Liste: [5, 2, 8, 1, 9] -> Minimum: 1, Maximum: 9
# Liste: [3.5, 2.1, 7.8, 4.2] -> Minimum: 2.1, Maximum: 7.8
#

#
# AUFGABE 9: FUNKTION MIT SCHLEIFE (MITTEL)
#
# Schreibe eine Funktion, die eine Liste von Namen bekommt
# und jeden Namen mit einer Begrüßung ausgibt.
#
# 0. Definiere die Funktion: def begruesse_alle(namen_liste):
# 1. Die Funktion geht mit einer for-Schleife durch die Liste
# 2. Für jeden Namen wird "Hallo [name]!" ausgegeben
# 3. Erstelle eine Liste mit 5 Namen (OHNE Benutzereingabe)
# 4. Rufe die Funktion mit der Liste auf
#
# BEISPIEL:
# Liste: ["Anna", "Ben", "Clara", "David", "Emma"]
# Ausgabe:
# Hallo Anna!
# Hallo Ben!
# Hallo Clara!
# Hallo David!
# Hallo Emma!
#

#
# AUFGABE 10: FUNKTIONEN ZUSAMMENSETZEN (SCHWER)
#
# Schreibe mehrere kleine Funktionen, die zusammen ein Programm ergeben.
#
# 0. Definiere die Funktionen:
#    0.a def eingabe_zahl(prompt): gibt input als float zurück
#    0.b def berechne_flaeche(breite, hoehe): gibt breite * hoehe zurück
#    0.c def ausgabe(flaeche): gibt "Die Fläche ist: [flaeche]" aus
# 1. Rufe die Funktionen in der richtigen Reihenfolge auf:
#    1.a Breite mit eingabe_zahl() einlesen
#    1.b Höhe mit eingabe_zahl() einlesen
#    1.c Fläche mit berechne_flaeche() berechnen
#    1.d Ergebnis mit ausgabe() anzeigen
#
# BEISPIEL:
# Breite: 5
# Höhe: 3
# Die Fläche ist: 15.0
#

#
# ALLGEMEINE TIPS FÜR ALLE AUFGABEN:
#
# - Funktionen werden mit def definiert: def funktionsname(parameter):
# - Der Code einer Funktion wird eingerückt
# - Mit return gibt eine Funktion einen Wert zurück
# - Ohne return gibt die Funktion None zurück
# - Funktionen werden mit funktionsname(argument) aufgerufen
# - Parameter können Standardwerte haben: def name(parameter="wert"):
# - Mehrere Rückgabewerte: return wert1, wert2
# - Die Dokumentation findest du unter:
#   https://www.w3schools.com/python/python_functions.asp