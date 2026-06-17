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