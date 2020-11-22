#def multiply(string,multi_int=10):
#    return string * multi_int
#string="My name is Riya"
#print(multiply(string))


#lambda functions
#neg= lambda x:-x

#g= lambda x: 2*x+10+5

# ZIP functions

first=list()
n=int(input("Enter how many names you want!\n"))
print("ENter the names:")
for i in range(n):
    names=input()
    first.append(names)

second=list()
m=int(input("Enter how many names you want!\n"))
print("ENter the names:")
for i in range(m):
    name=input()
    second.append(name)

lst=zip(first,second)
print(list(lst))
