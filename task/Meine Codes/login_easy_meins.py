# input("gebe deinen usernamen ein\n")
username_1 = input("gebe deinen unsernamen ein\n")
passwort_1 = input("gebe dein passwort ein\n")
#print(username_1)
if username_1 == "root" and passwort_1 == "admin": 
    print("Willkommen Admin")
    print(f"""
          #1 Taschenrechner (Addition)
          #2 Taschenrechner (Subtraktion)
          #3 Taschenrechner (Division)
          #4 Taschenrechner (Multiplikation)
          """)
    option = input("Wähle\n")
    if option == "1": 
        print("Addition\n")
        Addition_1 = float(input("Gebe eine Zahl an\n"))
        Addition_2 = float(input("Gebe eine Zahl an\n"))
        result = Addition_1 + Addition_2
        print(f"{result}")
        #copy / paste für alle weiteren Rechenarten
    elif option == "2":
        print("Subtraktion\n")
    elif option == "3":
        print("Division\n")
    elif option == "4":
        print("Multiplikation\n")
    else:
        print("Nicht möglich")
else: 
    print("Falsche Eingabe")
#input("ABC")
