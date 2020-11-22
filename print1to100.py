#problem statement: Write a program that prints the numbers from 1 to 100. But for multiples of 3 print "Fizz" instead of number and for the multiplies of 5 print "Buzz" instead of a number. For numbers which are multiples of both 3 and 5 print "FizzBuzz"

#using normal method:
#for i in range(1,101):
#    if(i%3==0 and i%5==0):
#        print("FizzBuzz")
#    elif(i%3==0):
#        print("Fizz")
#    elif(i%5==0):
#        print("Buzz")
#    else:
#        print(i)

#using List:

lst=list()
for i in range(1,101):
    if(i%3==0 and i%5==0):
        lst.append("FizzBuzz")
    elif(i%3==0):
        lst.append("Fizz")
    elif(i%5==0):
        lst.append("Buzz")
    else:
        lst.append(i)

print(lst)
