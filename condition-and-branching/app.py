# ==================== comparison operator ==========

a = 6
b = 6

# return True if a = b and False if not a = b 
print(a==b)

print(a>b)

print(a<=b)

# the js form of the code is !a=b :)
print(a!=b)


# we can also use the above comperison for strings


# ===================== Branching ==================
# age = input("Inter you age: ")
age = 18


if(int(age)>=19):
    print("you can inter")
elif(int(age)==18):
    print("You can inter in another section")
else:
    print("you can not inter")

# =========== logical operator =============

print(not(True))


# or

print(a>=5 or b<=5)


if(a>=5) or (b<=5):
    print("True")
else:
    print("False")


# and

print(a>=5 and b<=5)


if(a>=5) and (b<=5):
    print("True")
else:
    print("False")
    

user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    amount = int(input("Enter the amount to withdraw: "))
    if amount % 10 == 0:
        print("Amount dispensed: ", amount)
    else:
        print("Please enter a multiple of 10.")
else:
    print("Thank you for using the ATM.")




