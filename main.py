#Eine leere an usern. Ein User soll in der lange durch input der Liste neue User hinzuzufügen. Wenn der User "quit" eingibt soll keine weitere eingabe möglich sein und die die Liste mit allen hinzugefügten usern ausgegeben werden
 #0. Eine leere Liste 
 #1. Loop damit für die Eingabemöglichkeit 
 # 1.a Bei eingabe von "quit" oder "QUIT" oder "quIt" wird der loop unterbrochen und danach die bestehende Liste mit den Usern ausgegeben
 # TIP: user_entry = input("...").lower()
 #2. Nach dem Eingeben wird der Liste der eingegebene user hinzugefügt
 #Optional: Falls die Liste 10 Einträge groß ist (die Länge bekommt mit len()) wird das Programm beendet und die Liste mit den bestehenden usern ausgegeben
 
#HARD:

# AUFGABENSTELLUNG: MUSIKLISTE-VERWALTUNG

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






#Array, Schleifen, Eingaben & Ausgaben 
musik_list = []

    

while True :
    # text_option_1 = "#1. Füge einen Song hinzu."
    # text_option_2 = "#2. Gebe einen Song aus."
    # text_option_3 = "#3. Lösche einen Song."
    # print(f"""
    #      {text_option_1}
    #      {text_option_2}
    #      {text_option_3} 
    #       """)
    print("""
          #1. Füge einen Song hinzu.
          #2. Gebe einen Song aus.
          #3. Lösche einen Song.
          """)
    #eingabe für die optionsauswahl
    user_choice = input("Wähle die entsprechende Option aus [1|2|3]\n")
    if user_choice == "1":
        song = input("Gebe eine Song ein [Format: The Fray - How to save a life.mp3]\n")
        if  ".mp3" not in song:
            print("The song needs to contain the following [Artist - song.mp3]")
        
        ## Andere Lösungsmöglichkeit    
        # if song.find(".mp3") == -1:
        #      print("The song needs to contain the following [Artist - song.mp3]")
        
        #Lösung 3
        # song_string_splitted = song.split(".")
        
        # if song_string_splitted[1] != "mp3":
        #      print("The song needs to contain the following [Artist - song.mp3]")
        
        #Lösung 4
        
        ##Probiere aus
        # text = "test.mp3"
        # text_end = len(text) - 4 test.mp3 -> 8 - 3 = 4 
        #print(text[:text_end:-1])
        # print(text[:text_end:-1])   
        
        # text_end = len(song) - 4 # 
        # print(song[:text_end:-1])  #mp3 == 3pm   
        # if song[:text_end:-1] != "3pm":
        #     print("The song needs to contain the following [Artist - song.mp3]")
        #print(song_string_splitted)
        
        if song.lower() == "quit":
            print("Beende Programm")
            break
        
        musik_list.append(song)
        
        print("✅")
    elif user_choice.lower() == "quit":
            print("Beende Programm")
            break
    


