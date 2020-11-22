lst=list()
n=int(input("Enter the number of elements you want in your array:"))
print("Start entering the numbers:")
print("Enter the numbers:")
for i in range(n):
    numbers=int(input())
    lst.append(numbers)

def sum(lst):
    sum=0
    for i in lst:
        sum=sum + i

    return sum

print("The sum of number is:",sum(lst))
