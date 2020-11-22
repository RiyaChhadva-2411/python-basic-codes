#program 4:

#USING LAMBDA FUNCTION
#countries=['Canada','Mexico','Brazil','Chile','Denmark','Botswana','Spain','Britain','Portugal','Russia','Thailand','Bangladesh','Nigeria','Argentina','Belarus','Laos','Australia','Panama','Egypt','Morocco','Switzerland','Belgium']

#names=filter((lambda x:"B" in x),countries)

#for i in names:
#    print(i)

#USING NORMAL FUNCTION
countries=['Canada','Mexico','Brazil','Chile','Denmark','Botswana','Spain','Britain','Portugal','Russia','Thailand','Bangladesh','Nigeria','Argentina','Belarus','Laos','Australia','Panama','Egypt','Morocco','Switzerland','Belgium']

def fun(x):
    if "B" in x:
        return True
    else:
        return False

names=filter(fun,countries)
for i in names:
    print(i)

#USING ZIP FUNCTION AND LIST COMPREHENSION AT A TIME
species=['golden retriever','white tailed deer','black rhino','brown squirrel','field mouse','orangutan','sumatran elephant','rainbow trout','black bear','blue whale','water moccasin','giant panda','green turtle','blue jay','japanese beetle']
population=[10000,90000,1000,2000000,500000,500,1200,8000,12000,2300,7500,100,1800,9500,125000]

pop_info=list(zip(species,population))
print(pop_info)
print("\n")
endangered=[names for names,values in pop_info if values<2500]
print(endangered)
