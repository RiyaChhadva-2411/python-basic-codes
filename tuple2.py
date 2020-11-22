#program 6 on tuples:If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided you a dictionary called pokemon. For every key value pair, append the key to the list p_names, and append the value to the list p_number. Do not use the .keys() or .values() methods. pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126} 

pokemon={'Rattata':19,'Machop':66,'Seel':86,'Voltbeat':86,'Solrock':126}
print(pokemon.items())
p_names=list()
p_number=list()

for k,v in pokemon.items():
    p_names.append(k)
    p_number.append(v)

print(p_names)
print(p_number)

print("###############################################")
#program 7 on function
def circle(r):
    pi=3.14
    circumference=2*pi*r
    area=pi*r*r
    return(circumference,area)
print(circle(4))

#program 8 on fucntion using tuples

def information(name,birth_year,fav_color,hometown):
    return(name,birth_year,fav_color,hometown)

#program 9 on tuples like unpacking the tuples

def sum(x,y):
    return x+y

z=(6,9)
y=(13,56)
print(sum(*z))
print(sum(*y))

#program 10 on tuples
print("###############################################################")

tuples_lst=[('Beijing','China',2008),('London','England',2012),('Rio','Brazil',2016),('Tokyo','Japan',2020,'Future')]
country=list()
for i in tuples_lst:
    print(i)

for i in tuples_lst:
    country.append(i[1])
print("******************************")
print(country)

#program 11:Write a function called subtract_three that takes an integer or any number as input, and returns that number minus three. 
def subtract_three(x):
    return x-3
print(subtract_three(10))

#program 12:Write a function called change that takes one number as its input and returns that number, plus 7.

def change(x):
    return x+7
print(change(3))

#program 13

def decision(string):
    if len(string)>17:
        return 'This is a very long string'
    else:
        return 'this is a short string'
print(decision("My name is Riya"))
