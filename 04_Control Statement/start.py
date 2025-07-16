#! Types of control statements 
#! 1. Conditional Statements (Decision-making): 
#    a. if statement
#    c. if-elif-else statement
#    b. if-else statement

# * Program 
input_1 = float(input("Enter the first number: "))
input_2 = float(input("Enter the second number: "))

choice = input("Enter the choice: '+', '-', '*', '/', '%': " )

if choice == '+':
    print(f"Addition of -- {input_1} -- & -- {input_2} -- is:  {input_1+input_2}")
elif choice == '-':
    print(f"Subtraction of -- {input_1} -- & -- {input_2} -- is: {input_1-input_2}")
elif choice == '*':
    print(f"Multiplication of -- {input_1} -- & -- {input_2} -- is:  {input_1*input_2}")
elif choice == '/':
    print(f"Division of -- {input_1} -- & -- {input_2} -- is:  {input_1/input_2}")
elif choice == '%':
    print(f"Modulus of -- {input_1} -- & -- {input_2} -- is:  {input_1%input_2}")
else:
    print("Invalid choice")

#! 2. Looping Statements (Repetition):
#    a. for loop
#    b. while loop

# * Program 

i = 5 
while i <= 5:
    print(i)
    i += 1

#! 3. Loop Control Statements:
#  Break Statements
#  Continue Statements
#  Pass Statement
 
#! 4. Nested Statements:
# * Program
start = int(input("Enter the start num: "))
end = int(input("Enter the End num: "))
skip = int(input("Enter the num you want to skip: "))

if start < end:
    print("Invalid Input")
else:
    for i in range(start, end):
        if i == skip:
            continue
        print(i)    