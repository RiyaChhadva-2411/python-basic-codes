str=input("Enter the sentence or string ny the user:\n")
counts=dict()


for i in str:
    counts[i]=counts.get(i,0)+1

print("Dictionary:\n",counts)

keys=list(counts.keys())
print(keys)

for i in keys:
    print(counts[i])

for i in keys:
    if counts[i]>1:
        del counts[i]

print(counts)
new_str=''.join(counts)
print(new_str)
