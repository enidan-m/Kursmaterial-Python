# AUFGABE: Erweitere das Login-System mit einem einfachen Taschenrechner-Menü
# 
# 1. Erstelle 3 feste Benutzerkonten mit einzelnen Variablen:
#    - user1_name = "admin", user1_pw = "1234", user1_role = "admin"
#    - user2_name = "worker", user2_pw = "5678", user2_role = "user"  
#    - user3_name = "reader", user3_pw = "9012", user3_role = "user"
#
# 2. Login-Abfrage mit folgenden Bedingungen:
#    - Prüfe nacheinander: Ist der Username user1, user2 oder user3?
#    - Wenn ja, prüfe das dazugehörige Passwort
#    - Bei falschem Passwort: "Falsches Passwort! Programm wird beendet"
#    - Wenn Username nicht gefunden: "Benutzer nicht gefunden! Programm wird beendet"
#
# 3. Nach erfolgreichem Login zeige ein Menü mit:
#    [1] Taschenrechner (Addition)
#    [2] Taschenrechner (Subtraktion)
#    [3] Taschenrechner (Multiplikation)
#    [4] Taschenrechner (Division)
#    [5] Uhrzeit anzeigen
#    [6] Zufallszahl generieren
#    [7] Programm beenden
#
# 4. Taschenrechner-Funktionen:
#    - Fordere den User auf, zwei Zahlen einzugeben
#    - Führe die entsprechende Rechenoperation aus
#    - Zeige das Ergebnis an
#    - Bei Division: Prüfe ob der Divisor 0 ist -> "Division durch 0 nicht erlaubt!"
#
# 5. Zusätzliche Bedingungen:
#    - Bei Admin (admin): Zeige "Willkommen Admin! Du hast alle Rechte"
#    - Bei User (worker und reader): Zeige "Willkommen User! Grundfunktionen verfügbar"
#    - Das Programm beendet sich erst bei Option [7]
#
# 6. Zufallszahl:
#    - Generiere eine Zahl zwischen 1 und 100
#    - Zeige: "Deine Zufallszahl ist: [zahl]"
#
# 7. Uhrzeit:
#    - Zeige die aktuelle Uhrzeit im Format: "Aktuelle Uhrzeit: 14:30:25"

#Zusatz:
# Überlege wie man nach jeder Option wieder das Hauptmenü angezeigt bekommt (auch while schleife)
#
# Tipp: Verwende while-Schleifen für das Menü und if-elif-else für die
# Benutzerprüfung und Menüauswahl.
#
# Beispiel für die Benutzerprüfung:
# if username == user1_name:
#     if password == user1_pw:
#         # Login erfolgreich
#     else:
#         # Passwort falsch
# elif username == user2_name:
#     # ...
#

###START
user_login_count = 0
while True:
    username = input("...")
    if user_login_count == 3:
        print("Programm beendet, zu viele Fehleingaben")
        break
    if username == "admin":
        print("Willkommen Admin")
        #hier geht es weiter mit den nächsten funktionen...
        break
    elif username == "worker" or username == "reader":
        print("Willkommen user")
        #hier geht es weiter mit den nächsten funktionen...
        break
    else:
        print("Falscher username")
        user_login_count +=1
    