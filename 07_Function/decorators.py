#! Decorators:
#  (A decorator is a function that adds extra functionality to another function without changing its actual code.)

def decorators(func):
    def wrapper():
        print("Before Function")
        result = func()
        print("After Function")
        return result
    return wrapper
@decorators
def greet():
    print( "Say Hello")
greet()
    

def inner(func):
    def outer():
        print("*" * 10)
        res = func()
        print("*" * 10)
        return res
    return outer

def inner2(func):
    def outer2():
        print("*" * 10)
        res = func()
        print("*" * 10)
        return res
    return outer2

@inner
@inner2
def dec():
    print("Hassan")
dec()    

#! Real World Example
def login_required(func):
    def wrapper(user):
        if not user.get("is_logged_in"):
            return "Access Denied!"
        return func(user)
    return wrapper

@login_required
def dashboard(user):
    return f"Welcome {user['name']}!"

user1 = {"name": "Hassan", "is_logged_in": True}
user2 = {"name": "Ali", "is_logged_in": False}
print(dashboard(user1))  # Output: Welcome Hassan!
print(dashboard(user2))  # Output: Access Denied!

