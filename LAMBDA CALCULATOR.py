#Joana is participating in a selection process for a developer position and 
# has received a technical challenge to create a calculator to add, subtract, multiply, and divide two numbers.
# Her task is to create a program using lambda functions that receives two numbers and a mathematical operator 
# chosen by the user (+, -, *, or /) and displays the corresponding result.




first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

operation = input('Choose the mathematical operation (+, -, *, /): ')

if operation not in operators:
    print("Invalid operation!")
elif operation == '/' and second_number == 0:
    print("Error: division by zero!")
else:
    result = operators[operation](first_number, second_number)
    print(f'The result is: {result:.2f}')