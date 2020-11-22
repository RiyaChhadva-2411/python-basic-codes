lst=list()
n=int(input("Enter the number of elements you want in a list:\n"))
print("Enter the numbers:")

for i in range(n):
    numbers=int(input())
    lst.append(numbers)

def evenodd(lst):
    even=list()
    odd=list()
    for i in lst:
        if i%2==0:
            even.append(i)
        elif i%2!=0:
            odd.append(i)
    print("Even numbers are:",even)
    print("Odd numbers are:",odd)

print(evenodd(lst))
