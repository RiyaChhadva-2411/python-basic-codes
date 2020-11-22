#This counts a single character in a string or sentence
#counts=dict()
#str=input("Enter a single string or the sentence:\n")

#for i in str:
    #counts[i]=counts.get(i,0)+1

#print("Dictionary:",counts)


#This counts how many times a word occurs in a sentence
str=input("Enter the sentence:\n")
lst=list()
counts=dict()

lst=str.split()

for word in lst:
    counts[word]=counts.get(word,0)+1

print("Dictionary:", counts)
