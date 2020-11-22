n=int(input("Enter a number:"))
if n==0:
    print("Zero is not a prime number or composite number!")
elif n>=1:
    for i in range(2,n):
        if (n%i)==0:
            print(n,"is a composite number!")
            break

else:
    print(n,"is a prime number!")
