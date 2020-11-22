# program 1
lst=list()
n=int(input("Enter the length of the list:\n"))
print("Enter the numbers:")

for i in range(n):
    numbers=int(input())
    lst.append(numbers)

print(lst)
new_lst=list()
x=0
sum=0
while(x<len(lst)):
    sum=sum+lst[i]
    x=x+1

print(sum)
