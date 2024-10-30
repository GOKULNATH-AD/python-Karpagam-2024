# slot-01 |  day-01

---

#### `tamil python learning`

<https://www.youtube.com/watch?v=BVIoAILnZ4Q&list=PLvepBxfiuao1hO1vPOskQ1X4dbjGXF9bm>

#### `why we need math for programming FUN video`

<https://www.youtube.com/watch?v=sW9npZVpiMI>

#### `computer introduction`

💡 what is computer ?

    computer is a computing device.

💡 why it is called as computer ?

    As computer are mainly build for computing purpose, Hence it is called as computer.
    💭 who is father of computer ? charles babage. 
    Why he is called as father of computer ? because he is the one who invented first working computer which will do math calculation.

[Charles babbage first computer](https://www.youtube.com/watch?v=BlbQsKpq3Ak&t=177s)

## 📝 computer

- A computer is an electronic device
- It operates under the control of instructions.

## 📝  Functionalities of computer

- takes data as input
- stores the data/instructions in its memory and use them when required.
- process the data and converts it into useful information
- generates the output

## 📝 computer components

- Every computers consists of hardware and software.
- software example : Photo shop, VSCode etc.
  
## 📝 hardware

- computer hardware is the collection of physical elements that builds a computer system.
- Computer hardware refers to the physical elements that builds a computer system.
- computer hardware refers to the physical parts or components of a computer such as the monitor, mouse, keyboard, computer data storage, hard drive disk ( HDD), system unit(graphic cards, sound cards, memory, motherboard and chips ). and lot more. All of which are physical objects that can be touched.

### 📝 input devices

- input devices are essential for interacting with a computer allowing us to input data commands and other information.
- input device translate data from that human understand to one that the computer can work with most common are keyboard and mouse.
- Example for input devices are : keyboard, mouse, joystick, microphone, numeric keyboard, camera, webcame.

### 📝 Output devices

- output devices are essential for conveying information from the computer to the user.
- output devices converts the electronically generated information into human readable form.
- Example of output devices are: CRT monitor, Speakers, Printers, projector.
  
#### 📝 `Language introduction`

- 🏷️ Python is an interpreter language.
- 🏷️ Python is a high-level, general-purpose programming language.
- 🏷️ Its design philosophy emphasizes code readability with the use of significant indentation.
- 🏷️ Python is dynamically typed and garbage-collected.
- 🏷️ It supports multiple programming paradigms, including structured, object-oriented and functional programming.

## 📝 `Introduction to IDLE`

- IDLE - Integrated Development and Learning Environment

## 📝 `Difference between Compiler & interpreter`

- A teacher and student example 💭
- A teacher ask to write an essay about "AIM IN LIFE"
- After completing the essay, He gave his an essay to teacher for correction.
- The teacher say a mistake in first line, Hence student went and corrected the mistake.
- After correction, again ...
- So the point is executing line by line is interpreter.
- First check for all error then executing is compiler.

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

### 📝 compiler vs interpreter

|compiler  |interpreter  |
|---------|---------|
|c, java is compiler based language     | python is interpreter based language        |
|1st compile fully then execute the code | line by line compile and execute.        |

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

## 📝  `Assignment operator intro`

- assignment operator in python.
- Here `=` is not about assigning value to a variable. It is actually reference.
- In python there is no concept called pointer.

```python
a = 123
b = 123
print(id(a)) #  140714564323576
print(id(b)) #  140714564323576
```

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

## `input and print function`

### `Input`

#### Formats that can be asked in problem solving

##### basic single values

    input: 1
    code: int(input())
    
    input: 12.12
    code: float(input())
    
    input: Hello world
    code: input()

##### multiple values in single line

###### input format

```md
example 1: 1 2 3 4 5
example 2: 12 212 23
example 3: 1.23 2.12 43.3 43.3
example 4: hari jai krish mani   
```

##### `CODE`

```python
# example 1:
# input: 1 2 3 4 5
li = list(map(int,input().split()))
# example 2: 
# input: 12 212 23
li = list(map(int,input().split()))
# example 3: 
# input: 1.23 2.12 43.3 43.3
li = list(map(float,input().split()))
# example 4:
# input: hari jai krish mani   
li = input().split()
```

```python
# input: 12 23 34 53 53
# code example 1
li = list(map(int,input().split()))
# code example 2
li = []
temp = input().split()
for item in temp:
    li.append(int(item))
print(li) # [12, 23, 34, 53, 53]
# code example 3
li = [int(x) for x in input().split()]
print(li) # [12, 23, 34, 53, 53]
```

##### combining n and list items

```md
input: 
5
11 2 23 4 56 6
```

```python
# code example
n = int(input())
li = list(map(int,input().split()))
print(n) # 5
print(li) # [11, 2, 23, 4, 56, 6]
```

##### matrix input example

```md
input:
3 4
11 22 33 44
10 20 30 40
17 17 17 17 
```

```python
# code example
temp = list(map(int,input().split()))
rc = temp[0]
cc = temp[1]
matrix = []
for i in range(rc):
    row = list(map(int,input().split()))
    matrix.append(row)
```

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

### 📝 `Print`

```python
    
# print(*args, sep=' ', end='\n')
#     *args
#       which means you can pass any number of values.
#     sep
#       string inserted between values, default a space.
#     end
#       string appended after the last value, default a newline.
#     
```

example 1

```python
li = ['samsung', 'iphone','nokia','oppo','vivo']
print(*li,sep=" and ")
# samsung and iphone and nokia and oppo and vivo 
```

example 2

```python
li = [1,2,3,4]
n = len(li)
for i in range(n):
   print(li[i],end=",")
#  1,2,3,4,
```

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

### 📝 operators and data types

#### 📝  operators precedence and associativity

|precedence  |    operator  |associativity  |
|-------|---------|---------|
|1      |   ()    |      L-R   |
|2      |   x[index], x[index:index]     | L-R        |
|3      |   **      | R-L         |
|4      |   +x, -x, ~x     ( bitwise )    | R-L         |
|5      |   *, /, //, %      |      L-R    |
|6      |   +,-      |          L-R|
|7      |   <<,>>     |         L-R |
|8      |   (bitwise and)   |     L-R     |
|9      |   (bitwise xor)   | L-R         |
|10     |   (bitwise or)   |     L-R     |
|11     |   in, not in, is, is not, <, <=, >, >=, !=, ==     |  L-R       |
|12     |   not       |     R-L     |
|13     |   and    |      L-R    |
|14     |   or  |      L-R    |
|15     |   if else ( conditional expression )      |    R-L     |
|16     |   =      |R-L         |  

#### `points to be noted from above table`

- The most priority goes to brackets `()`.
- the least priority goes to `=` equal to.
- Most of the operators follows `L->R` approach.
- Where as some operators follows `R->L` and they are.
  - `**`
  - `+x, -x` | unary plus and unary minus
  - logical not  `not` | eg: `print( not not not True )`

##### 📝 list of operators

- =
  - a,b = 1,2
- arithmetic operator `( +, -, *, /, //, % ) and **`
  - unary +, unary - : it is called unary +, - because it has only one operand.
  - +,- ( addition and subtraction )
  - *, / ( division ), // ( floor division ), % ( modulus )
    - `2+3+5`
    - `2+3*5`
  - **

###### 📝 `most use cases of modulus operator`

- get remaining values
  - in 100 seconds , we can say 1 minutes and remaining 40 seconds there.
  - how to get this 40 remaining seconds.
  - `100//60` -> 1   | `gives how many times you can divide 100 by 60`
  - `100%60`  -> 40  | `gives remaining values that will left after dividing 100 by 60`
- get last digit

---

Below example shows how you can remove each digit one by one in a number.

```python
>>> x = 1234
>>> digit = x%10 # digit = 4
>>> x = x//10 # x = 123
>>> digit = x%10 # digit = 3
>>> x = x//10 # x = 12
>>> digit = x%10 # digit = 2
>>> x = x//10 # x = 1
>>> digit = x%10 # digit = 1
>>> x = x//10 # x = 0
>>> # we will do this until the number becomes zero.
```

- repeat an index value within its limit

```python
>>> li = [ 10, 20, 30 ]
>>> n = len(li) # 3
>>> i = 0
>>> li[ i%n ] # 0%3 = 0
>>> i = i + 1
>>> li[ i%n ] # 1%3 = 1
>>> i = i + 1
>>> li[ i%n ] # 2%3 = 2
>>> i = i + 1
>>> li[ i%n ] # 3%3 = 0
>>> i = i + 1
>>> li[ i%n ] # 4%3 = 1
>>> i = i + 1
>>> # 🙀 so we can repeat a number like 012 012 012
```

```python
# A working code for above example.
word = "hello"
n = len(word)
for i in range(20):
    idx = i%n
    char = word[idx]    
    print(char,end="")
# output
# hellohellohellohello
```

---
🙀 EXTRA : 🙀

```python
>>> a = 5%2 # 
>>> a = -5%2 # 
>>> a = 5%-2 # 
>>> a = -5%-2 # 
```

- while using modulus operator, result sign will be same as denominator sign.
- Internally it uses following formula,
- `Divident = divisor * Quotient + reminder`
- to find `Quotient` python uses floor division.

---

#### `Exponent operator ( ** )`

- usage is purely on maths.
- find square root and cube root

```python
>>> 2**3   #
>>> 2**1   #
>>> 2**-1  #
>>> 2**0.5   # square root
>>> 3**(1/3) # cube root
```

```python
# other examples 
# ( try below example to try to find why we got that output )
>>> 4**2    # 16
>>> 5*4**2  # 80
>>> -3**2   # -9
>>> (-3)**2 #  9
>>> 4**0.5  #  2.0
>>> 4**-0.5 # 0.5
>>> 4**-2   # 0.0625
```

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

### Other questions

```python
>>> a = 2 + 3 + 5
>>> # 2 + 3 executes first, as we have see from left to right
>>> # 3 + 5 executes second.

>>> a = 2 + 3 * 5 # 17
>>> # 3*5 executes first as multiplication has more priority.

>>> a = (2+3)*5 # 25
>>> # () will execute first

>>> a = 5/2*3   # 7.5
>>> a = (5/2)*3 # 7.5 same result
>>> # div then multiplication
```

```python
# one of major question on (python3 vs python2)
>>> 5/2
2.5 # in python 3
>>> 5/2
2   # in python 2
```

```python
# below are example of floor division when interacting with int, float
>>> 5//2   # int - int -> int
2
>>> 5.0//2 # int - float -> float
2.0
```
