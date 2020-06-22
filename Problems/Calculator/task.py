a = float(input())
b = float(input())
ope = input()


if ope == '+':
    print(a + b)
elif ope == '-':
    print(a - b)
elif ope == '*':
    print(a * b)
elif ope == '/':
    if b != 0:
        print(a / b)
    else:
        print('Division by 0!')
elif ope == 'mod':
    if b != 0:
        print(a % b)
    else:
        print('Division by 0!')
elif ope == 'div':
    if b != 0:
        print(a // b)
    else:
        print('Division by 0!')
elif ope == 'pow':
    print(a ** b)
