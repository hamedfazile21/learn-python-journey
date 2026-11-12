name = "Hamed Fazeli"
print(name[0])

## select last char of the string
print(name[-1])

## select a range from the string
print(name[0:5])

## select the adds chart
print(name[::2])

## select from 6 chart up to the end of string
print(name[6:])

## slice the array from 0 up to the 5 and select the chars with 1
print(name[0:5:1])

## check the length
print(len(name))

## concatenate the strings
concatenate = name + " " + "I am frm AF"

print(concatenate)


## tuples
tuples  = 3 * (name + " ")
print(tuples)

## \n send the chars into new line 
print("My Name is \n Hamed")

## \t it means tab
print("Ali is a \t good man")

## but if we want to add a backslash in over string what we should do ??!! :( . do not wory duble backslashes and r is hear are hear \\
print("Check for backslash \\ is it works ??")
print(r"Check for backslash \ is it works ??")


## interpolation (f-strings)
age = 30
print(f"My Name is {name} and I am {age}")


## str.format()
print('My Name is {} and I am {} years old'.format(name , age))

## % operator
## %s is a placeholder for a string
## %d is a placeholder for interger
print('My name is %s and I am %d years old.' % (name , age))

## =====================> method ===================>

## uppercase
nameB = name.upper()
print(nameB)

## replace
nameC = name.replace("Hamed" , "Mahsa")
print(nameC)

## find
## if does not exist the output is -1
nameD = name.find('Fazeli')
print(nameD)

## split
split_name = name.split()
print(split_name , "Goooooood")


## strip
messy = "###@@@ Python Programming@@##"
print(messy.strip("#@"))

## RegEx
import re

s1 = "My English is the best with 1 Level :)"

result = re.search('best' , s1)

print(result.group())  # best
print(result.start())  # 18
print(result.end())    # 22
print(result.span())   # (18, 22)

## Special Sequence
pattern = r"\d"  # Matches any ten consecutive digits`
result_number = re.search(pattern , s1)
print(result_number.span())


patternB = r"\w\w\w\w\w\w\w\w\w\w\w"
result_symbol = re.split(patternB , messy)
print(result_symbol , "check")

## \d	Matches any digit character (0-9)	"123" matches "\d\d\d"
## \D	Matches any non-digit character	"hello" matches "\D\D\D\D\D"
## \w	Matches any word character (a-z, A-Z, 0-9, and _)	"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"
## \W	Matches any non-word character	"@#$%" matches "\W\W\W\W"
## \s	Matches any whitespace character (space, tab, newline, etc.)	"hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"
## \S	Matches any non-whitespace character	"hello_world" matches "\S\S\S\S\S\S\S\S\S\S\S"
## \b	Matches the boundary between a word character and a non-word character	"cat" matches "\bcat\b" in "The cat sat on the mat"
## \B	Matches any position that is not a word boundary	"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"
