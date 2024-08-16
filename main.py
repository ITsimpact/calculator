first = int(input('first number: '))
second = int(input('second number: '))
operator = str(input('operator: '))


with open('calculator.txt' , 'w') as file:
    file.write(f'first number is {first} \n')
    file.write(f'second number is {second} \n')
    file.write(f'operator is {operator} \n')


def plus(a , b):
    result = (a + b)
    with open('calculator.txt' , 'w') as file:
        file.write(f'first number is {first} \n')
        file.write(f'second number is {second} \n')
        file.write(f'operator is {operator} \n')
        file.write(f'result is {result}')


def minus(a , b):
    result = (a - b)
    with open('calculator.txt' , 'w') as file:
        file.write(f'first number is {first} \n')
        file.write(f'second number is {second} \n')
        file.write(f'operator is {operator} \n')
        file.write(f'result is {result}')


def deleniye(a , b):
    result = (a / b)
    with open('calculator.txt' , 'w') as file:
        file.write(f'first number is {first} \n')
        file.write(f'second number is {second} \n')
        file.write(f'operator is {operator} \n')
        file.write(f'result is {result}')

def umnojeniye(a , b):
    result = (a * b)
    with open('calculator.txt' , 'w') as file:
        file.write(f'first number is {first} \n')
        file.write(f'second number is {second} \n')
        file.write(f'operator is {operator} \n')
        file.write(f'result is {result}')
try:
    if operator == '+':
        plus(first , second)
    elif operator == '-':
        minus(first , second)
    elif operator == '/':
        deleniye(first , second)
    elif operator == '*':
        umnojeniye(first , second)
except ValueError:
    print('type numbers')
except ZeroDivisionError:
    print('the 0 not dividing ')