lst=list()
n=int(input("Enter how many numbers you want in a list:\n"))
print("ENter the numbers:")

for i in range(n):
    numbers=int(input())
    lst.append(numbers)

def check(lst):
    positive=list()
    negative=list()
    for i in lst:
        if i>0:
            positive.append(i)
        elif i<0:
            negative.append(i)
    print("Positive numbers are:", positive)
    print("Negative numbers are:", negative)

print(check(lst))
