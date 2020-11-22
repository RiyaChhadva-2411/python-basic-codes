str=input("Enter the string or sentence:\n")
a=input("Enter a character to be removed:\n")
lst=list()



for i in str:
    lst.append(i)

for i in lst:
    if a in lst:
        lst.remove(a)
    #else:
        #print("The character does not exist in the given string")
newstr=''.join(lst)
print("The new string is:",newstr)
