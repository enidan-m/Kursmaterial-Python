import datetime
import random
#login 


#1. Usereingaben in variablen speichern (username,password)
username = input("Gebe den Usernamen ein\n").lower()
password = input("Gebe das Passwort ein\n").lower()

#2. Abfrage: ist der User root und das passwort admin wird das system angezeigt ansonsten abgebrochen. 
if username == "root" and password == "admin":
    #3. Eine Art Überschrift z.B Willkommen <User> ... Eine Optionsauswahl
    #1. Zeige Systemwerte 
    #2. Zeige Uhrzeit an
    #3. Lasse eine random Zahl generieren
    #4. Exit
    #Tip:
    #print("1. Zeige Systemwert\n...")
    print(f"""
          ********Willkommen {username}********
          #1. Zeige Systemwerte
          #2. Zeige Uhrzeit an t
          #3. Lasse eine Zufallszahl generieren
          #4. Exit
          """)
    user_option = input("Wähle eine entsprechende Option aus! [1|2|3|4]")
    if user_option == "1":
        print("""
              ABC: ...
              ABC:...
              
              """)
    elif user_option == "2":
        now = datetime.datetime.now()
        print(str(now.time()))
    elif user_option == "3":
        pseudo_random_number = random.randrange(1,10)
        print(pseudo_random_number)
    else:
        print("CYA!")
else:
    print("Beende Programm")

#4. User soll durch Eingabe in den entsprechenden Menü gelangen
    #4.1 ....
    #4.2 ....
    #4.3
    #Tip:
    # https://www.w3schools.com/python/gloss_python_random_number.asp - Random number
    # https://www.w3schools.com/python/ref_module_time.asp  - Zeit
    
#5. Das programm endet wenn der user einen Menüpunkt ausgeführt hat
    