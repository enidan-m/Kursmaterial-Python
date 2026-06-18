#Eine leere an usern. Ein User soll in der lange durch input der Liste neue User hinzuzufügen. Wenn der User "quit" eingibt soll keine weitere eingabe möglich sein und die die Liste mit allen hinzugefügten usern ausgegeben werden
 #0. Eine leere Liste 
 #1. Loop damit für die Eingabemöglichkeit 
 # 1.a Bei eingabe von "quit" oder "QUIT" oder "quIt" wird der loop unterbrochen und danach die bestehende Liste mit den Usern ausgegeben
 # TIP: user_entry = input("...").lower()
 #2. Nach dem Eingeben wird der Liste der eingegebene user hinzugefügt
 #Optional: Falls die Liste 10 Einträge groß ist (die Länge bekommt mit len()) wird das Programm beendet und die Liste mit den bestehenden usern ausgegeben
 
#HARD:

# A
#TE-VERWALTUNG

# Erweitere das vorhandene Login- und Hauptmenü-Programm um zwei neue Funktionen:

# 1. Musikliste anlegen (Option 8): Der Benutzer kann Songs zur Liste hinzufügen.
# 2. Songs aus der Musikliste löschen (Option 9): Der Benutzer kann einen Song 
#    anhand des Namens suchen und löschen.

# -------------------------------------------------------------------------------
# ANFORDERUNGEN FÜR DIE MUSIKLISTE
# -------------------------------------------------------------------------------
# - Erstelle eine LEERE LISTE namens 'music_list' zu Beginn des Programms 
#   (z.B. nach dem Login).
# - Die Liste soll die hinzugefügten Songs speichern.

# -------------------------------------------------------------------------------
# ANFORDERUNGEN FÜR OPTION 8: MUSIKLISTE ANLEGEN (SONGS HINZUFÜGEN)
# -------------------------------------------------------------------------------
# - Implementiere eine SCHLEIFE, die es erlaubt, mehrere Songs hintereinander 
#   einzugeben.
# - Der Benutzer soll zur Eingabe eines Songtitels aufgefordert werden.
# - Wenn der Benutzer "quit" (Groß-/Kleinschreibung egal) eingibt, wird die 
#   Schleife beendet.
#   TIPP: Verwende .lower() für die Eingabe.
# - Nach der Beendigung der Schleife wird die gesamte Musikliste mit allen Songs 
#   ausgegeben.
# - OPTIONAL: Falls die Liste bereits 10 Einträge enthält, wird die Schleife 
#   automatisch beendet und die Liste ausgegeben.
# - Füge den eingegebenen Song (außer "quit") zur Liste hinzu.
#   TIPP: Verwende die append()-Methode.

# -------------------------------------------------------------------------------
# ANFORDERUNGEN FÜR OPTION 9: SONGS AUS DER MUSIKLISTE LÖSCHEN
# -------------------------------------------------------------------------------
# - Der Benutzer wird aufgefordert, den NAMEN EINES SONGS einzugeben, den er 
#   löschen möchte.
# - Das Programm sucht nach diesem Song in der 'music_list'.
#   TIPP: Verwende eine Schleife (for oder while), um die Liste zu durchsuchen.
#   TIPP: Verwende die in- oder remove()-Methode aus den Python Listen-Methoden
#   (z.B. list.remove() oder list.pop()).
# - Wenn der Song gefunden wird, wird er aus der Liste gelöscht und eine 
#   Bestätigung ausgegeben.
# - Wenn der Song NICHT gefunden wird, erscheint eine entsprechende Meldung.

# -------------------------------------------------------------------------------
# HINWEISE ZUR EINBINDUNG

# - Füge die neuen Optionen [8] Musikliste anlegen und [9] Songs aus Musikliste 
#   löschen in das Hauptmenü ein.
# - Passe die Bereichsüberprüfung (if choice == "1" bis elif choice == "9") und 
#   die else-Meldung entsprechend an.
# - Die music_list muss AUSSERHALB der Hauptschleife definiert werden, damit sie 
#   beim Hinzufügen und Löschen erhalten bleibt.

# TIPS FÜR DIE UMSETZUNG
# -------------------------------------------------------------------------------
# - Nutze die Dokumentation zu Python Listen und insbesondere die Methoden unter 
#   "List Methods" auf W3Schools.
# - Verwende für die Song-Eingabe input() und für die Ausgabe print().
# - Denk daran, die neuen Menüpunkte im Hauptmenü-Text zu ergänzen.

usernames = []

while True:
    entry_user = input("Gebe einen Namen ein\n")
    if entry_user.lower() == "quit":
        break
    if len(usernames) > 10: 
        break
    usernames.append(entry_user)
for username in usernames:
    print(f"User: {username}")

while True:
    delete_entry = input("Welcher user soll gelöscht werden?\n")
    found = 0
    username_found = ""
    for username in usernames:
        if delete_entry == username: 
            #print(username)
            username_found = username
            found +=1
^^
    if found == 0:
        print("Nicht gefunden")
    else: 
        print(f"""
        username: {username_found}
        counts: {found}
        """)    