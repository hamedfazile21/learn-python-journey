
## =============================== Tuples ========================

chart = (32,32,21,34,221,2,1111,2)
print(chart)


## print(type(chart))


tup = ('Hamed' , 18 , False , 85.9)
print(tup)



## the index access is the same with string


## concatenating
tup1 = ("Hamed")
tup2 = ("Mahsa")

tup1 = tup2 + ("Hamed")
print(tup1)

## sliceing
print(tup[0:3])


## length
print(len(chart))


## immutable
rate = (10,4,9,8,3,2,1,5,6,7)
rate2 = rate
## sort fun
sort_rate = sorted(rate)
print(sort_rate)


## nesting tuples
nest = (("hamed" , "mahsa" , "mahmood" , "maryam") , (19 , 18 , 24 , 21))
print(nest)

## access with index
print(tup[0] , tup[1:3])

## nest index access
print(nest[0][1])

## =============================== List ========================

nums = [5,3,2,7,6,8,9,10,1]


## the difference between the list and tuple : lists are mutable but tuples are not
## You can:
## - Change an existing element.
nums[0] = 4

## - Add new elements.
nums.append(10)

# - Remove elements.
nums.remove(10)
nums.pop(1) # removing with index

# I know that we just can command a line with one # not tow of them :)

print(nums)

