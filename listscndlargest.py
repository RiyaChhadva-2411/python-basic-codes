lst=list()
n=int(input("Enter hoe many numbers you want in your list:\n"))
print("Enter the numbers:")

for i in range(n):
    numbers=int(input())
    lst.append(numbers)

lst.sort()
print("The second largest number is:" , lst[-2])
