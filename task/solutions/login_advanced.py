import datetime
import random

user1_name = "admin"
user1_pw = "1234"
user1_role = "admin"

user2_name = "worker"
user2_pw = "5678"
user2_role = "user"

user3_name = "reader"
user3_pw = "9012"
user3_role = "user"

max_login_attempts = 3
login_attempts = 0
logged_in = False

while login_attempts < max_login_attempts and not logged_in:
    print("\n")
    print("       WILLKOMMEN ZUM LOGIN-SYSTEM")
    print("")
    
    username = input("Benutzername: ")
    password = input("Passwort: ")
    
    user_found = False
    user_role = None
    
    users = [
        (user1_name, user1_pw, user1_role),
        (user2_name, user2_pw, user2_role),
        (user3_name, user3_pw, user3_role)
    ]
    
    for user_name, user_pw, user_role_temp in users:
        if username == user_name:
            user_found = True
            if password == user_pw:
                user_role = user_role_temp
                print("")
                print("Login erfolgreich!")
                if user_role == "admin":
                    print("Willkommen Admin! Du hast alle Rechte")
                else:
                    print("Willkommen User! Grundfunktionen verfuegbar")
                logged_in = True
                break
            else:
                print("")
                print("Falsches Passwort! Programm wird beendet")
                login_attempts = max_login_attempts
                break
            break
    
    if not user_found and not logged_in:
        login_attempts += 1
        remaining = max_login_attempts - login_attempts
        print("")
        print("Benutzer nicht gefunden! Noch " + str(remaining) + " Versuch(e)")
        if login_attempts == max_login_attempts:
            print("")
            print("Zu viele Fehleingaben! Programm wird beendet")

if not logged_in:
    print("")
    print("Programm beendet")
else:
    while True:
        print("""
        HAUPTMENÜ

        [1] Taschenrechner (Addition)
        [2] Taschenrechner (Subtraktion)
        [3] Taschenrechner (Multiplikation)
        [4] Taschenrechner (Division)
        [5] Uhrzeit anzeigen
        [6] Zufallszahl generieren
        [7] Programm beenden
        """)
        
        choice = input("Ihre Auswahl: ")
        
        if choice == "1":
            num1 = input("Erste Zahl: ")
            num2 = input("Zweite Zahl: ")
            if num1.isdigit() and num2.isdigit():
                num1 = float(num1)
                num2 = float(num2)
                result = num1 + num2
                print("")
                print(str(num1) + " + " + str(num2) + " = " + str(result))
            else:
                print("")
                print("Bitte geben Sie gueltige Zahlen ein!")
        
        elif choice == "2":
            num1 = input("Erste Zahl: ")
            num2 = input("Zweite Zahl: ")
            if num1.isdigit() and num2.isdigit():
                num1 = float(num1)
                num2 = float(num2)
                result = num1 - num2
                print("")
                print(str(num1) + " - " + str(num2) + " = " + str(result))
            else:
                print("")
                print("Bitte geben Sie gueltige Zahlen ein!")
        
        elif choice == "3":
            num1 = input("Erste Zahl: ")
            num2 = input("Zweite Zahl: ")
            if num1.isdigit() and num2.isdigit():
                num1 = float(num1)
                num2 = float(num2)
                result = num1 * num2
                print("")
                print(str(num1) + " * " + str(num2) + " = " + str(result))
            else:
                print("")
                print("Bitte geben Sie gueltige Zahlen ein!")
        
        elif choice == "4":
            num1 = input("Erste Zahl (Dividend): ")
            num2 = input("Zweite Zahl (Divisor): ")
            if num1.isdigit() and num2.isdigit():
                num1 = float(num1)
                num2 = float(num2)
                if num2 == 0:
                    print("")
                    print("Division durch 0 nicht erlaubt!")
                else:
                    result = num1 / num2
                    print("")
                    print(str(num1) + " / " + str(num2) + " = " + str(result))
            else:
                print("")
                print("Bitte geben Sie gueltige Zahlen ein!")
        
        elif choice == "5":
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%H:%M:%S")
            print("")
            print("Aktuelle Uhrzeit: " + formatted_time)
        
        elif choice == "6":
            random_number = random.randint(1, 100)
            print("")
            print("Deine Zufallszahl ist: " + str(random_number))
        
        elif choice == "7":
            print("")
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        
        else:
            print("")
            print("Ungueltige Auswahl! Bitte waehlen Sie 1-7")
        
        input("")
        input("Druecken Sie Enter, um fortzufahren...")

    print("")
    print("         PROGRAMM BEENDET")