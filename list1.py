several_things=["hello",2,4,6.0,7.5,234352354,"the end","",99]

#program 1
for i in several_things:
    print("List:",i)
#program 2
for j in several_things:
    print(type(j))
#program 3
str_list= ["hello","","goodbye","wonderful","I love Python"]

for k in str_list:
    print(len(k))

#program 4
addition_str="2+5+10+20"
lst=list()
lst=addition_str.split("+")
print(lst)
sum=0
for i in lst:
    j=int(i)
    sum=sum+j

print(sum)
#program 5
week_temps_f="75.1,77.7,83.2,82.5,81.0,79.5,85.7"
lst=list()
lst=week_temps_f.split(",")
print(lst)
sum=0
count=0
for i in lst:
    i=float(i)
    count=count+1
    sum=sum+i

avg=sum/count
print("Average of numbers in list:\n",avg)
