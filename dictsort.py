d=dict()
str=input("Enter a string or a sentence:\n")
lst=sorted(str)
print("List:",lst)

for i in lst:
    d[i]=d.get(i,0)+1

print("Dictionary:" , d)
