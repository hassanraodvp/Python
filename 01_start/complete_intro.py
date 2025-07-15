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