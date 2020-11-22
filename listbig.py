lst=list()
n=int(input("Enter the number of elements you want in a list:"))
print("Enter the numbers:")
for i in range(n):
    numbers=int(input())
    lst.append(numbers)

def max(lst):
    max=0
    for i in lst:
        if i > max:
            max=i

    return max
print("The greatest number among the list is:",max(lst))

def min(lst):
    for i in lst:
        min=i
        if i<min:
            min=i
    return min
print("The smallest number among the list is:",min(lst))
