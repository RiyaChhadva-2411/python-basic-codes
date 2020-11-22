#r=int(input("Enter the radius of the circle:\n"))


#area=3.14*r*r
#print("The area of the circle is:\n",area)
#circumference=2*3.14*r
#print("The circumference of a circle is:\n",circumference)

def circle(r):
       area=3.14*r*r
       return area
a=circle(3)
print("The area of a circle is:\n",a)



def circlee(rad):
    circumference=2*3.14*rad
    return circumference
c=circlee(2)
print("The circumference of a circle is:\n",c)
