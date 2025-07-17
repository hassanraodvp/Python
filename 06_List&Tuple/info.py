# 1. Using [] Brakets
# my_list = [1,2,3,"Hassan", "BWN", 23]

# 2. Using List Constructor
my_list2 = list((1,2,3,"Hassan", "BWN", 23))
print(my_list2)

# 3. List comprehension & Range
my_list3 = [i for i in range(1,11)]
print(my_list3)

# 4. Accessing List Items
list_4 = [1,4,3,8,7,6,2,9]
print(list_4[0])
print(list_4[1])
print(list_4[1:3])
print(list_4[1:]) 
print(list_4[2])
print(list_4[3])
print(list_4[4])
print(list_4[5])

# 5. Mutable
list_5 = [1,4,3,8,7,6,2,9]
list_5[0] = "Hassan"
print(list_5) # OutPut - ['Hassan', 4, 3, 8, 7, 6, 2, 9]

