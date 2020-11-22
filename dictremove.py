#str=input("Enter a string or sentence:\n")
#d=dict()
#a=input("Enter the character or a word to be removed:\n")

#for i in str:
    #d[i]=d.get(i,0)+1

#print("Dictionary:",d)

#del d[a]
#print("The modified dictionary is:",d)

#to delete a word from a Dictionary

str=input("Enter the string or a sentence:\n")
lst=list()
lst=str.split()
counts=dict()

for i in lst:
    counts[i]=counts.get(i,0)+1

print("Dictionary:",counts)

a=input("Enter the word to be deleted from dictionary:\n")
del counts[a]
print("The modified dictionary is:",counts)
