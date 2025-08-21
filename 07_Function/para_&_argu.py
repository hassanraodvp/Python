def add(a , b): #! here a & b is parameters
    print(f"Addition of {a} and {b} is {a+b}")
add(5 , 8) #! here 5 & 8 are arguments

#! Types of function Arguments
# 1: Positional Arguments (Order important hota hai, jo value pehle doge wo pehle parameter mai jayegi.)
def known(name , age):
    print(f"Name is {name} and age is {age}")
known("Hassan Akhtyr", 28)  # ✅ This is right 

def known1(name , age):
    print(f"Name is {name} and age is {age}")
known1( 28 ,"Hassan Akhtyr")  # ❌ This is wrong 

# 2: Keyword Arguments (Order important hota hai, jo value pehle doge wo pehle parameter mai jayegi.)
def student_info(name, age):
    print(f"Name is: {name}, Age: {age}")
student_info(age=22, name="Hassan")   # order change kiya

# 3: default Arguments (Agar user value na de to default value use ho jati hai.)
def student_info2(name, age=18):
    print(f"Name: {name}, Age: {age}")
student_info2("Hassan")       # age default 18 le lega
student_info2("Ali", 25)      # custom value de di
