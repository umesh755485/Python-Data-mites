# Python-Data-mites

# 1. Defining a function
def greet_user(name):
    """This function greets the person passed in as a parameter"""
    return f"Hello, {name}! Welcome to the repo."

# 2. Calling the function
# Functions don't run until they are called
message = greet_user("Developer")

# 3. Using the result
print(message) 

# 4. Avoiding repetition: We can call it as many times as we want!
print(greet_user("Alice"))
print(greet_user("Bob"))
