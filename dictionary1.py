#program 14
swimmers={"Manuel":4,"Lochte":12,"Adrian":7,"Ledecky":5,"Dirado":4,"Phelps":23}
print(swimmers)
swimmers["Phelps"]=swimmers["Phelps"]+5
print("The modified dictionary is:",swimmers)

print("*******************************************************************************")
#program 15
travel={"North America":2,"Europe":8,"South America":3,"Asia":4,"Africa":1,"Antartica":0,"Australia":1}
print(travel)
total=0
for k,v in travel.items():
     total=total+v

print("The total number of countries that Jackie has travelled to are:",total)

print("*******************************************************************************")
#program 16
placement="Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore"
counts=dict()
for i in placement:
    counts[i]=counts.get(i,0)+1

print(counts)

smallword=None
smallcount=None

for word,count in counts.items():
    if smallcount is None or count<smallcount:
        smallword=word
        smallcount=count

print(smallword,smallcount)

print("*******************************************************************************")
#program 17
product="iphone and android phones"
d=dict()

for i in product:
    d[i]=d.get(i,0)+1
print("Dictionary:",d)

bigword=word
bigcount=count

for word,count in d.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)

#program 18
