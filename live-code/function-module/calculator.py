def calculator(operands,operator="+"):
    result  = 0
    if operator == "+":
        for item in operands: 
            result = result + item #result += item
    elif operator == "-":
        result = operands[0]
        for item in operands: 
            result = result - item #result -= item
        #return result
    elif operator == "*":
        result = 1
        for item in operands: 
            result = result * item 
    elif operator == "/":
        result = operands[0]
        for item in operands: 
            result = result / item #result += item
    else:
        print("Operator entry is not valid!")
    
    print("End of function!")
    return result
