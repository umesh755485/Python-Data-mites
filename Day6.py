################################################################################
# 📅 DAY: 06 - Python Fundamentals
# ------------------------------------------------------------------------------
# Description:In This It will cover all Python String Methods  
################################################################################

#capitalize()

#The capitalize() method returns a string where the first character is upper case, and the rest is lower case.



## Example

name = "love"

print(name.capitalize())

#out put
 # "Love"

# ------------------------------------------------------------------------------

#Casefold()
#The casefold() is similar to .lower but it is more aggressive that it converts more characters in to lower case

## Example
name = "MY NAME IS UMESH REDDY"
print(name.casefold())

#output
    # "my name is umesh reddy"

# ----------------------------------------------------------------------------


# string center()
#The center() method will center align the string, using a specified character (space is default) as the fill character.

## Example


txt = "banana"

print(txt.center(20, "O"))

#out put

# "OOOOOOObananaOOOOOOO"

# ----------------------------------------------------------------------------

#count() Method

#The count() method returns the number of times a specified value appears in the string.
#In future we can use this ML project like where we use this in a counting a number a people are persons like that

#Example 1

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple",10 , 20)

print(x)

#output
# 01

# ----------------------------------------------------------------------------

# find() Method

# The find() method finds the first occurrence of the specified value.

# The find() method returns -1 if the value is not found.

# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.

#Example

txt = "Hello, welcome to my world."

x = txt.find("e")

print(x)

# output
# 1

# ----------------------------------------------------------------------------

# format_map() Method

# The format_map() method formats the specified values of a dictionary and insert them inside the string's placeholders.

# The format_map() method returns the formatted string.

#Example

myvar = {"name" : "Jane", "age" : 36}
txt = "Happy birthday {name} you are now on level {age}!"
print(txt.format_map(myvar))

#output

#Happy birthday Jane you are now on level 36!

# ----------------------------------------------------------------------------

# index() Method

# The index() method finds the first occurrence of the specified value.

# The index() method raises an exception if the value is not found.

# The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. 

# It count space also and symbols also

#Example

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

#output
#7

# ----------------------------------------------------------------------------
