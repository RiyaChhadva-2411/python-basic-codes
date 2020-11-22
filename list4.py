#program 8
z=30
y=22
if z>y:
    y=y+5
    print("y=",y)
else:
    print("Do nothing!")

x=z*y
print("The multiplication of z and y is:",x)

#program 9
wrd_lst=["Hello","activecode","Java","C#","Python","HTML and CSS","Javascript","Swift","php"]
count=0
for i in wrd_lst:
    if len(i)<6:
        count=count+1

print(count,"words are present in the given list whose length is less than 6")

#program 10
original_str="The quick brown rhino jumped over the extremely lazy fox"
lst=list()
lst=original_str.split()
print("List:",lst)

for i in lst:
    print(len(i))

#program 11
stopwords=["to","a","for","by","an","am","the","so","it","and","The"]
print(stopwords)
org="The organization for health, safety, and eduaction"
lst=list()
lst=org.split()
print(lst)

for i in lst:
    if i in stopwords:
        lst.remove(i)

print("The modified list is:",lst)

new_str=''.join(lst)
print(new_str)

#program 12
scores="67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
lst=list()
lst=scores.split()
print("List of scores:",lst)
count=0

for i in lst:
    i=int(i)
    if i>=90:
        count=count+1
        print(i)

print("The count of scores above 90 are:",count)
