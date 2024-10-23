# slot-01 | day-02

---

### `comment`

- where to use, Consider a scenario where you don't want to execute a line of codes.
- The developers uses comments that will restrict the execution of such code.
- Some times, developers use comments to explain below codes.

```python
a = 10 # a is assigned with value 10
b = 20
# In below code 
# - we are doing addition operation
# - and storing in variable c
c = a + b
print(c)
```

- why in python we use # for comments
- why not `//` for comments | in c, cpp, java, javascript we use `//` for comments
- because already `//` has been used for `floor division`

---

### `Data types`

```md
     Data types
       /      \
  Numberic    string datatype
  /                \
int               str
float
bool
complex     
```

#### `int`

1. +ve, =ve, 0 are called `int`
1. size/range is dependent on machine

```python
# some times you want to store money information in code
amount = 1,00,000 # 1 lakh
print(amount) # (1,0,0)

# you can make above code readable by using underscore.
amount = 1_00_000
print(amount) # 100000
# 💡NOTES:
# - only point is use underscore(_) in-between the digits
# - not in front or rear of digits.
```

- you can represent binary, octal, hexadecimal in integer

```python
# you can use both small and capital letters ( b, B, x, X, o, O )
a = 0b1010 # (or) 0B1010
print(a) # 10
b = 0o10 # (or) 0O10
print(b) # 8
c = 0xA  # (or) 0XA
print(c) # 10
```

#### `float`

- float will follow double precision
- float data will only follow "decimal representation"
- `0b10.10` is wrong becase, here this is meaning less,
  - and in python you can use 0b, 0B, 0x, 0X, 0o, 0O in integer type only.
- `1e3` mean `1*10**3`, 1 multiple of 10 to power of 3

```python
# rare examples
# below is actually type conversion
>>> float("inf") 
inf
>>> float("-inf")
-inf
>>> float("-inf") * 10
-inf
>>> float("nan")
nan
>>> float("infinity")
inf

# in python we can represent infinite like this.
```

#### `complex`

- This is all about complex numbers which comes under subject `math`
- examples of valid complex numbers
  - `5+3j`
  - `5-3j`
  - `3j`
  - `5+3J`
  - `3.5+3J`
  - `3.5+6J`
  - `0b1010 + 21j`
  - `0x13 + 0x13J`

```python
a = 7 + 9j
print(a.real) # 7.0
print(a.imag) # 9.0
```

```python
v1 = 4 + 5j
v2 = 6 + 3j
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / v2)
print(v1 // v2) # ERROR 💀. can use // in complex 
```

#### `strings`

- in python there is no data type like 'char' ( character )
- Because in c, cpp we have a data type called 'char'
- In python we can create/represent string in following ways.
  - single quotes `'`
  - double quotes `"`
  - triple quotes
    - 3 single quotes `'''`
    - 3 double quotes `"""`

```python
# valid ways to create a string in python
a = 'h'
a = "h"
a = "hello"
a = "" # empty string
a = " " # a single space in string
a = '''line 1
line 2
line 3
line 4
''' # we use triple quotes to store string in that can 
# be written in multiple lines
a = "don't" # outside - " and inside - '
a = 'I will never "give up"' # outside - ' and inside - "
a = 'hai\nhello\twhat\'\"\\' # these are escape sequences
```

---

`ADDITIONAL NOTES`

##### REPL

REPL stands for Read-Eval-Print Loop. It is an interactive programming environment that takes user inputs (one at a time), evaluates them, and returns the result to the user. This process is repeated in a loop, hence the name "Read-Eval-Print Loop."

### `comparison operators`

#### types

- Equality
- Relational
- Membership
- Identity

---

- `==` Equal To
- `!=` Not Equal To
- `>` Greater Than
- `<` Less Than
- `>=` Greater Than or Equal To
- `<=`  Lesser Than or Equal To
- `in` # checks if given item in sequence
- `not in` # checks if given item not in sequence
- `is` # check if left content `id` is same as right `id`
- `is not` # check if left content `id` is not same as right `id`
- `NOTE :` # we cannot do comparison on complex types.

##### `Lexicographical comparison`

```python
# this means, you can compare strings in python
# How this is working ? 🤔 
# - It will compare each characters ASCII value
print( 'abc' == 'abc' ) # True
print( 'abc' == 'bbc' ) # False
print( 'abc' <= 'bbc' ) # True
```

### MUTABLE AND IMMUTABLE

- Immutable Objects are of in-built datatypes like int, bool, string, Unicode, and tuple. In simple words, an immutable object can’t be changed after it is created.
- Mutable Objects are of type Python list, Python dict, or Python set. Custom classes are generally mutable.

|`is`  |`===`  |
|---------|---------|
|Meant for reference comparison    | Meant for content comparison         |
|It is used to check both references (or) pointing to same object or not    | It is used to check both the content or value is same or not         |

```python
# for int
# only following range will have same id by default
# range : -5 to 256
>>> a = 10
>>> b = 10
>>> a == b
True
>>> a is b
True
>>> id(a), id(b)
(140730277624536, 140730277624536)
----------------------------------------
>>> a = 10.12
>>> b = 10.12
>>> a == b
True
>>> a is b
False
>>> id(a), id(b)
(1184823356912, 1184823356336)
----------------------------------------
>>> a = 10.12
>>> b = a
>>> a == b
True
>>> a is b
True
>>> id(a)
3215396023792
>>> id(b)
3215396023792
```

### others ( `x+y` )

- case 1 :
  - if x,y is number ->
