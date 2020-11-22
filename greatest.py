a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
print("**********************************")
if (a>b)and(a>c):
    print("The largest number is:",a)
elif (b>a)and(b>c):
    print("The largest number is:",b)
elif (c>a)and(c>b):
    print("The largest number is:",c)
