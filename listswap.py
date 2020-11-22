lst=list()
n=int(input("Enter the number of elements you want in a list:\n"))
print("Enter the numbers:")

for i in range(n):
    numbers=int(input())
    lst.append(numbers)

def swap(lst):
    temp=list()
    size=len(lst)
    temp=lst[0]
    lst[0]=lst[size-1]
    lst[size-1]=temp
    return lst
print("Original list:",lst)
print("Swapped list:",swap(lst))
