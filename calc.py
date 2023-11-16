import os
os.system('clear')
def add():
    sum = a+b
    print("The sum is ", sum)
def sub():
    diff = a-b
    print("The difference is " , diff)
def mult():
    prod = a*b
    print("The product is ",prod)
def div():
    try:
        quo = a/b
        print(quo)
    except ZeroDivisionError:
        quo = 0
        print("Division by 0 is not possible")
while(1):
    a = float(input("Enter a number "))
    b = float(input("Enter another number "))
    op = input("Which operation do you want to perform? \n + for addition \n - for subtraction \n * for multiplication \n / for division \n")
    if op ==  '+':
        add()
    elif op ==  '-':
        sub()
    elif op ==  '*':
        mult()
    elif op == '/':
        div()
    elif op ==  'q':
        print("Thank you for using my calculator")
        break
    else:
        print("Invalid operation input")
