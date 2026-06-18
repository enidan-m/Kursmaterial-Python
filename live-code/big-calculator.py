# calculator_db = [
#     {
#        "operator": "+",
#        "operanden": [10,15,25],
#        "result": 50,
#        "isDisplayed": False
#     },
#     {
#        "operator": "-",
#        "operanden": [10,15,25],
#        "result": -30,
#         "isDisplayed": False
#     }
# ]


# for item in calculator_db:
#     print(f"""
#           Die folgende Berechnungsart wurde durchgeführt: {item["operator"]}
#           Die folgenden Operanden wurden verwendet: {item["operanden"]}
#           Das Ergebnis der Berechnung ist: {item["result"]}
#           """)
#     item["isDisplayed"] = True
    
# print(calculator_db)

calculator_db = [
    
]

while True: 
    start_calculating = input("Do you want to start calculating. If you want stop please enter [quit]")
    if start_calculating.lower() == "quit":
        break
    operator = input("Please enter the operator [+|-|*|/]")
    operands = []
    while True:
        operand = input("Enter the operand to use. If you are done, please enter [quit]")
        if operand.lower() == "quit":
            print("You entered your inputs. Continue with next step!")
            break
        if not isinstance(float(operand),float):
            break
    
        operand = float(operand)
        operands.append(operand)
    #prüfe die länge der Liste, wenn diese kleiner als zwei ist, breche die Schleife (Programm) ab.
    if len(operands) < 2:
        print("Das Programm wird beendet, weil zu wenige Operanden eingegeben wurden!")
        print(f"Der einzige angegebene Operand entspricht {operands}")
        break
    
    #Berechnung durchführen 
    result = 0
    if operator == "+":
        #z.b [10,15,25] als operanden, also gehe mit schleife darüber
        for item in operands:
            result += item
    elif operator == "-":
        for item in operands:
            result -= item
    elif operator == "*":
        result = 1  # wir wollen nicht mit 0 * 10 starten, sondern 1* 10 = 10 * 15 = 150 usw.
        for item in operands:
            result = result * item
        
    elif operator == "/":
        #Wir nehmen den ersten Wert 10 / 15 / 25
        result = operands[0] #Speichere den ersten Wert der Operanden als zu teilenden Wert
        operands_remaining = operands[1:] #Die restlichen Werte sind die Divisoren
        for item in operands_remaining:
            result = result / item
    result = round(result,3) 
    print(f"""
           Die folgende Berechnungsart wurde durchgeführt: {operator}
           Die folgenden Operanden wurden verwendet: {operands}
           Das Ergebnis der Berechnung ist: {result}        
          """)
    
    #Frage ob Berechnung gespeichert werden soll:
    save_calculation = input("Do you want to save the calculation history?[y|n]")
    if save_calculation.lower() == "y":
        calculation = {}
        calculation["operator"] = operand
        calculation["operands"] = operands
        calculation["result"] = result
        calculation["isDisplayed"] = False
        calculator_db.append(calculation)
        print("Displaying updated  calculation history")
        print(calculator_db)
    elif save_calculation.lower() == "n":
        print("Displaying current saved calculation history")
        print(calculator_db)
        