# AUFGABE: PASSWORTGENERATOR MIT BENUTZERVERWALTUNG (OHNE FUNKTIONEN)
#
# Eine umfassende Aufgabe, die alle bisherigen Konzepte vereint:
# - Variablen und Datentypen
# - Eingaben und Ausgaben
# - Listen und Wörterbücher
# - Bedingungen (if/elif/else)
# - Schleifen (for/while)
#
# ZIEL: Ein Programm zur Benutzerverwaltung mit automatischem Passwortgenerator
#       OHNE eigene Funktionen zu definieren! Verwende nur die Hauptschleife.
#

# ==================================================================================
# IMPORTE
# ==================================================================================

import random
import string
from datetime import datetime

# ==================================================================================
# PROGRAMMSTART
# ==================================================================================

#
# 1. DATENBANK INITIALISIEREN
#
# Erstelle eine leere Liste namens 'datenbank', die später alle Benutzer speichert.
# Jeder Benutzer wird als Dictionary gespeichert.
#
# TIPP: datenbank = []

datenbank = []

while True:
    print("""
          1. Neuen Benutzer erstellen
          2. Alle Benutzer anzeigen
          3. Benutzer suchen
          4. Benutzer löschen
          5. Passwort ändern
          6. Programm beenden
          """)
    user_choice = input("Wähle die entsprechende Option aus [1|2|3|4|5|6]\n")

    if user_choice == "1":
        new_user = input("Geben einen Benutzernamen ein\n")
        break

    elif user_choice == "2":
        print("Hier sind alle Benutzer")
        break

    elif user_choice == "3":
        search_user = input("Gib einen Benutzernamen ein, nachdem gesucht werden soll\n")
        break

    elif user_choice == "4":
        delete_user = input("Welcher Benutzer soll gelöscht werden?\n")
        break

    elif user_choice == "5":
        change_password = input("Passwort ändern\n")
        break

    elif user_choice == "6":
        print("Das Programm wird beendet\n")
        break


        
        
        
        # if  ".mp3" not in song:
        #     print("The song needs to contain the following [Artist - song.mp3]")
#

#
# 2. HAUPTSCHEIFE STARTEN
#
# Starte eine while-Schleife, die solange läuft, bis der Benutzer "6" eingibt.
#
# TIPP: while True:
#

#
# 3. MENÜ ANZEIGEN
#
# Zeige dem Benutzer das Hauptmenü an:
#
# ==================================
#    PASSWORTGENERATOR & USERVERWALTUNG
# ==================================
# [1] Neuen Benutzer erstellen
# [2] Alle Benutzer anzeigen
# [3] Benutzer suchen
# [4] Benutzer löschen
# [5] Passwort ändern
# [6] Programm beenden
# ==================================
#
# TIPP: Verwende print() für die Ausgabe
#

#
# 4. BENUTZEREINGABE FÜR MENÜAUSWAHL
#
# Frage den Benutzer mit input("Ihre Wahl: ") nach seiner Auswahl.
# Speichere die Eingabe in einer Variable (z.B. 'wahl').
#

#
# 5. FALLUNTERSCHEIDUNGEN FÜR DIE MENÜAUSWAHL
#
# Verwende if/elif/else, um die verschiedenen Optionen zu behandeln.
#
# TIPP: if wahl == "1": ... elif wahl == "2": ... elif wahl == "6": break
#

#
# ==================================================================================
# OPTION 1: NEUEN BENUTZER ERSTELLEN
# ==================================================================================

#
# 1.1 BENUTZERNAMEN EINGEBEN
#
# Frage den Benutzer mit input("Benutzername: ") nach dem Namen.
# Speichere den Namen in einer Variable (z.B. 'name').
#

#
# 1.2 PASSWORTLÄNGE EINGEBEN
#
# Frage den Benutzer mit input("Passwortlänge (min. 4): ") nach der Länge.
# Wandle die Eingabe in einen Integer um.
# TIPP: laenge = int(input("Passwortlänge: "))
#

#
# 1.3 PASSWORT GENERIEREN
#
# Erstelle einen String mit allen möglichen Zeichen für das Passwort:
# zeichen = string.ascii_lowercase + string.digits
#
# Generiere das Passwort mit random.choice() in einer Schleife.
# TIPP: Verwende eine for-Schleife mit range(laenge) und baue das Passwort auf.
#
# Beispiel für die Schleife:
# passwort = ""
# for i in range(laenge):
#     passwort = passwort + random.choice(zeichen)
#

#
# 1.4 PASSWORT-STÄRKE BEWERTEN
#
# Bewerte das generierte Passwort:
# - Punkte sammeln für:
#   * Länge >= 8: 1 Punkt, >= 12: 2 Punkte
#   * Enthält Großbuchstaben: 1 Punkt (TIPP: any(c.isupper() for c in passwort))
#   * Enthält Zahlen: 1 Punkt (TIPP: any(c.isdigit() for c in passwort))
#   * Enthält Sonderzeichen: 1 Punkt (TIPP: any(c in string.punctuation for c in passwort))
#
# - Gesamtbewertung:
#   * 0-2 Punkte: "Schwach"
#   * 3-4 Punkte: "Mittel"
#   * 5+ Punkte: "Stark"
#

#
# 1.5 BENUTZER OBJEKT ERSTELLEN
#
# Erstelle ein Dictionary für den neuen Benutzer mit folgenden Schlüsseln:
# - "name": der eingegebene Name
# - "passwort": das generierte Passwort
# - "erstellt_am": aktuelles Datum und Uhrzeit (TIPP: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# - "passwort_staerke": die berechnete Stärke
#

#
# 1.6 BENUTZER ZUR DATENBANK HINZUFÜGEN
#
# Überprüfe zuerst, ob der Benutzername bereits existiert.
# Durchsuche die datenbank mit einer for-Schleife:
# for benutzer in datenbank:
#     if benutzer["name"] == name:
#         print("Benutzername existiert bereits!")
#         break
# else:
#     datenbank.append(neuer_benutzer)
#     print("Benutzer wurde erfolgreich erstellt!")
#

#
# ==================================================================================
# OPTION 2: ALLE BENUTZER ANZEIGEN
# ==================================================================================

#
# 2.1 PRÜFEN, OB DATENBANK LEER IST
#
# Wenn die datenbank leer ist (len(datenbank) == 0), gib "Keine Benutzer gefunden" aus.
#

#
# 2.2 ALLE BENUTZER AUSGEBEN
#
# Durchlaufe die datenbank mit einer for-Schleife und gib jeden Benutzer aus.
# Verwende dafür eine Trennlinie zwischen den Benutzern.
#
# Ausgabeformat:
# Name: Anna | Passwort: abc123 | Erstellt: 2024-01-15 | Stärke: Mittel
# --------------------------------------------------
#

#
# ==================================================================================
# OPTION 3: BENUTZER SUCHEN
# ==================================================================================

#
# 3.1 BENUTZERNAMEN EINGEBEN
#
# Frage den Benutzer mit input("Benutzername: ") nach dem Namen.
#

#
# 3.2 BENUTZER IN DATENBANK SUCHEN
#
# Durchsuche die datenbank mit einer for-Schleife:
# for benutzer in datenbank:
#     if benutzer["name"] == name:
#         print(benutzer)  # Oder besser formatiert
#         break
# else:
#     print("Benutzer nicht gefunden")
#

#
# ==================================================================================
# OPTION 4: BENUTZER LÖSCHEN
# ==================================================================================

#
# 4.1 BENUTZERNAMEN EINGEBEN
#
# Frage den Benutzer mit input("Benutzername: ") nach dem Namen.
#

#
# 4.2 BESTÄTIGUNG ABFRAGEN
#
# Frage den Benutzer: "Möchten Sie diesen Benutzer wirklich löschen? (j/n): "
# Verwende .lower() für die Eingabe.
#

#
# 4.3 BENUTZER LÖSCHEN (WENN BESTÄTIGT)
#
# Durchsuche die datenbank mit einer for-Schleife:
# for benutzer in datenbank:
#     if benutzer["name"] == name:
#         datenbank.remove(benutzer)
#         print("Benutzer wurde gelöscht")
#         break
# else:
#     print("Benutzer nicht gefunden")
#

#
# ==================================================================================
# OPTION 5: PASSWORT ÄNDERN
# ==================================================================================

#
# 5.1 BENUTZERNAMEN EINGEBEN
#
# Frage den Benutzer mit input("Benutzername: ") nach dem Namen.
#

#
# 5.2 BENUTZER IN DATENBANK SUCHEN
#
# Durchsuche die datenbank mit einer for-Schleife, um den Benutzer zu finden.
# Wenn nicht gefunden: Gib eine Fehlermeldung aus.
#

#
# 5.3 NEUE PASSWORTLÄNGE EINGEBEN
#
# Frage den Benutzer mit input("Neue Passwortlänge: ") nach der Länge.
#

#
# 5.4 NEUES PASSWORT GENERIEREN
#
# Verwende den gleichen Code wie bei Option 1, um ein neues Passwort zu generieren.
#

#
# 5.5 PASSWORT-STÄRKE BEWERTEN
#
# Bewerte das neue Passwort mit dem gleichen Code wie bei Option 1.
#

#
# 5.6 PASSWORT AKTUALISIEREN
#
# Aktualisiere das Passwort und die Passwort-Stärke des gefundenen Benutzers.
# TIPP: benutzer["passwort"] = neues_passwort
#       benutzer["passwort_staerke"] = neue_staerke
#

#
# ==================================================================================
# OPTION 6: PROGRAMM BEENDEN
# ==================================================================================

#
# 6.1 ABSCHIEDSNACHRICHT
#
# Gib "Programm beendet. Auf Wiedersehen!" aus.
#

#
# 6.2 SCHLEIFE BEENDEN
#
# Verwende break, um die while-Schleife zu beenden.
#

#
# ==================================================================================
# UNGÜLTIGE EINGABE BEHANDELN
# ==================================================================================

#
# 7.1 ELSE-ZWEIG FÜR UNGÜLTIGE EINGABE
#
# Wenn die Wahl nicht 1-6 ist, gib "Ungültige Auswahl! Bitte wählen Sie 1-6." aus.
#
# TIPP: else: (nach allen elifs)
#

#
# ==================================================================================
# PAUSE AM ENDE JEDER AKTION
# ==================================================================================

#
# 8.1 PAUSE EINFÜGEN
#
# Nach jeder Aktion soll der Benutzer die Möglichkeit haben, die Ausgabe zu lesen.
# Füge am Ende jedes if-Zweigs ein input("Drücken Sie Enter, um fortzufahren...") ein.
#
# TIPP: input("Drücken Sie Enter, um fortzufahren...")
#

#
# ==================================================================================
# BEISPIELE FÜR DIE AUSGABE
# ==================================================================================

#
# BEISPIEL 1: Neuen Benutzer erstellen
#
# ==================================
#    PASSWORTGENERATOR & USERVERWALTUNG
# ==================================
# [1] Neuen Benutzer erstellen
# [2] Alle Benutzer anzeigen
# [3] Benutzer suchen
# [4] Benutzer löschen
# [5] Passwort ändern
# [6] Programm beenden
# ==================================
# Ihre Wahl: 1
# 
# Benutzername: Anna
# Passwortlänge (min. 4): 10
# Generiertes Passwort: a7k3m9x2b4
# Passwort-Stärke: Mittel
# Benutzer 'Anna' wurde erfolgreich erstellt!
# Drücken Sie Enter, um fortzufahren...
#

#
# BEISPIEL 2: Alle Benutzer anzeigen
#
# Ihre Wahl: 2
# 
# Alle Benutzer:
# Name: Anna | Passwort: a7k3m9x2b4 | Erstellt: 2024-01-15 10:30:00 | Stärke: Mittel
# --------------------------------------------------
# Name: Ben | Passwort: c5n8q2w5e1 | Erstellt: 2024-01-15 10:35:00 | Stärke: Stark
# --------------------------------------------------
# Drücken Sie Enter, um fortzufahren...
#

#
# BEISPIEL 3: Benutzer suchen
#
# Ihre Wahl: 3
# 
# Benutzername: Anna
# Name: Anna | Passwort: a7k3m9x2b4 | Erstellt: 2024-01-15 10:30:00 | Stärke: Mittel
# Drücken Sie Enter, um fortzufahren...
#

#
# BEISPIEL 4: Benutzer löschen
#
# Ihre Wahl: 4
# 
# Benutzername: Anna
# Möchten Sie Anna wirklich löschen? (j/n): j
# Benutzer 'Anna' wurde gelöscht.
# Drücken Sie Enter, um fortzufahren...
#

#
# BEISPIEL 5: Passwort ändern
#
# Ihre Wahl: 5
# 
# Benutzername: Ben
# Neue Passwortlänge: 12
# Neues Passwort: x7p3m9q2w5e1
# Passwort-Stärke: Stark
# Passwort für 'Ben' wurde aktualisiert.
# Drücken Sie Enter, um fortzufahren...
#

#
# BEISPIEL 6: Programm beenden
#
# Ihre Wahl: 6
# Programm beendet. Auf Wiedersehen!
#

# ==================================================================================
# TIPS FÜR DIE UMSETZUNG
# ==================================================================================

#
# 1. STRING-METHODEN:
#    - .lower() für Kleinschreibung bei Bestätigungen
#    - any() für die Überprüfung von Zeichen im Passwort
#
# 2. LISTEN-METHODEN:
#    - .append() zum Hinzufügen von Benutzern
#    - .remove() zum Löschen von Benutzern
#
# 3. WÖRTERBUCH-METHODEN:
#    - dict["key"] = wert zum Setzen von Werten
#    - for benutzer in datenbank: zum Durchlaufen der Liste
#
# 4. IMPORTE:
#    - import random (für random.choice)
#    - import string (für string.ascii_lowercase, string.digits, string.punctuation)
#    - from datetime import datetime (für datetime.now())
#
# 5. DOKUMENTATION (nützliche Links):
#    - W3Schools Python: https://www.w3schools.com/python/
#    - Python Docs: https://docs.python.org/3/
#    - Random: https://docs.python.org/3/library/random.html
#    - String: https://docs.python.org/3/library/string.html
#    - Datetime: https://docs.python.org/3/library/datetime.html
#
# VIEL ERFOLG BEI DER UMSETZUNG!
#  