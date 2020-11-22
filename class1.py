#program1 : Creating a class and its object

class Myclass:
    x=12
    y=98
    u=56
    r=90

obj_1=Myclass()
print(obj_1.x)
print(obj_1.y)
print(obj_1.u)
print(obj_1.r)

print("************************************************")
#program2 : Using the __init__() function:

class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name

obj1=Person(20,"Hem")
obj2=Person(20,"Riya")

print(obj1.name)
print(obj1.age)
print(obj2.name)
print(obj2.age)

print("************************************************")
#program3 : How to take user-defined values

class Animal:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

x=input("Enter the name of the first animal:\n")
y=input("Enter the colour of the first animal:\n")
a=input("Enter the name of the second animal:\n")
b=input("Enter the colour of the second animal:\n")

obj1=Animal(x,y)
obj2=Animal(a,b)
print("\n")
print(obj1.name)
print(obj1.colour)
print(obj2.name)
print(obj2.colour)

print("************************************************")
#program4 :Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2, which hold each of the input integers. Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10. Save this instance to a variable t. 

class NumberSet:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

t=NumberSet(6,10)
print(t.num1)
print(t.num2)
