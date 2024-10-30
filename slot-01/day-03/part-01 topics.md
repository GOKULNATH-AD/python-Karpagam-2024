# SLOT-01 | day-03

## `multiplication`

Rules

    1.    if a,b is numbers -> multiplication
    Below are when repetition happens to string (string)
    2.    a -> str             , b -> (int,bool)
    3.    a -> (int, bool)m      b -> str
    #  eg: 'hello'*3
    gives output as 'hellohellohello'

```python
a = "hello"
b = 3
a*b # 'hellohellohello'
b*a # 'hellohellohello'

>>> a = "hi"
>>> a*2
hihi

>>> a = "hi"
>>> a * 2 * 2
"hihi"*2
"hihihihi"
>>> 2 * a * 2
"hihihihi"
>>> 2 * 2 * a
"hihihihi"
```

```python
# edge cases
>>> a = 'hello'
>>> a * -1
''
>>> a * 0
''
>>> a * True
'hello'
>>> a * False
''
>>> a * 3.5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
```

## `logical operators`

- `and`
- `or`
- `not`

---

`and`

    arg1 and arg2
    * arg1 is non-zero then result is arg2
    * arg1 is 0 then result is arg1

```python
# example
>>> 5 and 10
10
>>> 100 and 0
0
>>> True and False
False
>>> 3.75 and 6.42
6.42
>>> 0 and 100
0
>>> 0 and 0
0
>>> "hello" and "hai"
'hai'
>>> False and True
False
>>> False and False
False
>>> " " and "hai"
'hai'
```

---

`or`

    arg1 or arg2
    * arg1 is non-zero then result is arg1
    * arg1 is 0 then result is arg2

```python
>>> 10 or 5
10
>>> 7 or 0
7
>>> 6.5 or -5
6.5
>>> False or 100
100
>>> False or False
False
>>> 0 or 2.5
2.5
```

- In case of `and` 1st is `0` don't go next.
- In case of `or` 1st is non-zero then don't go for next.

---

`not`

```python
# not True -> False
# not False -> True
# not non-zero => False
# not zero -> True
# not 10 -> False
# not 3.5 -> False
# not False -> True

# in below code, 
# == has high priority
# but 10==not is invalid.
>>> a = 10 == not 100
  File "<stdin>", line 1
    a = 10 == not 100
              ^^^
SyntaxError: invalid syntax

>>> 10 != (not 100)
True
>>> not 10 == 0
True
>>> not 100 and 20
False
>>> 10 and not 20
False
>>> 0 and not 100
0
# last scenario, as first it is zero.
# python will not check further.
```

---

```python
# mostly we use logical operators 
# - to compare multiple conditions like
a = 10
b = 20
c = 30
if not ( a>b and b>=c or a==c ):
   print('condition satisfied')
```

```python
>>> 10 and 20 and 0 and 100 and 200
0
>>> 10 and 20 and [] and 20 and (1,2)
[]

# in above cases. It will convert each and every thing into its boolean type then evaluates. Once it stop evaluation it will through the ans. 
# 10 -> bool(10)  -> True
# 20 -> bool(20)  -> True
# [] -> bool([])  -> False
# 20 -> bool(20)  -> True

# As we are using only `and`. Python will stop once it gets 
# False ( bool([]) -> False ).
# so only we got output as `[]`
```

---

## type of errors

|syntax error  |Runtime error  |
|---------|---------|
|No output at all     |   runs some code, stop where ever there is a problem     |

- python script is executed from top to bottom, ( controlling is also possible )
- python will follow a rule called indentation
- every statement should be under a indentation
- default indentation is main indentation

```python
# indentation error
print("A")
   print("B") # this will come under "main indentation"
# indentation error comes under syntax error, so no output.
```

```python
a = 10 # we mentioned to python that, we are going to use a.
print(a + b) # error, because, b is not yet defined.
# we didn't told to python, that we are using "b"
```

---

## `Flow control`

### if

```python
print("A")        # main indentation/block
print("B")        # main indentation/block
if True:          # main indentation/block
    print("C")        # IF indentation/block
    print("D")        # IF indentation/block
print("E")        # main indentation/block
print("F")        # main indentation/block
```

#### if syntax

- if keyword followed by condition,
- where condition can be an valid expression, or variable or anything
- that can be converted to boolean.
- Python finally checked if it is True or False.
  - if is True. then executes IF block
  - if is False. then executes ELSE Block

```python
# some invalid indentation codes.

# code 01
print(10)
if (3>2):
    print(20)
  print(30) # this will not comes under either main/if block.
print(40)

# code 02
print(10)
if (3>2):
   print(20)
      print(30) # this will not comes under either main/if block.
print(40)

# code 03
print(10)
if (3>2): # expected an indented block after 'if' statement
print(20)
print(30) 
print(40)
```

some if code scenario's

```python
# code 01
print(10)
if (3>2):
    pass # this is used, when you don't want to write a code now. 
    # but you will write in future.
    # pass will do nothing. 
print(20)
print(30)
print(40)

# code 02
print(10)
if (): # empty brackets are always valid, 
    # is consider False, 
    # Because it means, empty tuple.
    print(20)
print(30)

# code 03
print(10)
if :# End up with syntax error. 
    # Because, bracket is mandatory
    print(20)
print(30)
```

---

### else

```python
# WAP to find max of 2 numbers
a = int(input())
b = int(input())
if a > b:
    res = a 
else:
    res = b
print(res)

# alternate solution
a = int(input())
b = int(input())
res = (a>b)*a + (b>a)*b
print(res)
```

```python
# some valid indentation codes.

# code 01
print(10)
if (3>2):
    print(20)    # this will comes under if block
    print(25)
else:
          print(26)
          print(30) # this will not comes under either else block.
print(40)

# 💡In python switch concept is not there.💡 
# But later match is introduced...
# But now we can use elf for doing switch logic.
key = input() # W A S D
if key == "W":
    print("move forward")
elif key=="S":
    print("move backward")
elif key == "A":
    print("move left")
elif key == "D":
    print("move right")
else: # it is optional to write else here.
    print("invalid key")
```

---

### while

```python
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1 

col = 5
row = 5
c = 1
while col <= 5: # outer while 
    r = 1
    while r <= r-c: # inner while
         print(b, end=" ")
         b = b + 1
    print()
    a = a + 1
    
```

---

### for

In Python, a `for` loop allows you to repeat a block of code a specific number of times. When using `range()`, you can control how many times the loop will run.

#### Syntax

```python
for variable in range(start, stop, step):
    # code to repeat
```

- **`start`** (optional): The number where the loop starts (default is 0).
- **`stop`** (required): The number where the loop stops. This is not included in the loop.
- **`step`** (optional): The amount the loop counter increases by after each iteration (default is 1).

##### Example 1: Basic Loop with `range(stop)`

```python
for i in range(5):
    print(i)
```

**Explanation**:

- The loop starts at `0` and ends at `4` (since `5` is not included).
- Output:

  ```
  0
  1
  2
  3
  4
  ```

##### Example 2: Loop with `range(start, stop)`

```python
for i in range(2, 6):
    print(i)
```

**Explanation**:

- The loop starts at `2` and ends at `5` (because `6` is not included).
- Output:

  ```
  2
  3
  4
  5
  ```

##### Example 3: Loop with `range(start, stop, step)`

```python
for i in range(0, 10, 2):
    print(i)
```

**Explanation**:

- The loop starts at `0`, ends at `8` (since `10` is not included), and increments by `2` each time.
- Output:

  ```
  0
  2
  4
  6
  8
  ```

##### Example 4: Loop in Reverse with `range()`

```python
for i in range(5, 0, -1):
    print(i)
```

**Explanation**:

- The loop starts at `5`, ends at `1`, and decreases by `1` each time.
- Output:

  ```
  5
  4
  3
  2
  1
  ```

---

---

### break

- break keyword will only work inside
- the for, while ( loops )

```python
# some other examples
a = 1
while a <=10:
    print(a)
    if a == 4:
        break
    a = a + 1

# some other examples
# example - 01
a = 1
while a <=10:
    print(a)
    if a == 4:
        break
    a = a + 1
else:
    print("loop completed") 

# example - 02
a = 1
while a <=10:
    print(a)
    a = a + 1
else:
    print("loop completed") 
```

```python
# find prime no
n = int(input())
i = 2
isPrime = True
while i<(n**0.5):
    if n%i == 0:
        isPrime = False
        break
    i = i + 1

if isPrime:
    print("is Prime")
else:
    print("is not a Prime")

# find prime no
n = int(input())
i = 2
while i<(n**0.5):
    if n%i == 0:
        print("Not a prime")
        break
    i = i + 1
else:
    print("is a Prime")

# NOTE: If break executed, then else not get executed.


```

---

### continue

- continue keyword will only work inside
- the for, while ( loops )

diff `continue` and `break` in Python:

| **Concept**   | **`break`**                                 | **`continue`**                            |
|---------------|---------------------------------------------|-------------------------------------------|
| **Purpose**   | Exits the loop entirely.                    | Skips the current iteration and moves to the next. |
| **Effect**    | Terminates the loop when executed.          | Skips the remaining code in the current iteration, but the loop continues. |
| **When to use**| When you want to stop the loop early.       | When you want to skip certain iterations but continue looping. |
| **Example use**| Exiting a loop when a condition is met.     | Skipping an iteration based on a condition. |

#### Example using `continue` and `break` together

```python
for i in range(10):
    if i == 3:
        continue  # Skip when i is 3
    if i == 8:
        break  # Exit the loop when i is 8
    print(i)
```

**Explanation**:

- The loop prints numbers from `0` to `9`.
- When `i` is `3`, `continue` skips the rest of the code for that iteration, so `3` is not printed.
- When `i` is `8`, `break` terminates the loop, so `8` and anything beyond it are not printed.

**Output**:

```
0
1
2
4
5
6
7
```

---

---

### pass

    In Python, the `pass` statement is a placeholder that does nothing. It’s used when a statement is syntactically required but you don’t want to execute any code. Typically, you use `pass` in situations where you plan to add code later or you want to skip a block without causing errors.

#### Common Uses of `pass`

1. **Empty Function or Class**: You can use `pass` when you want to define a function or class but aren’t ready to implement the logic yet.
2. **Placeholders in Conditional Statements**: Sometimes in `if`, `for`, or `while` statements, you may want to skip certain conditions temporarily.

#### Example 1: `pass` in Conditional Statements

```python
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    else:
        print(i)
```

**Output**:

```
0
1
2
4
```

In this example, when `i` is `3`, the `pass` statement is executed, meaning the loop does nothing for that iteration, but continues with the next.

---

### conditional operator

- is a concept used, literally a short form of if else
- Technically we can call it as "conditional expression"
- But it act as an expression

```python
a = int(input())
b = int(input())
res = a if a > b else b
print(res)

# syntax 
#   a            if         a > b        else           b
#  [True res] [if keyword] [ condition] [else keyword] [False res]
# to put in simple terms.
# res1 if exp else res2

    
```
