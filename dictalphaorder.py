str=input("Enter the string or sentence:\n")
counts=dict()

new_str=str.lower()
for i in new_str:
    counts[i]=counts.get(i,0)+1

print(counts)

keys=list(counts.keys())

new_keys=sorted(keys)

for i in new_keys:
    print(i,counts[i])
