#Definition
def calculator(firstOperator,secondOperand,operator="+"):
    result  = 0
    if operator == "+":
        result = firstOperand + secondOperand
        #return result
    elif operator == "-":
        result = firstOperand - secondOperand
        #return result
    elif operator == "*":
        result = firstOperand * secondOperand
        #return result
    elif operator == "/":
        result = firstOperand / secondOperand
        #return result
    else:
        print("Operator entry is not valid!")
    
    print("End of function!")
    return result


operator = input("Enter the operator\n")
firstOperand = input("Enter the first operand\n")
secondOperand = input("Enter the second operand\n")
operands = [firstOperand,secondOperand]
result = calculator(firstOperand,secondOperand,operator)
print(result)




# def calculator(operands,operator="+"):
#     result  = 0
#     if operator == "+":
#         for item in operands: 
#             result = result + item #result += item
#     elif operator == "-":
#         result = operands[0]
#         for item in operands: 
#             result = result - item #result -= item
#         #return result
#     elif operator == "*":
#         result = 1
#         for item in operands: 
#             result = result * item 
#     elif operator == "/":
#         result = operands[0]
#         for item in operands: 
#             result = result / item #result += item
#     else:
#         print("Operator entry is not valid!")
    
#     print("End of function!")
#     return result

# #Aufruf
# operands = []
# while True: 
#     operand = input("Enter the Operand or [quit]\n")
#     if operand.lower() == "quit":
#         print("Continue with calculation")
#         break
#     if not isinstance(float(operand),float): 
#         print("The input entered is not an operand.")
#         break
#     else:
#         operands.append(float(operand))

# print(operands)
# if len(operands) > 2:
#     operator = input("Enter the operator\n")
#     result = calculator(operands,operator)
#     print(result)
# else:
#     print("Please restart. Too few operands!")

