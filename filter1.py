#program 1
#lst_check=['plums','watermelon','kiwi','strawberries','blueberries','peaches','apples','mangoes','papaya']

#def check(x):
#    if 'w' in x:
#        return True
#    else:
#        return False

#fruits=filter(check,lst_check)
#for i in fruits:
#    print(i)

# USING LAMBDA FUNCTION

lst_check=['plums','watermelon','kiwi','strawberries','blueberries','peaches','apples','mangoes','papaya']

fruits=filter((lambda x:'w' in x ),lst_check)

for i in fruits:
    print(i)

print("********************************************************************")

#program 2
n=int(input("Enter how many numbers you want in your list:\n"))
print("Enter the number:\n")
lst=list()
for i in range(n):
    numbers=int(input())
    lst.append(numbers)
print(lst)

def evenodd(x):
    if x%2==0:
        return True
    else:
        return False

even=filter(evenodd,lst)
new_lst=list()
for i in even:
    new_lst.append(i)

print(new_lst)

print("****************************************************************")

#program 3
lst=["witch","halloween","pumpkin","cat","candy","wagon","moon"]
new_lst=list()
lst2=filter((lambda x:"o" in x),lst)
for i in lst2:
    new_lst.append(i)

print(new_lst)
