lst=list()
str=input("Enter the sentence:\n")
a=int(input("Enter the user defined number:\n"))

lst=str.split()
newlst=list()

for i in lst:
    if len(i)>a:
        newlst.append(i)


print(newlst)
