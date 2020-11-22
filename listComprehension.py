#program 1

alist=[4,5,6,7,8,9]

oddnumbers=[i*2 for i in alist if i%2!=0]
print(oddnumbers)

print("********************************************")

#program 2
lst=list()
n=int(input("Enter the length of the list:\n"))
print("Enter the numbers:")

for i in range(n):
    numbers=int(input())
    lst.append(numbers)

print("List:\n",lst)

new_lst=[i*2 for i in lst]
print(new_lst)
print("***********************************************")
