
str=input("Enter the string:\n")

def vowel(str):
    if "a" in str or "e" in str or "i" in str or "o" in str or "u" in str:
        return "The string contains vowels!"
    else:
        return "The string doesnt contain any vowel!"
print(vowel(str))
