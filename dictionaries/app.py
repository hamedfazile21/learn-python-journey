profile = {"name" : "Hamed" , "sex" : "male" , "age" : 20 }
print(profile)


# access with key

print(profile['name'])

# add a key with value
profile["faivorate_colors"] = ['red' , 'yellow' , 'black']

print(profile)

# delete a key

del(profile["faivorate_colors"])

print(profile)

# check if any key exist or not

print("job" in profile) # False
print("sex" in profile) # True


# list keys and value
print(profile.keys())
print(profile.values())
