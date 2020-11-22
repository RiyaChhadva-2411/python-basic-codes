lst=list()
str=input("Enter the names in the string:\n")

a=str.split()
print(a)

even=list()
odd=list()
for i in a:
    if (len(i)%2==0):
        even.append(i)
    elif (len(i)%2!=0):
        odd.append(i)

print("The list with even number of strings is:",even)
print("The list with odd number of strings is:",odd)
