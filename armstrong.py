n=int(input("Enter a number from user:\n"))
#count=0

#while (n>0):
    #count=count+1
    #n=n//10

#print(count)
sum=0
digit=0
temp=n
while (temp>0):
    digit=temp%10
    sum+=digit ** 3
    temp=temp//10

if(n==sum):
    print("The given number is an armstrong number!")
else:
    print("The given number is not an armstrong number!")
