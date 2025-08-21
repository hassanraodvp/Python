#! 1. Generators 
# 👉 Generators special functions hote hain jo ek sequence of values ko ek-ek karke produce (generate) karte hain instead of returning all values at once.

# 2. Difference Between return vs yield 
#! Return
def normal_func():
    return [1, 2, 3]
print(normal_func()) # Output: [1, 2, 3]
#! Yield 
def gen_func():
    yield 1
    yield 2
    yield 3
print(gen_func())       # ye ek generator object banata hai
for val in gen_func():  # values ek-ek karke milengi
    print(val)
# Output: 1
# Output: 2
# Output: 3

#! 4. Why use Generators? 
# Memory Efficient → ek waqt mai ek hi value hold hoti hai (big data mai useful).
# Lazy Evaluation → value tabhi generate hoti hai jab zarurat ho.
# Readable Iterators → loops mai easy to use.

def read_file(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

for line in read_file(r"C:\Users\hassan-akhtyr\OneDrive\Desktop\Python\07_Function\data.txt"):
    print(line)





