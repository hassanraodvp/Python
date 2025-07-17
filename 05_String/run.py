s1 = 'Hello'
s2 = "World"
s3 = '''This is
a multiline string'''

#!  2. String Properties
# ✅ Ordered
# ✅ Iterable
# ✅ Immutable
# ✅ Supports indexing and slicing

#! 3. String Indexing and Slicing 
s = "Python"
print(s[0])     # P
print(s[-1])    # n
print(s[0:3])   # Pyt
print(s[::-1])  # nohtyP

# ! 4. String Immutability
# Strings can't be changed after creation. 
s = "Hello"
s[0] = 'h'  # ❌ Error

#! 6. String Methods
#!  Method                                     | Description             -----  Example                         
#  `.lower()`                                 | Lowercase               -----  `'PYTHON'.lower()` → `'python'` 
#  `.upper()`                                 | Uppercase               -----  `'python'.upper()` → `'PYTHON'` 
#  `.title()`                                 | Capitalize each word    -----  `'hello world'.title()`         
#  `.capitalize()`                            | Capitalize first letter -----  `'hello'.capitalize()`          
#  `.strip()`                                 | Removes whitespace      -----  `'  hi  '.strip()`              
#  `.replace(a, b)`                           | Replace `a` with `b`    -----  `'hello'.replace('l', '*')`     
#  `.find(sub)`                               | Returns index           -----  `'apple'.find('p')`             
#  `.count(sub)`                              | Count occurrences       -----  `'banana'.count('a')`           
#  `.split(sep)`                              | Returns list            -----  `'a,b,c'.split(',')`            
#  `.join(iter)`                              | Joins elements          -----  `'-'.join(['a','b']) → 'a-b'`   
#  `.startswith()` / `.endswith()`            | Bool                    -----  `'abc'.startswith('a')`         
#  `.isdigit()` / `.isalpha()` / `.isalnum()` | Check type              -----  `'123'.isdigit()`               

# * Example of these methods:
#! .lower()
# Sab letters ko lowercase bana deta hai
"HELLO".lower()  # 'hello'

#! .upper()
# Sab letters ko uppercase bana deta hai
"hello".upper()  # 'HELLO'

#! .title()
# Har word ka pehla letter capital kr deta hai
"hello world".title()  # 'Hello World'

#! .capitalize()
# Sirf first letter capital, baqi lowercase
"hello world".capitalize()  # 'Hello world'

#!.strip()
# Start/end ka whitespace ya characters hata deta hai
"  hello  ".strip()  # 'hello'

#! .replace(a, b) 
# a ko b se replace karta hai
"hello world".replace("world", "Python")  # 'hello Python'

#! .find(sub)
# Substring ka first index return karta hai (nahi mila to -1)
"hello".find("e")  # 1

#! .count(sub)
# Substring kitni baar aaya, ye batata hai 
"banana".count("a")  # 3

#! .split(sep)
# Separator ke basis pe tod deta hai string ko list mai
"a,b,c".split(",")  # ['a', 'b', 'c']

#! .split(sep)
# Separator ke basis pe tod deta hai string ko list mai
"a,b,c".split(",")  # ['a', 'b', 'c']

#! .join(iter)
# Iterator ke elements ko join kr deta hai
"-".join(["a", "b", "c"])  # 'a-b-c'

#! .startswith() / .endswith()
# Checks if string starts/end with the given substring 
"hello".startswith("h")  # True
"hello".endswith("o")    # True

#! .isdigit() / .isalpha() / .isalnum()
"123".isdigit()  # True
"abc".isalpha()  # True
"123abc".isalnum()  # True


            # ------------ End ----------- 

#!  7. f-Strings (Formatting)
name = "Ali"
age = 25
print(f"My name is {name} and I am {age} years old.")

#!  8. Useful Built-in Functions 
len("hello")        # 5
max("abc")          # 'c'
min("abc")          # 'a'
ord('A')            # 65
chr(65)             # 'A'

