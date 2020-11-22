str=input("Enter the sentence:\n")
d=dict()

for i in str:
    d[i]=d.get(i,0)+1
print("Dictionary:",d)
count=0
for k,v in d.items():
    count=count+v
print("The total count of characters are:",count)
