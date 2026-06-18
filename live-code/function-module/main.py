from calculator import calculator

operands = []
while True: 
    operand = input("Enter the Operand or [quit]\n")
    if operand.lower() == "quit":
        print("Continue with calculation")
        break
    if not isinstance(float(operand),float): 
        print("The input entered is not an operand.")
        break
    else:
        operands.append(float(operand))

print(operands)
if len(operands) > 2:
    operator = input("Enter the operator\n")
    result = calculator(operands,operator)
    print(result)
else:
    print("Please restart. Too few operands!")