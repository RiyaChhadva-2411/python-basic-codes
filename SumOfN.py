x=int(input("Enter a number:\n"))
sum=0

if (x==0):
    print(x,"is a whole number")
elif (x>=1):
    for i in range(1,x+1):
       sum=sum+i

print("The sum of numbers is\n",sum)
