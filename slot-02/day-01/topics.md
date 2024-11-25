# slot-02 | day-01

## string methods

Here’s a concise guide to Python string methods, ideal for beginners:

---

### **Python String Methods**

#### **String Basics**

- **Strings**: A sequence of characters enclosed in single (`'`) or double (`"`) quotes.
- **Indexing**: Strings are indexed, starting from `0`.

  ```python
  s = "Python"
  print(s[0])  # Output: P
  print(s[-1]) # Output: n
  ```

- **Immutability**: Strings cannot be changed after they are created.

---

### **String Methods**

#### **1. Case Conversion**

- **`lower()`**: Converts all characters to lowercase.

  ```python
  s = "Hello"
  print(s.lower())  # Output: hello
  ```

- **`upper()`**: Converts all characters to uppercase.

  ```python
  print(s.upper())  # Output: HELLO
  ```

- **`capitalize()`**: Capitalizes the first letter.

  ```python
  print(s.capitalize())  # Output: Hello
  ```

- **`title()`**: Capitalizes the first letter of each word.

  ```python
  print("hello world".title())  # Output: Hello World
  ```

- **`swapcase()`**: Swaps case for all letters.

  ```python
  print("HeLLo".swapcase())  # Output: hEllO
  ```

- **`istitle()`**: Check if it is in title case

  ```python
  print("HeLLo".istitle())  # Output: True
  print("Hello world".istitle())  # Output: False
  print("Hello World".istitle())  # Output: True
  print("Hello World ".istitle())  # Output: True
  print("   Hello World".istitle())  # Output: True
  ```

- **`isupper()`**: Check if it is in title case

  ```python
    print("HeLLo".isupper())  # Output: false
    print("HeLLo world".isupper())  # Output: false
    print("HeLLo WORLD".isupper())  # Output: false
    print("HELLO".isupper())  # Output: true
    print("HELLO WORLD".isupper())  # Output: true
    print("   HELLO WORLD".isupper())  # Output: true
  ```

- **`casefold()`**: Return a version of the string suitable for caseless comparisons.

```python
print("Hello world") # hello world
gmail = "Byts@GMAIL.com"
if gmail.casefold() == "byts@gmail.com":
    print("valid email")
```

---

#### **2. String Searching**

- **`find(substring)`**: Returns the index of the first occurrence of a substring. Returns `-1` if not found.

  ```python
  print("hello".find("e"))  # Output: 1
  ```

- **`rfind(substring)`**: Returns the index of the last occurrence of a substring.

  ```python
  print("hello".rfind("l"))  # Output: 3
  ```

- **`count(substring)`**: Returns the number of times a substring appears.

  ```python
  print("hello".count("l"))  # Output: 2
  ```

---

#### **3. String Manipulation**

- **`strip()`**: Removes leading and trailing spaces.

  ```python
  print("  hello  ".strip())  # Output: hello
  ```

- **`lstrip()`**: Removes leading spaces.

  ```python
  print("  hello".lstrip())  # Output: hello
  ```

- **`rstrip()`**: Removes trailing spaces.

  ```python
  print("hello  ".rstrip())  # Output: hello
  ```

- **`replace(old, new)`**: Replaces occurrences of `old` with `new`.

  ```python
  print("hello".replace("l", "p"))  # Output: heppo
  ```

---

#### **4. String Testing**

- **`startswith(substring)`**: Checks if a string starts with a substring.

  ```python
  print("hello".startswith("he"))  # Output: True
  ```

- **`endswith(substring)`**: Checks if a string ends with a substring.

  ```python
  print("hello".endswith("lo"))  # Output: True
  ```

- **`isalpha()`**: Returns `True` if all characters are alphabetic.

  ```python
  print("hello".isalpha())  # Output: True
  ```

- **`isalnum()`**: Returns `True` if all characters are alphanumeric.

  ```python
  print("hello123".isalnum())  # Output: True
  ```

- **`isspace()`**: Returns `True` if all characters are whitespace.

  ```python
  print("   ".isspace())  # Output: True
  ```

---

##### `isdigit()` vs `isnumeric()` vs `isdecimal()`

Here’s a clear comparison of Python's `isdigit()`, `isnumeric()`, and `isdecimal()` string methods presented in a table:

| **Feature**        | **`isdigit()`**                                     | **`isnumeric()`**                                  | **`isdecimal()`**                                 |
|---------------------|----------------------------------------------------|--------------------------------------------------|--------------------------------------------------|
| **Description**    | Checks if all characters in the string are digits. | Checks if all characters are numeric characters. | Checks if all characters are decimal characters. |
| **Supports**       | Digits (0–9) and Unicode digit characters.         | All digit characters + numeric symbols (e.g., fractions). | Only decimal characters (0–9).                  |
| **Excludes**       | Decimal points, fractions, Roman numerals, etc.    | Non-numeric characters like Roman numerals, letters, etc. | Non-decimal numerics (e.g., fractions, superscripts). |
| **Examples**       | `"123".isdigit()` → `True`<br>`"⅔".isdigit()` → `False` | `"123".isnumeric()` → `True`<br>`"⅔".isnumeric()` → `True` | `"123".isdecimal()` → `True`<br>`"⅔".isdecimal()` → `False` |

---

### **Detailed Explanation with Examples**

#### **1. `isdigit()`**

- **Definition**: Checks if all characters are digits (0–9 or Unicode digits).
- **Examples**:

  ```python
  print("123".isdigit())      # True
  print("²³".isdigit())       # True (superscripts are digits)
  print("⅔".isdigit())        # False (fraction is not considered a digit)
  ```

#### **2. `isnumeric()`**

- **Definition**: Checks if all characters are numeric (digits or other numeric representations like fractions).
- **Examples**:

  ```python
  print("123".isnumeric())    # True
  print("⅔".isnumeric())      # True (fraction is numeric)
  print("Ⅷ".isnumeric())      # False (Roman numeral is not numeric)
  ```

#### **3. `isdecimal()`**

- **Definition**: Checks if all characters are decimal (strictly 0–9).
- **Examples**:

  ```python
  print("123".isdecimal())    # True
  print("²³".isdecimal())     # False (superscripts are not decimal)
  print("⅔".isdecimal())      # False (fraction is not decimal)
  ```

---

### **Quick Summary**

Use:

- **`isdecimal()`** for strict decimal digit checks.
- **`isdigit()`** for broader digit checks (including superscripts).
- **`isnumeric()`** for the most inclusive numeric checks (including fractions).


### A Correct Example Where Only `isdigit()` Returns `True`
If you want a case where `isdigit()` returns `True`, but both `isnumeric()` and `isdecimal()` return `False`, **there are none.** All characters where `isdigit()` is `True` are either `numeric` or `decimal`.

---

### Example Clarification
If you're looking for differences among the three methods, here’s a practical demonstration:

```python
examples = ["²", "⅓", "10", "5.5", "3", "abc"]

for char in examples:
    print(f"Character: '{char}'")
    print(f"  isdigit(): {char.isdigit()}")
    print(f"  isnumeric(): {char.isnumeric()}")
    print(f"  isdecimal(): {char.isdecimal()}")
    print()
```

### Output Explanation:
| Character | `isdigit()` | `isnumeric()` | `isdecimal()` | Explanation                              |
|-----------|-------------|---------------|---------------|------------------------------------------|
| `"²"`     | `True`      | `True`        | `False`       | Superscript 2 is numeric, not decimal.  |
| `"⅓"`     | `False`     | `True`        | `False`       | Fraction is numeric but not a digit.    |
| `"10"`    | `True`      | `True`        | `True`        | A regular number passes all checks.     |
| `"5.5"`   | `False`     | `False`       | `False`       | Float numbers don't pass any checks.    |
| `"3"`     | `True`      | `True`        | `True`        | A single digit passes all checks.       |
| `"abc"`   | `False`     | `False`       | `False`       | Letters fail all numeric checks.        |

For superscripts like `"²"`, both `isdigit()` and `isnumeric()` return `True`, but `isdecimal()` does not.

#### **5. Splitting and Joining**

- **`split(separator)`**: Splits the string into a list based on the `separator`.

  ```python
  print("a,b,c".split(","))  # Output: ['a', 'b', 'c']
  ```

- **`join(iterable)`**: Joins elements of an iterable into a single string with the specified separator.

  ```python
  print("-".join(["a", "b", "c"]))  # Output: a-b-c
  ```

---

#### **6. Formatting**

- **`format()`**: Inserts values into placeholders `{}`.

  ```python
  print("Hello, {}".format("World"))  # Output: Hello, World
  ```

- **`f-strings`**: A modern way to format strings (Python 3.6+).

  ```python
  name = "Alice"
  print(f"Hello, {name}!")  # Output: Hello, Alice!
  ```

---

#### **7. Other Useful Methods**

- **`len()`**: Returns the length of the string (not a method, but very useful).

  ```python
  print(len("hello"))  # Output: 5
  ```

- **`zfill(width)`**: Pads the string with zeros to the left to reach the specified width.

  ```python
  print("42".zfill(5))  # Output: 00042
  ```

- **`center(width)`**: Centers the string in a field of given width.

  ```python
  print("hello".center(10))  # Output: '  hello   '
  ```

- **`ljust(width)`** / **`rjust(width)`**: Left-aligns or right-aligns the string in a field of given width.

  ```python
  print("hi".ljust(5, "-"))  # Output: hi---
  ```

---

This comprehensive overview should help you and your students get comfortable working with strings in Python!

---
---

## functions

### introduction

- Functions -> pre defined function / user defined funcitons

- Eg of pre defined functions are
  - `print()`
  - `input()`
  - `len()`
  - `chr()`
  - `ord()`

### User defined functions

- To define a function we use `def` keyword

```python
def fun(): # function definition
     print("hello world!")

def main():
     pass

fun() # function call
main() # function call
```

```python
def f2():
    print("I am in function f2")
def f1():
    print("I am in function f1")
    f2()
    print("I am in function f1")

print("calling f2()")
f2()
print("calling f1()")
f1()
print("end of code")
```

---

```python
def add(a,b):
    print("the result is : ",a+b)

add(5,2)
add(5,3.5)
add(2,True)
add("hello","world")
add([10,20,30],[50,60,70])

add(10) # Error
add()
add(10,20,30)
```

# `return` statement

```python
def add(x,y):
    print(x+y)
    return x+y 
res = add(5,8)
print(res) # or print(add(5,8))
```

```python
def fun():
   print("hello")
x = fun()
print(x)

>>> print(print("Hello"))
```

```python
def calc(a,b):
    return a+b,a-b

x,y = calc(5,2)
print(x,y)
```

```python
def calc(a,b):
    return a+b, a-b, a*b, a/b

x,y,z,a = calc(5,2)
t = calc(5,2)
for x in t:
    print(x)
```

### Types of arguments

- positional
- keyword
- default
- variable length

#### `positional`

```python
def sub(a,b):
    print(a-b)
sub(10,5) # 5
sub(5,10) # -5     positional argument
```

#### `keyword`

```python
def fun(name,age):
    print("hello ",name)
    print(age)
fun("karthik",32)
fun(32,"karthik")
# So above based on the position the o/p values
# So to fix age as, name as karthik
# we go for keyword arguments

fun(age=32, name="karthik")
fun(name="karthik",age=32)
fun("karthik",age=32)
fun(age=32,32)

# positional argument followed by keyword arg
# keyword arguments must be at trailing end
# all positional, all keyword
```

```python
def fun(a,b,c):
    print(a,b,c)
fun(10,20,30)
fun(10,c=30,b=20)
fun(10,20,c=30)
fun(c=30,a=10,b=20)
fun(10,20,b=30)
fun(a=10,b=20,30)
```

#### `default` argument

```python
def wish(name="guest"):
    print("Good day",name)
wish("byts")      
wish()            
wish(name="byts") 

# if we, pass, in the fun, def it is called default argument
# if we, pass in the func call it is called keyword argument
```

```python
def wish(msg,name="guest"):
    print(msg,name)
wish("GA","karthik") # GA karthik
wish("GM") # GM Guest
wish(msg="GN",name="Ram") # GN Ram
wish(msg="Good Day") # Good day Guest
wish(msg="GE","karthik") # syntax error: pos arg follows key arguments
wish() # TYpe error
wish(name="sam") # Type error : missing 1 pos arg
```

```python
print(10,20) # default arg sep=" ", end="\n"

print(10,20,sep=",")
print(10,20,30,sep="#",30) # syntax error: pos arg follows keyword arguments
```

#### `variable number of arguments`

- range(10)
- range(10,20)
- range(10,20,2)
- 💡 In python, there is no func overloading,
- 💡 but still we can achieve it using var no of arguments

```python
def fun(*k):
    print(k)
fun() # ()
fun(10) # (10)
fun(10,20) # (10,20)
fun(10,20,30) # (10,20,30)
```

```python
def add(*t):
    res = 0
    for i in t:
        res += i
    return res

result = add()
print(result)

result = add(10)
print(result) # 10

result = add(1,2,3)
print(result) # 6

result = add(10,20)
print(result) # 30
```

```python
def fun(*x):
    print(x)

fun([10,20,30],"Hello",(5,6))
# output: ([10,20,30],"Hello",(5,6))
# tuple contains heterogenous elements.
```

```python
def fun(a,*b):
    print(a,b)

fun()
fun(10)
fun(10,20)
fun(10,20,30)
fun(10,20,30,40)
```

```python
def fun(k=111,*m):
    print(k,m)
fun() # 111 ()
fun(10) # 111 (10)
fun(10,20) # 111 (10,20)
fun(10,20,30) # 111 (10,20,30)
```

- we can write var-args after default arg since var-args accepts 0 args
- But we cannot write non-default args after default args.

```python
def test(a=10,b):
    pass 

def fun(*k, m):
    print(k,m)

fun(10,20,30) # error
# - whenever we are writing non-default arg after var-args
# - Then compulsory we should call with key-word args.

fun(0,m=123) # (0,) 123
fun(10,20,30,40,m=111) # (10,20,30,40) 111
fun(m=25) # () 25
```

- default-arg, var-args ✅
- default-arg, non-default-arg ❌
- non-default arg, var-args ✅
- var-args, non-default-args ✅
- var-args, default-args ✅

```python
def fun(a=111,*b,c):
    print(a,b,c)
fun(10,20,30,40)
fun(10)
fun(10,20,30)
fun()
fun(a=10,20,30,40) # syntax error
fun(10,20,30,40,c=50) # 111 (10,20,30,40) 50
fun(a=10,20,30,c=40) # syntax error
#    ☝️  key arg, must be at the end.
fun(c=25) # 111 ( ) 25
```

```python
def fun(*a):
    print(a)
fun(a=111) # var-args cannot be called with keyword arg
# type error: func got an unexpected keyword arg 'a' 
```

##### summary

```python
def fun(a,b=10): pass        # a is called non-default arg | b is called default-arg
def fun(*c): pass            # c is called var-arg
def fun(x,y): pass           # x,y are positional-arg
def fun(d=20,c=30): pass     # d,e are keyword-arg
```

###### 🏷️ FINAL NOTES 🏷️

- In the `function call`, if we are not using any assignment then they are called `positional argument`.
- In the `function call`, if we are using any assignment then they are called `keyword arguments`
- In the `function definition`, If we using any assignment, then they are called `default arguments`.
- In the `function definition`, we are not using assignment then they are called `non-default argument`.
- In the `function call`, we cannot provide `positional arguments` after `keyword arguments`, if we do not get `💀 syntax error`.
- In the `function definition`, we cannot provide, `non-default arguments` after `default arguments`, if we do we get `💀 syntax error`.
- After default argument, if we want to provide `non-default argument` then compulsory in between there should be a `variable no of argument` and that `non-default argument` must be called by a `keyword arguments only`.
- After `var-args` if we are providing `non-default arg`, then we should call that with `keyword arg only`.
- we cannot invoke `var-args` with `keyword-arg`.
- if we use * in `function definition`, it is called packing.
- if we use * in `function call`, it is called unpacking.

| **Context**                     | **Point**                                                                                                                                                                      | **Explanation**                                                                                                            |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Function Call**                | **Positional Arguments**: No assignment is used.                                                                                                                            | Example: `func(1, 2, 3)` - All arguments are positional.                                                                   |
|                                  | **Keyword Arguments**: Assignment is used.                                                                                                                                  | Example: `func(a=1, b=2)` - Arguments are explicitly named.                                                                |
|                                  | **Positional arguments before keyword arguments**.                                                                                                                          | Example: `func(1, b=2)` is valid. <br> But `func(a=1, 2)` gives a syntax error.                                            |
|                                  | **Cannot invoke variable arguments (`*args`) using keyword arguments**.                                                                                                    | Example: `func(*[1, 2, 3])` is valid for unpacking; `func(args=[1, 2, 3])` is not.                                         |
|                                  | **Unpacking (`*`) in function call**: Used to unpack iterables into positional arguments.                                                                                   | Example: `func(*[1, 2, 3])` unpacks the list into `func(1, 2, 3)`.                                                         |
| **Function Definition**          | **Default Arguments**: Arguments with assignment in the definition.                                                                                                        | Example: `def func(a=10):` - `a` has a default value.                                                                      |
|                                  | **Non-default Arguments**: Arguments without assignment in the definition.                                                                                                 | Example: `def func(a, b):` - Both `a` and `b` are non-default arguments.                                                   |
|                                  | **Non-default arguments cannot appear after default arguments**.                                                                                                          | Example: `def func(a=10, b):` results in a syntax error.                                                                   |
|                                  | **Default arguments followed by non-default arguments**: Requires `*args` (variable-length arguments) between them.                                                        | Example: `def func(a=10, *args, b):` - Here `b` must be called using a keyword argument.                                    |
|                                  | **Variable-length arguments (`*args`) followed by non-default arguments**: Non-default arguments must be called with keyword arguments.                                   | Example: `def func(*args, b):` - `func(1, 2, b=3)` is valid; `func(1, 2, 3)` gives an error.                               |
|                                  | **Packing (`*`) in function definition**: Used to accept variable-length positional arguments.                                                                             | Example: `def func(*args):` - Accepts any number of arguments as a tuple.                                                  |
|                                  | **Unpacking (`*`) in function definition**: Not applicable.                                                                                                               | Unpacking occurs in function calls, not definitions.                                                                       |

---

### **Key Notes**

1. **Packing**:
   - Collects multiple positional arguments into one variable.
   - Example:

     ```python
     def func(*args):  # args is a tuple
         print(args)

     func(1, 2, 3)  # Output: (1, 2, 3)
     ```

2. **Unpacking**:
   - Breaks an iterable into individual arguments during a function call.
   - Example:

     ```python
     def func(a, b, c):
         print(a, b, c)

     values = [1, 2, 3]
     func(*values)  # Output: 1 2 3
     ```

3. **Order Rules**:
   - Positional arguments → `*args` → Default arguments → Keyword arguments → `**kwargs`.
   - Non-default arguments must always come before default arguments unless variable arguments are used.
