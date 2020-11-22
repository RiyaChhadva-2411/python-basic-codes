#problem 1 on tuples
#This is called the packing of the tuple
#practice=('y','h','z','x')
#print(practice)

#problem 2 on tuples
lst_tups=[('Artjcuno','Moltres','Zaptos'),('Beedrill','Metapod','Charizard','Venasaur','Squirtle'),('Oddish','Ploiwag','Diglett','Bellsprout'),('Pontya','Farfetch','Tauros','Dragonite'),('Hoothoot','Chikorita','Lanturn','Flaaffy','Unown','Teddiursa','Phanpy'),('Loudred','Volbeat','Wailord','Seviper','Sealeo')]
t_check=list()
for i in lst_tups:
    t_check.append(i[2])
print(t_check)

print("#####################################################################")
#problem 3 on tuples
tups=[('a','b','c'),(8,7,6,5),('blue','green','yellow','orange','red'),(5.6,9.99,2.5,8.2),('squirrel','chipmunk')]
seconds=list()
for i in tups:
    print(i)
for i in tups:
    seconds.append(i[1])
print("List of tuples containing only the second element:\n",seconds)

#problem 4 on tuples: With only one line of code, assign four variables, v1, v2, v3, and v4, to the following four values: 1, 2, 3, 4. 

(v1,v2,v3,v4)=(1,2,3,4)
print(v1,v2,v3,v4)

print("###########################################")

#problem 5 on tuples:With only one line of code, assign the variables water, fire, electric, and grass to the values “Squirtle”, “Charmander”, “Pikachu”, and “Bulbasaur” 

(water,fire,electric,grass)=('Squirtle','Charmander','Pikachu','Bulbasaur')
print(water)
print(fire)
print(electric)
print(grass)
