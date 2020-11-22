str=input("Enter the sentence:\n")
vowel=list()
vowel.append("a")
vowel.append("e")
vowel.append("i")
vowel.append("o")
vowel.append("u")
count=0
for i in str:
    if i in vowel:
        count=count+1

print("The number of vowels in the sentence are", count)

#The other method

#str=input("Enter the sentence:")

#def vowel(str):
    #count=0
    #if "a" in str and "e" in str and "i" in str and "o" in str and "u" in str:
        #count=count+1
        #return count


#print(vowel(str))
