import os
os.system('cls')
# scientific calculator by define function.
import math

#adding 
def add(b,*a):
    sum=b
    for x in a:
        sum+=x
    print(sum)

#substraction
def sub(b,*a):
    sub=b
    for x in a:
        sub-=x
    print(sub)

#multiplication
def mul(b,*a):
    mul=b
    for x in a:
        mul*=x
    print(mul)

#division
def div(b,*a):
    div=b
    for x in a:
        div/=x
    print(format((div),".6f"))

#modulous
def mod(b,a):
    c=b%a
    print(c)

#squareroot
def squareroot(b,*a):
    d=input("operator is(+,-,*,/,): ")
    if d=="+":
        sum=b
        for x in a:
            sum+=x
    elif d=="-":
        sum=b
        for x in a:
            sum-=x
    elif d=="*":
        sum=b
        for x in a:
            sum*=x
    elif d=="/":
        sum=b
        for x in a:
            sum/=x
    else:
        sum=b
    print("ANS= ",format(math.sqrt(sum),".6f"))

#exponent
def exponent(a,b):
    c=math.pow(a,b)
    print(format((c),".12f"))

#trignometric function
#sine function
def sin(a):
    b=math.sin(a)
    print("value is: ",format((b),".4f"),)

#coscent function
def cos(a):
    b=math.cos(a)
    print("Value is: ",format((b),".4f"))

#tangent function
def tan(a):
    b=math.tan(a)
    print("Value is: ",format((b),".4f"))

#cosine function
def cosec(a):
    b=1/math.sin(a)
    print("Value is: ",format((b),".4f"))

#secant function
def sec(a):
    b=1/math.cos(a)
    print("Value is: ",format((b),".4f"))

#cotangent
def cot(a):
    b=1/math.tan(a)
    print("Value is: ",format((b),".4f"))

#degree to radian
def radian(a):
    b=math.radians(a)
    print(format((b),".6f"))

#radian to degree
def degrees(a):
    b=math.degrees(a)
    print(format((b),".6f"))

squareroot(67,89,74,73)