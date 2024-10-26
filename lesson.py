#Declaring a variable



temperature = 22.0

name = "Ylli"

print(type(temperature))
print(type(name))

age = 17

x = 5
y = 8

result = x+y

print(result)

#update value
age = age + 1
print(age)

#combine values

first_name = "Yll"
last_name = "Berisha"

full_name = first_name + " " + last_name
print(full_name)

#Linsts

name_of_the_list = ["item1" , "item2", "item3"]

#example od the list

shooping_list = ["apples", "milk", "bread", 3 ,4 ,5]

print(shooping_list)

#Indeksimi

homework = ["math","psikologji","anglisht"]
print(homework[0])
print(homework[3])
print(homework[1])

to_do_list = ["teach 11D", "Go shopping", "create the app", "check devops"]
first_item =to_do_list[0]
second_item = to_do_list[1]
third_item = to_do_list[2]

favorite_subject = ["psikologji", "soiologji", "ed fizike", "frengjisht"]
forth_subject = favorite_subject[3]
print(forth_subject)

#Adding Data to do list we do so by using the append() method
shooping_list.append("strawberries")

print(shopping_list)

shooping_list.insert(2,"lemons")
print(shooping_list)

#remove() methods help us remove item from teh list

to_do_list.remove("check devops")
print(to_do_list)

del to_do_list [2]
print(to_do_list)

#updeting data, you can change the value of an item by assinging a new value to an index
to_do_list[0] = "teach 10"

print(to_do_list)

