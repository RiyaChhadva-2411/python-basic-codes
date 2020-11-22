counts=dict()
str=input("Enter the sentence:\n")

def countvowels(str):
    for i in str:
        if ("a" in str or "e" in str or "i" in str or "o" in str or "u" in str):
            counts[i]=counts.get(i,0)+1
    return counts
print(countvowels(str))
