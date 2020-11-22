str=input("Enter the name of the string:\n")
str_1="ing"
lst=list()
lst=str.split()
print(lst)
newlst=list()
for i in lst:
    newlst.append(i+str_1)

newstr=' '.join(newlst)
print("The new list is appending ing words is:",newstr)
