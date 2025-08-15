#! 1. Tuple creations 

#! Empty tuple
t1 = ()
# Tuple with values
t2 = (1, 2, 3)
# Tuple with mixed data types
t3 = (1, "hello", 3.5, True)
# Without parentheses (still tuple)
t4 = 1, 2, 3
# Single element tuple (comma is must)
t5 = (5,)
# Nested tuple
t6 = (1, (2, 3), [4, 5])

#! 2. Accessing Tuple Items
t = (10, 20, 30, 40)
# Indexing
print(t[1])      # 20
# Negative indexing
print(t[-1])     # 40
# Slicing
print(t[1:3])    # (20, 30)

#! 3. Tuple Methods 
#!  Method         ----   Description                                ----   Example                    
#  `count(value)`  ----  Counts how many times a value appears       ----  `(1,2,3,2).count(2)` → `2` 
#  `index(value)`  ----  Returns index of first occurrence of value  ----  `(1,2,3).index(2)` → `1`   

# ✔️ Note: Only 2 built-in methods are available because tuples are immutable. 

#! 4. Tuple Operation 
t1 = (1, 2)
t2 = (3, 4)

# Concatenation
print(t1 + t2)           # (1, 2, 3, 4)

# Repetition
print(t1 * 2)            # (1, 2, 1, 2)

# Membership
print(2 in t1)           # True

# Length
print(len(t1))           # 2

# Max / Min / Sum (if all elements are numbers)
print(max((1, 5, 3)))    # 5
print(min((1, 5, 3)))    # 1
print(sum((1, 2, 3)))    # 6

