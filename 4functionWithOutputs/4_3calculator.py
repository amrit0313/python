def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2
def calculator():
    n1= float(input('Enter first number:'))

    operations = {
        '+':add,
        '-':subtract,
        '*':multiply,
        '/': divide 
    }

    for symbol in operations:
        print(symbol)
    shouldContinue = True

    while shouldContinue:
        operator = input('pick a operator from above: ')
        n2= float(input('Enter next number: '))
        function = operations[operator]
        result = function(n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        if input(f"Enter 'y' for continuing calculations with {result} or enter 'n' to start again: " ) == 'y':
            n1 = result
        else:
            shouldContinue = False
            calculator()


calculator()