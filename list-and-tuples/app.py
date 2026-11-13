

chart = (32,32,21,34,221,2,1111,2)
print(chart)


## print(type(chart))


tup = ('Hamed' , 18 , False , 85.9)
print(tup)


## access with index
print(tup[0] , chart[3:5])


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
