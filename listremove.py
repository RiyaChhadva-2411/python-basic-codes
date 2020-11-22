lst=list()
n=int(input("Enter how many numbers you want in your list:\n"))
print("Enter the numbers:")

for i in range(n):
    numbers=int(input())
    lst.append(numbers)
print("**********************************************************")
a=int(input("Enter the number you want to remove from a list:\n"))
for i in lst:
    if a in lst:
        lst.remove(a)
else:
    print("Number not found in the list!")


print("The list after removing an element is",lst)
