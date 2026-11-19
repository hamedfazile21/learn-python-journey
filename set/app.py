
# set can not containes dublicate value
first_set = {"hamed" , "mahmood" , "mozamel" , "modaser" , "boshra"}
second_set = {"osaid" , "boshra" , "onais" , 'sohail'}
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

print("mhasa" in first_set) # False if not exist True if exsit

# comper two set
# take only item that exsit in both set
third_set = first_set & second_set

print(third_set , "===============================================")

# take all items but not dublicate
both_item = first_set.union(second_set)

print(both_item)

# take items that is located in both
# if the second_set items all exsit in the first_set it will return True otherwise return False
both = second_set.issubset(first_set)
print(both)


#  Find the difference in set1 but not set2
print(first_set.difference(second_set))


print(first_set.intersection(second_set))
