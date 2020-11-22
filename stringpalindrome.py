str=input("Enter the name of the string:\n")
reversed_string= reversed(str)
print(reversed_string)

rev=''.join(reversed_string)
print(rev)

if (str==rev):
    print("It is a palindrome string !")
else:
    print("It is not a palindrome string !")
