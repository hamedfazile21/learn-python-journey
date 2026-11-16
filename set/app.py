
# set can not containes dublicate value
first_set = {"hamed" , "mahmood" , "mozamel" , "modaser"}

# type of set
print(type(first_set))
print(first_set)


# conver a list to a set
number = [3,2,4,1,6,5,7,9,8,10]

list_set = set(number)

print(list_set)

# add item to a set

first_set.add('mahsa')

print(first_set)

# remove item from a set

first_set.remove("mahsa")

print(first_set)

# check if any item exsit to a set

print("mhasa" in first_set)
