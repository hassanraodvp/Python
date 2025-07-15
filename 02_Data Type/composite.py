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