lst=list()
n=int(input("Enter how many elements you want in your list:\n"))
print("Enter the numbers:")
count=0
for i in range(n):
    numbers=int(input())
    lst.append(numbers)

def occurence(lst , x):
    return lst.count(x)

y=int(input("Enter the number to be checked:"))
print(occurence(lst , y))
#With using dictionary
#counts=dict()
#for i in lst:
#counts[i]= counts.get[i,0]+1
#print("COunts:",count)
