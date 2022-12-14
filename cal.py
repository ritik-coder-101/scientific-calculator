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
    print(format(div),".12f")

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
    print(format(math.sqrt(sum),".12f"))

#exponent
def exponent(a,b):
    c=math.pow(a,b)
    print(format((c),".12f"))

#trignometric function
#sine function
def sine(a):
    b=math.sin(a)
    print("value is: ",format((b),".4f"),)

sine(89)