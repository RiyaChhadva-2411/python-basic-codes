lst=list()
n=int(input("Enter how many elements you want in the list:\n"))
print("Enter the numbers:")

for i in range(n):
    numbers=int(input())
    lst.append(numbers)

#For Descending
#lsttwo=sorted(lst , reverse = True)
#print("The sorted list is:\n",lsttwo)

#For Ascending
lsttwo=list()
lsttwo=sorted(lst)
print("The sorted list in ascending order is:\n", lsttwo)
