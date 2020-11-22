lst=list()
n=int(input("Enter the number of elements you want in a list:\n"))
print("Enter the numbers:")

for i in range(n):
    numbers=int(input())
    lst.append(numbers)

def check(lst):
    a=int(input("Enter a number to be checked:"))
    if a in lst:
        return("Number found")
    else:
        return("Number not found")

print(check(lst))
