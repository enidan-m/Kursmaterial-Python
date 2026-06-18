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

#def gruesse(name): 
    #print(f"Hallo, {name}")

#gruesse("Anna")
#gruesse("Ben")
#gruesse("Clara")


#AUFGABE 2: SUMME BEREICHNEN (SEHR EINFACH)
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


#def summe(firstOperand, secondOperand, operator="+"):
    #if operator == "+":
        #result = firstOperand + secondOperand
       # return result

#operator = input("Enter the operator\n")
#firstOperand = float(input("Enter the first operand\n"))
#secondOperand = float(input("Enter the second operand\n"))
#operands = [firstOperand,secondOperand]
#result = summe(firstOperand,secondOperand,operator)
#print(result)


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

#def quadrat(operand):
    #return operand ** 2 

#operand = float(input("Enter operand\n"))
#result = quadrat(operand)
#print(result)

#AUFGABE 4: GERADE ODER UNGERADE (EINFACH)
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

#def ist_gerade(operand):
    #if operand % 2 == 0:
        #return True 
    #else:
        #return False

#number = float(input("Gebe eine Zahl ein\n"))
#print(ist_gerade(number))
#even_or_odd = ist_gerade(number)
#print(even_or_odd)


#AUFGABE 5: MEHRERE FUNKTIONEN (EINFACH)
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

#def addieren(a, b):
   # return a + b

#def sub(a, b):
    #return a - b 

#def multi(a, b):
    #return a * b

#number_1 = float(input("Zahl 1\n"))
#number_2 = float(input("Zahl 2\n"))
#operator = input("operator (+, -, *)\n")

#if operator == "+":
    #result = addieren(number_1, number_2)

#elif operator == "-":
    #result = sub(number_1, number_2)

#elif operator == "*":
    #result = multi(number_1, number_2)
    
#print(result)


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

def begruessung(name, anrede="Hallo"):
    print(f"{anrede} {name}\n")
begruessung("Max","Hi")