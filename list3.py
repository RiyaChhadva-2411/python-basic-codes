#program 6
rainfall_mi="1.65,1.46,2.05,3.03,3.35,3.46,2.83,3.23,3.5,2.52,2.8,1.85"
lst4=[]
new_lst=rainfall_mi.split(',')
print(new_lst)
for i in new_lst:
    print(i)
    i2=float(i)
    if i2>3:
        lst4.append(i2)
print(lst4)

#program 7
sentence="python is a high level general purpose programming language that can be applied to many different classes of problems"
lst=list()
lst=sentence.split()
print(lst)
new_lst=list()
for i in lst:
    if "a" in i or "e" in i:
        new_lst.append(i)

print(new_lst)
