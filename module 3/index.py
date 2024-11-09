#Create a set using curly braskets


#my_set = {1,2,3}

#print(my_set)

#Creating a set from a list using the set () function
#my_set = {[4,5,6]}
#print(my_set)
#Create an empty set using teh set() function
#my_set = set()
#print(my_set)

my_set = {1,1,2,2,3,3,4,4,5,4,5}
print(my_set) #Set will a automaticlly remove duplicates

############

set1 = {1,2,3}
set2 = {3,4,5}

#Union between aet1 and set2 using the union() metgod

union_method = set1.union(set2)

#Compute an union between set1 and set2 using the | operator

union_operator = set1 | set2

print("Union of set1 and set2 using method:", union_method)
print("Union of set1 and set2 using operator ", union_operator)

#Compute interesection between set1 and set2 using the intersection() method

intersection_method = set1.intersection(set2)

#Compute interesection between set1 and set2 using using & operator

intersection_operator = set1 & set2

print("Interescetion of set1 and set2 using the interection method" , intersection_method)
print("Interescetion of set1 and set2 using the interection operator" , intersection_operator)

#Computing the elements that are unique to set1 using the diffrence method
diffrence_method = set1.difference(set2)

#Computing elements that are unique to set using - operator

print("Diffrence of set1 and set2 using the diffrence method:", diffrence_method)
print("Diffrence of set1 and set2 using the diffrence operator", diffrence_operator)

symmetric_diffrence_method = set1.symmetric_difference(set2)

print("Symmetric difference of set1 and set2 using the symmetric diffrence method: ", symmetric_diffrence_method)
print("Symmetric difference of set1 and set2 using the symmetric diffrence operator:" , symmetric_diffrence_operator)

#SET METHODS

#Create a set

my_set = {1,2,3}

#Add number 7 at the end of the set

my_set.add(7) #add method

#Remove number 3 from the set without throwing and error if 8 in snow on the set

my_set.discard(8)
print(my_set)

#Remove all teh numbers from the set
my_set.clear()
print(my_set)

#Remove duplications from a list

#Create a list that contains duplications

my_list = [1,2,2,2,3,3,4,4,4,5,6]

#convert this list to a set to remove duplications
uniqe_set = set(my_list)

print(uniqe_set)

#convert this set to a list
unique_list = list(uniqe_set)
print(uniqe_set)

#checking for common elements

blertas_intrets = {"music", "movies", "travling"}










