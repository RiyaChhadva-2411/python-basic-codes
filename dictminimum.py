d=dict()
str=input("Enter the string or sentence:\n")
lst=list()
lst=str.split()
for i in lst:
    d[i]=d.get(i,0)+1
print("Dictionary:\n",d)

for k,v in d.items():
    if v<2 and v>0:
        lst.append(k)

print(lst)
