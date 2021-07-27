# CALCULATOR

#add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1/n2

#exponent
def exponent(n1, n2):
    return n1 ** n2

#modulus
def modulus(n1, n2):
    return n1%n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "e" : exponent,
    "%" : modulus
}

def calculator():
    num1 = float(input("What's the first number?: "))

    print("The operations are: ")
    for key in operations:
        print(key)

    continuar = True
    while continuar :
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Wha's the second number?: "))
        calculation_function = operations[operation_symbol] 
        #con esto asignamos el nombre de la función, donde como tal sera reemplazada
        #por el nombre de la función y solo necesita los argumentos para ser llamada
        #llamar_funcion = subtract
        #print(llamar_funcion(5,2))

        answer1 = calculation_function(num1, num2 )
        print(f"{num1} {operation_symbol} {num2} = {answer1}")

        if input(f"Type 'y' to continue calculating with {answer1}, or type 'n' to exit: ") == "y":
            num1 = answer1
        else:
            continuar = False
            calculator()

calculator()
        








