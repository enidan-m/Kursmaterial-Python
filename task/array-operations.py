#Eine leere an usern. Ein User soll in der lange durch input der Liste neue User hinzuzufügen. Wenn der User "quit" eingibt soll keine weitere eingabe möglich sein und die die Liste mit allen hinzugefügten usern ausgegeben werden
 #0. Eine leere Liste 
 #1. Loop damit für die Eingabemöglichkeit 
 # 1.a Bei eingabe von "quit" oder "QUIT" oder "quIt" wird der loop unterbrochen und danach die bestehende Liste mit den Usern ausgegeben
 # TIP: user_entry = input("...").lower()
 #2. Nach dem Eingeben wird der Liste der eingegebene user hinzugefügt
 #Optional: Falls die Liste 10 Einträge groß ist (die Länge bekommt mit len()) wird das Programm beendet und die Liste mit den bestehenden usern ausgegeben
 
usernames = []

while True:
    user_entry = input("Gebe einen username ein.\n")
    if user_entry.lower() == "quit":
        break
    if len(usernames) > 10: 
        break
    usernames.append(user_entry)
print(f"The usernames are:\n{usernames}")