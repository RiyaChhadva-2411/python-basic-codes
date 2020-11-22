#program 3:Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. Using list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater). students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
students=[('Tommy',95),('Linda',63),('Carl',70),('Bob',100),('Raymond',50),('Sue',75)]

for k,v in students:
    print(k,v)

lst=[names for names,values in students if values>=70]
print("The new list is:",lst)

print("****************************************************")

#program 4:Use list comprehension to create a list called lst2 that doubles each element in the list, lst. lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4] 
lst=[["hi","bye"],"hello","goodbye",[9,2],4]

lst2=[i*2 for i in lst]
print(lst2)
print("********************************************************************")
#program 5:people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')] show only first names using list comprihension 

people=[('Snow','Jon'),('Lannister','Cersei'),('Stark','Arya'),('Stark','Robb'),('Lannister','Jamie'),('Targaryen','Daenerys'),('Stark','Sansa'),('Tyrell','Margaery'),('Stark','Eddard'),('Lannister','Tyrion'),('Baratheon','Joffrey'),('Bolton','Ramsey'),('Baelish','Peter')]

first=[i[1] for i in people]
print(first)
