#p=float(input("Enter the principal:\n"))
#t=float(input("Enter the time:\n"))
#r=float(input("Enter the rate:\n"))

#SimpleInterest=(p*t*r)/100
#print("The simple interest is:\n",SimpleInterest)

def SimpleInterest(p,t,r):

    si=(p*t*r)/100
    return si

y=SimpleInterest(23.22,56,8.98)
print("The SImple Interest is:\n",y)
