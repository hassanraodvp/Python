# !----- Compiler ------
# Compiler convert the entire program/whole code into machine code before execution. e.g (c, C++, Java) use compiler.

# !----- Interpreter ------
# Interpreter executes the code line by line, one at a time. e.g (Python, Ruby, Perl, JS) use interpreter.

# !------- High Level Languages ----------
# High-level languages are human-readable, abstracted from hardware, and easier to learn/write (e.g., Python, Java, JavaScript).

# !------- Low Level Languages --------- 
# Low-level languages are closer to machine code, offering direct hardware control but requiring complex syntax (e.g., Assembly, C).

# !------- PYTHON? ---------
# Python is a high level, interpreted languages known for its simplicity and readability.

# * Composite Data Type
# !----- List -----
# List data type represents a collection of items. List are in ordered, mutable, and allow duplicate values.
# Examples: [1, 2, 3], ["apple", "banana"], [1, "apple", True]

# !----- Tuple -----
# Tuple data type represents an ordered, immutable (can't change) collection and allow duplicate values.
# Examples: (1, 2, 3), ("apple", "banana"), (1, "apple", True)

# !----- Set -----
# Set data type represents an unordered, mutable collection and no duplicated allowed.
# Examples: {1, 2, 3}, {"apple", "banana"}, {1, "apple", True}

# !----- Dictionary -----
# Dictionary data type represents a collection of key-value pairs.
# Examples: {"name": "John", "age": 30}, {"apple": 1, "banana": 2}


# ! ------ Summary ---------
# Type	        Ordered	        Mutable	            Allows Duplicates	Index Access	Key-Value Pairs
# List	        ✅ Yes	        ✅ Yes	            ✅ Yes	           ✅ Yes	       ❌ No
# Tuple	        ✅ Yes	        ❌ No	            ✅ Yes	           ✅ Yes	       ❌ No
# Set	        ❌ No	        ✅ Yes	            ❌ No	           ❌ No	           ❌ No
# Dict	        ✅ Yes*	        ✅ Yes	            ❌ No (Keys)	       ❌ No	           ✅ Yes

# * Primitive Data Type
# ! ------ int ------
# Integer data type represents whole numbers.
# Examples: 10, -5, 0

# ! ------ float ------
# Float data type represents decimal numbers.
# Examples: 3.14, -2.5, 0.0

# ! ------ str ------
# String data type represents a sequence of characters.
# Examples: "Hello", '123', "!@#"

# ! ------ bool ------
# Boolean data type represents a truth value.
# Examples: True, False

# !----- 1. Arithmetic Operators -------
#! Operator --------   Description       ------    Example  ------   Output
# `+`      --------   Addition          ------    `5 + 3`  ------    `8`   
# `-`      --------   Subtraction       ------    `5 - 3`  ------    `2`   
# `*`      --------   Multiplication    ------    `5 * 3`  ------    `15`  
# `/`      --------   Division          ------    `5 / 2`  ------    `2.5` 
# `//`     --------   Floor Division    ------    `5 // 2` ------    `2`   
# `%`      --------   Modulus           ------    `5 % 2`  ------    `1`   
# `**`     --------   Exponentiation    ------    `2 ** 3` ------    `8`   

#! ------- 2. Assignment Operators ---------
#! ------------     Operator     ----------       Example           ---------          Meaning      
# ------------     `=`          ----------       `x = 5`           ---------          Assign value 
# ------------     `+=`         ----------       `x += 3`          ---------          `x = x + 3`  
# ------------     `-=`         ----------       `x -= 2`          ---------          `x = x - 2`  
# ------------     `*=`         ----------       `x *= 2`          ---------          `x = x * 2`  
# ------------     `/=`         ----------       `x /= 2`          ---------          `x = x / 2`  
# ------------     `//=`        ----------       `x //= 2`         ---------          `x = x // 2` 
# ------------     `%=`         ----------       `x %= 2`          ---------          `x = x % 2`  
# ------------     `**=`        ----------       `x **= 2`         ---------          `x = x ** 2` 

#! ------ 3. Comparison (Relational) Operators ------
#!  -----  Operator  -----  Description            -----  Example     -----    Output  
#  -----  `==`      -----  Equal to               -----  `5 == 5`    -----    `True`  
#  -----  `!=`      -----  Not equal to           -----  `5 != 3`    -----    `True`  
#  -----  `>`       -----  Greater than           -----  `5 > 3`     -----    `True`  
#  -----  `<`       -----  Less than              -----  `5 < 3`     -----    `False` 
#  -----  `>=`      -----  Greater than or equal  -----  `5 >= 5`    -----    `True`  
#  -----  `<=`      -----  Less than or equal     -----  `3 <= 5`    -----    `True`

#! ----- 4. Logical Operators ------
#!  ------  Operator  ------  Description            ------  Example            ------  Output  
#  ------  `and`     ------  True if both are true  ------  `5 > 3 and 4 < 6`  ------  `True`  
#  ------  `or`      ------  True if one is true    ------  `5 > 3 or 4 > 10`  ------  `True`  
#  ------  `not`     ------  Inverts the condition  ------  `not(5 > 3)`       ------  `False` 

#! ----- 5. Identity Operators -----
#! Operator  ------  Description              ------  Example       ------  Output       
#  `is`      ------  True if same object      ------  `a is b`      ------  `True/False` 
#  `is not`  ------  True if not same object  ------  `a is not b`  ------  `True/False` 

#! 6. ----- Membership Operators ------
#!  Operator  -----  Description           ------  Example               -----  Output 
#  `in`      -----  True if value exists  ------  `3 in [1, 2, 3]`      -----  `True` 
#  `not in`  -----  True if not exists    ------  `5 not in [1, 2, 3]`  -----  `True` 

#! 7.  ----- Bitwise Operators -----
#!  Operator  ------   Description           ------   Example   -----   Result 
#  `&`       ------     AND                   ------  `5 & 3`   -----     `1`    
#  \`        ------     \`                    ------    OR      -----     \`5    
#  `^`       ------     XOR                   ------  `5 ^ 3`   -----     `6`    
#  `~`       ------     NOT (1’s complement)  ------  `~5`      -----     `-6`   
#  `<<`      ------     Left shift            ------  `5 << 1`  -----     `10`   
#  `>>`      ------     Right shift           ------  `5 >> 1`  -----     `2`    

#! sort() & sorted()
# * Sort  
# Ye original list ko hi change kar deta hai.
# Koi nayi list return nahi karta.
a = [3, 1, 2]
a.sort()
print(a)   # Output: [1, 2, 3]

# * Sorted
# Ye nayi sorted list banata hai.
# Original list waise ki waise rehti hai.
a = [3, 1, 2]
b = sorted(a)
print(a)   # Output: [3, 1, 2]
print(b)   # Output: [1, 2, 3]

#! Break - Continue - Pass 
# * Break
# Loop ko foran rok deta hai.
for i in range(5):
    if i == 3:
        break
    print(i) # output -- 0 1 2

# * Continue
# Current iteration skip karta hai, next pe chala jata hai.
for i in range(5):
    if i == 3:
        continue
    print(i) # output 0 1 2 4 ( skip 3 )

# * pass   
# Kuch nahi karta — placeholder hota hai. yai bas program ko bugs se bachany kay liay hota hai. ham program likhty hain or pass likh dety hain, in future program mai kuch changes yai program ko jab complete krty hain to isy hata dety hain.
for i in range(5):
    pass

#! String Concept

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
# ------- End ---------

#! List 
#!  Method          Purpose                                        Example                              Output
#  `append(x)`     End mein item add karta hai              `lst = [1, 2]; lst.append(3)`            `[1, 2, 3]`

#  `insert(i, x)`  Index `i` par item insert karta hai      `lst = [1, 3]; lst.insert(1, 2)`         `[1, 2, 3]`

#  `remove(x)`     Pehli baar jo `x` mile usay remove kare  `lst = [1, 2, 2]; lst.remove(2)`         `[1, 2]`

#  `pop(i)`        Index `i` se item remove + return karta  `lst = [1, 2, 3]; lst.pop(1)`            `2`, list: `[1, 3]`

#  `sort()`        List ko ascending order mein sort karta  `lst = [3, 1, 2]; lst.sort()`            `[1, 2, 3]` 

#  `reverse()`     List ko ulta (reverse) karta hai         `lst = [1, 2, 3]; lst.reverse()`         `[3, 2, 1]`

#  `index(x)`      `x` ki pehli position return karta hai   `lst = ['a', 'b', 'a']; lst.index('a')`  `0` 

#  `count(x)`      `x` kitni dafa aya, woh count karta hai  `lst = [1, 2, 2, 3]; lst.count(2)`       `2` 

#  `extend(iter)`  List mein multiple items add karta hai   `lst = [1]; lst.extend([2, 3])`          `[1, 2, 3]`

#  `clear()`       Saari list empty (clear) karta hai       `lst = [1, 2]; lst.clear()`              `[]`

#  `copy()`        List ka ek copy banata hai               `new = lst.copy()`                    `new` same as `lst` |
