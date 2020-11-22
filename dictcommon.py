lst=list()
str=input("Enter the string or sentence by the user:\n")
count=dict()

for i in str:
    count[i]=count.get(i,0)+1

print("Dictionary:",count)

for k,v in count.items():
    if v>1:
        lst.append(k)

print(lst)
