n=int(input("Enter the number:"))
f=1
if n<0:
    print("Factorial of the given number does not exist!")
elif n>=1:
    for i in range(1,n+1):
       f=f*i
print("Factorial of the given number", +n, "is",f)
