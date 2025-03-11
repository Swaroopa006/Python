'''def add(x,y):
    return x+y
    #print("Sum of numbers:", c)

def sub(x,y):
    return x-y
    #print("Sub of numbers:", c)


def multiply(x,y):
    return x*y
    #print("multiply of numbers:", c)

def div(x,y):
    return x/y
    #print("Div of numbers:", c)


x = int(input("Enter the number:"))
y = int(input("Enter the 2nd number:"))

def calci():
    print("Select operator:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")

    choose = input("Enter the operator number(1/2/3/4):")

    if choose == '1':
        print("Sum of numbers:", {add(x,y)})
        #add(x,y)
    elif choose == '2':
        print("subtraction of numbers:", {sub(x,y)})
        #sub(x,y)
    elif choose == '3':
        print("multiplication of numbers:", {multiply(x,y)})
        #multiply(x,y)
    elif choose == '4':
        print("division of numbers:",{div(x,y)})
        #div(x,y)
    else:
        print("Invalid input")
calci()


def add(x,y,z,a,b):
    c = x+y+z+a+b
    print("Sum is:", c)
    
def avg(x,y,z,a,b):
    v = (x+y+z+a+b)/5
    print("Average is:", v)

x = int(input("Enter the 1st number:"))
y = int(input("Enter the 2nd number:"))
z = int(input("Enter the 3rd number:"))
a = int(input("Enter the 4th number:"))
b = int(input("Enter the 5th number:"))

add(x,y,z,a,b)
avg(x,y,z,a,b)

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter a number: "))
print(f"Factorial of a number is {fact(n)}")'''

def count_lower_upper(str):
    i= 0
    u = 0
    for i in str:
        if (i.isupper()):
    str = input("Enter a string")
count_lower_upper()
































    
