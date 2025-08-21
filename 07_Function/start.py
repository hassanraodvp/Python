# Function? ==> (Function is block of code, ek reusable code block jo kaam ko organize, simple aur fast banata hai.)

#! Why we use Funtion in py? 
# Reusability → ek dafa likho, bar bar use karo.
# Readability → code samajhna easy ho jata hai.
# Maintenance → changes karna easy ho jata hai.

#* Examples 
# simple function
def greet():
    print("Hello, Welcome to Python!")
greet() # function call

#* Function with parameters (input) 
def greet_user(name):
    print(f"Hello {name}, Welcome to Python!")
greet_user("Hassan") # OutPut: Hello Hassan, Welcome to Python!
greet_user("Ali") # OutPut: Hello Ali, Welcome to Python!

#* Function with return (output wapas bhejna)
def add(a, b):
    return a + b
result = add(5, 3)
print("Result:", result) # Result: 8
