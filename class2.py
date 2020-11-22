#program5: Taking more than one functions at a time:

class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age
    def getName(self):
        print("The name is:",self.name)
    def getAge(self):
        print("The age is:",self.age)

obj=Person(20,"Riya")
obj.getName()
obj.getAge()

#program6:

class Animal:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    def getDetails(self):
        print("The name and colour of animal is:\n", self.name, self.colour)

obj=Animal("Lion","Yellow")
obj.getDetails()

#program7: Addition of two numbers using oop python:

class Operations:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("The addition of two numbers is:\n",self.num1 + self.num2)
    def subtract(self):
        print("The subtraction of two numbers is:\n",self.num1 - self.num2)
    def multiply(self):
        print("The multiplication of two numbers is:\n",self.num1 * self.num2)
    def divide(self):
        print("The division of two numbers is:\n",self.num1 / self.num2)
    def modulus(self):
        print("The modulus of two numbers is:\n",self.num1 % self.num2)
    def average(self):
        print("The average of two numbers is:\n",(self.num1/self.num2)/2)

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))


obj=Operations(x,y)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()
obj.modulus()
obj.average()
print("---------------------------------------------------------------------------")
#program 8: __str__() pre-defined function in python classes and objects
class numb:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __str__(self):
        return 'x is {} and y is {}'.format(self.x,self.y)

obj=numb(16,23)
print(obj.getX())
print(type(obj.getX()))
print("-------------------------")
print(obj.getY())
print(type(obj.getY()))
print("-------------------------")
print(obj.__str__())
print(type(obj.__str__()))
print("--------------------------")
print(obj)
print(type(obj.__str__()))
