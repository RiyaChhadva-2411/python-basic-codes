str_1=input("Enter the first string:\n")
first_dict=dict()
for i in str_1:
    first_dict[i]=first_dict.get(i,0)+1
print("First dictionary:\n",first_dict)

str_2=input("Enter the second string:\n")
second_dict=dict()
for i in str_2:
    second_dict[i]=second_dict.get(i,0)+1
print("Second dictionary:\n",second_dict)

new_dict=first_dict.copy()
new_dict.update(second_dict)
print("The modified dictionary is:\n",new_dict)
