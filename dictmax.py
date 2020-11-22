str=input("Enter the string or the sentence:\n")
counts=dict()

for i in str:
    counts[i]=counts.get(i,0)+1

print("The dictionary is:\n",counts)

bigword=None
bigcount=None


for word,count in counts.items():
    if bigcount is None or count> bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)
