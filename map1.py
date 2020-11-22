#program 1:Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” to the beginning of each element using mapping. lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya'] 

lst_check=['plums','watermelon','kiwi','strawberries','blueberries','peaches','apples','mangoes','papaya']

def fun(x):
    return 'Fruit:{}'.format(x)
join=map(fun,lst_check)
print(join)
print(list(join))
