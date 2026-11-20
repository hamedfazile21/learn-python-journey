# ====================== For loops =====================

list_var = ["Hamed", "Mahmood" , "mahsa" , "jamal" , "Other one"]

rng = range(len(list_var))
# print(rng)

# for i in rng:
#     print("Hello" , " ", i)
#

for i in list_var:
    print(i)


for key, value in enumerate(list_var):
    print(key , value)

for item in reversed(list_var):
    print(item , "--------------")
# ========================== while loops ==================
a=0
while(a<=5):
    print(a , ":" ,"a")
    a=a+1


i=10

while(i>=0):
    print(i , ":" , "i")
    i=i-1
