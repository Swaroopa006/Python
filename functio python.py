'''def count_lower_upper(str):
    s= 0
    for i in str:
        if (i.isupper()):
            s+=1
    a =0
    for i in str:
        if(i.islower()):
            a+=1
    return(s,a)
def input_():
    str = input("Enter a string")
    g,h = count_lower_upper(str)
    d = {'lower':g, 'upper': h}
    print(d)
input_()

q2)def addval(n):
    s = 0
    v = n
    for i in range(4):
        s = s+n
        n = n*10+v
        print(i, n, s)
    return s

for x in range(4,8):
    print(addval(x))

q3) def create_array1(x,n):
    I =[]
    for i in range(x):
        I = I +[n]
    return I

x = int(input('How many elements you want to create in array:'))
n = int(input('With what value should I inialize this array:'))
a1 = create_array1(x,n)
print(a1)

#def create_array2(x,y,n):
 #   I= []
  #  for i in range(x):
   #     m = m.append(I)

def create_array3(x,y,z,v):
    I = []
    for i in range(x):
        m = []
        for j in range(y):
            n=[]
            for k in range(z):
                n = n+[v]
            m.append(n)
        I.append(n)
    return I
x = int(input('How many rows you want in array:'))
y = int(input('How many columns you want in array:'))
z = int(input('How many elements you want in array:'))
n = int(input('With what value should I inialize this array:'))
a3 =  create_array3(x,y,z,n)
print(a3)

#q4)
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

#q5)
def pangram(s):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    print(alphaset)
    s = s.lower()
    s = set(s)
    return(alphaset <= s)
str = "The quick brown fox jumps over tho lazy dog"
print(str,pangram(str))
str = "Crazy Fredrick bought many vey exquisite opal jewels"
print(str,pangram(str))
str = "Priyam"
print(str, pangram(str))

#q6)
def tuple_in_list(x):
    l =[]
    k = ()
    for i in range(1,x+1):
        k = (i, i*i, i*i*i)
        l.append(k)
    return l
x = int(input("Enter a number:"))
print(tuple_in_list(x))'''


    
    
