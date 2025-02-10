"""
#Simple Function
Define and call a simple function greet_user which takes name 
as a parameter. The function should print 'Hello, name' to 
the console.
"""

def greet_user (name):
    print(f"hello, {name}")

print(" ")
greet_user("ana")
print("-"*15)

"""
#Default and Keyword Arguments
Update the greet_user function by adding a default value 
'Guest' for the name parameter. When the function is called 
without an argument it should print 'Hello, Guest' to the 
console.
"""

def greet_user(name="Guest"):
    print(f"hello, {name}")

greet_user()
greet_user("john")
print("-"*15)

"""
#Function with Return Values
Write a function that calculates and returns the area of a 
rectangle. The function should take length and breadth as the 
arguments.
"""

def calculate(lenght, breadth):
    return lenght*breadth

space=calculate(2,2)
print(f"the calculus of the area is: {space}")
print("-"*15)

"""
#Variable Scope
To understand the difference between local and global variables, follow these steps:
1. Define a global variable and print its value.
2. Write a function and assign a new value to the same varible inside the function and then print it.
3. Print the variable again outside the function again to observe that its value didn't change.
4. Write another function that access the global variable using the global keyword and then update its value.
5. Print the variable again outside the function. Verify that it's value now got updated.
"""
GlobalVariable=10
print(f"GlobalVariable before the function call: {GlobalVariable}")

def AnotherGlobalVariable():
    GlobalVariable=20
    print(f"Global Variable inside the function: {GlobalVariable}")


AnotherGlobalVariable()

print(f"Global Variable after the function call: {GlobalVariable}")

def AnotherGlobalVariable2():
    global GlobalVariable #declare that we want to use the GlobalVariable
    GlobalVariable=30 #update the GlobalVariable inside the function
    print(f"Globalvariable updated inside the function: {GlobalVariable}")


AnotherGlobalVariable2()

print(f"Global Variable after the update function call: {GlobalVariable}")

