#program 1:Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each. l1 = ['left', 'up', 'front']
#l2 = ['right', 'down', 'back'] 

l1=['left','up','front']
l2=['right','down','back']
l3=list(zip(l1,l2))
print(l3)


#USING LIST COMPREHENSIONS
#new_lst=[(i,y) for (i,y) in l3 if len(i)>3 and len(y)>3]
#print(new_lst)

# USING FILTER FUNCTION
opposites=list(filter(lambda x:len(x[0])>3 and len(x[1])>3,l3))
new_lst=list()
for i in opposites:
    new_lst.append(i)

print(new_lst)
