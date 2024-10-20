# slot-01 |  day-01

## all topics that are going to be covered

- Computer introduction
- Language introduction
- Introduction to IDLE
- Difference between Compiler &
interpreter
- Assignment operator intro
- Walrus operator
- print function
- Arithmetic operator
- Data types
  - integer

---

#### `computer introduction`

💡 what is computer ?

    computer is a computing device.

💡 why it is called as computer ?

    As computer are mainly build for computing purpose, Hence it is called as computer.
    💭 who is father of computer ? charles babage. 
    Why he is called as father of computer ? because he is the one who invented first working computer which will do math calculation.

## computer 
- A computer is an electronic device
- It operates under the control of instructions.

## Functionalities of computer:
- takes data as input
- stores the data/instructions in its memory and use them when required.
- process the data and converts it into useful information
- generates the output

## computer componenets:
- Every computers consists of hardware and software.
  
## hardware
- computer hardware is the collection of physical elements that builds a computer system.
- Computer hardware refers to the physical elements that builds a computer system.
- computer hardware refers to the physical parts or components of a computer such as the monitor, mouse, keyboard, computer data storage, hard drive disk ( HDD), system unit(graphic cards, sound cards, memory, motherboard and chips ). and lot more. All of which are physical objects that can be touched.

## input devices
- input devices are essential for interacting with a computer allowing us to input data commands and other information.
- input device translate data from that human understand to one that the computer can work with most common are keyboard and mouse.
- Example for input devices are : keyboard, mouse, joystick, microphone, numeric keyboard, camera, webcame.

## Output devices
- output devices are essential for conveying information from the computer to the user.
- output devices converts the electronically generated information into human readable form.
- Example of output devices are: CRT monitor, Speakers, Printers, projector.
  

#### `Language introduction`

- 🏷️ Python is an interpreter language.
- 🏷️ Python is a high-level, general-purpose programming language.
- 🏷️ Its design philosophy emphasizes code readability with the use of significant indentation.
- 🏷️ Python is dynamically typed and garbage-collected.
- 🏷️ It supports multiple programming paradigms, including structured, object-oriented and functional programming.

#### `Introduction to IDLE`

- IDLE - Integrated Development and Learning Environment

#### `Difference between Compiler & interpreter`

- A teacher and student example 💭
- A teacher ask to write an essay about "AIM IN LIFE"
- After completing the essay, He gave his an essay to teacher for correction.
- The teacher say a mistake in first line, Hence student went and corrected the mistake.
- After correction, again ...
- So the point is executing line by line is interpreter.
- First check for all error then executing is compiler.

#### `Assignment operator intro`

- assignment operator in python.
- Here `=` is not about assigning value to a variable. It is actually reference.
- In python there is no concept called pointer.

```python
a = 123
b = 123
print(id(a)) #  140714564323576
print(id(b)) #  140714564323576
```

#### `Walrus operator`

- walrus operator ( := )
- assign and pass value at the same time.
- which is possible in other languages like ( c, cpp, java )
- But in python as there is a concept called keyword arguments, It is not possible.

```python
a = 0
if a:
    print("true block")
else:
    print("false block")
```

```python
a = 0
if a:=1:
    print("true block")
else:
    print("false block")
```

another use case

```python
def fn(x):
  print(x)

fn(a:=100)
print(a) # 100
```

---

#### `input and print function`

##### `Input`

###### Formats that can be asked in problem solving

###### basic single values

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

---

### `Print`

```python

# print(*args, sep=' ', end='\n')
#     
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

NOTE: Below code will remove last `,`

```python
li = [1,2,3,4]
n = len(li)
for i in range(n):
    if i!=n-1:
       print(li[i],end=",")
    else:
       print(li[i],end="")
#  1,2,3,4
```

`print` flush example ( out of scope )

```python
# sep:   string inserted between values, default a space.
# end:   string appended after the last value, default a newline.
# file:  a file-like object (stream); defaults to the current sys.stdout.
# flush: whether to forcibly flush the stream.
```

```python
# flush example
# --------------------------------------------
# example 1
import time

i = 0
while i<5:
    print(i)
    time.sleep(1)
# output
# The output will be like print each i value
# with a 1 second delay.
# --------------------------------------------
# example 2
import time

i = 0
while i<5:
    print(i,end=" ")
    time.sleep(1)
# output
# The output will be like print each i value
# side by side. But It will show the output 
# only after 5 second
# REASON : that is because by default flush=False,
#   - Which means first it will store all character that should be 
#     printing in a single line.
#   - Then it will flush all the values to output screen

# To make our code run with following scenario
# we have to pass flush=True

i = 0
while i<5:
    print(i,end=" ",flush=True)
    time.sleep(1)
# output will be same but different behavior
```

print `file` ( out of scope )

```python
# by default python will print output in output screen.
# But instead you can print the output in other streams like in files.
fs = open('output.txt','w')
print('hello world!', file=fs)
print('sample text', file=fs)
print('End of the code', file=fs)
# Now output will be saved in a file. Instead of output screen.
```

#### `Arithmetic operator`

### operators and data types

#### operators precedence and associativity

|precedence  |    operator  |associativity  |
|-------|---------|---------|
|1      |     ()    |      L-R   |
|2      |    x[index], x[index:index]     | L-R        |
|3      |   **      | R-L         |
|4      |     +x, -x, ~x     ( bitwise )    | R-L         |
|5      |   *, /, //, %      |      L-R    |
|6      |   +,-      |          L-R|
|7      |    <<,>>     |         L-R |
|8      |      (bitwise and)   |     L-R     |
|9      |      (bitwise xor)   | L-R         |
|10     |      (bitwise or)   |     L-R     |
|11     |    in, not in, is, is not, <, <=, >, >=, !=, ==     |  L-R       |
|12     |  not       |     R-L     |
|13     |     and    |      L-R    |
|14     |       or  |      L-R    |
|15     |   if else ( conditional expression )      |    R-L     |
|16     |   :=      |R-L         |  

##### list of operators

- =
  - a,b = 1,2
- arithmetic operator
- unary +, unary - : it is called unary +, - because it has only one operand.
- +,- ( addition and subtraction )
- *, / ( divition ), // ( floor division ), % ( modulus )
  - `2+3+5`
  - `2+3*5`
- **

###### `most use cases of modulus`

- get remaining values
  - in 100 seconds , we can say 1 minutes and remaining  40 seconds there.
  - how to get this 40 remaining seconds.
  - `100//60` -> 1
  - `100%60`  -> 40
- get last digit

```python
>>> 1234 % 10  # 4
>>> 1234 // 10 # 123
>>> 123 % 10   # 3
>>> 123 // 10  # 12
>>> 12 % 10    # 2
```

- repeat an index value within its limit

```python
>>> li = [ 10, 20, 30 ]
>>> n = len(li) # 3
>>> i = 0
>>> li[ i%n ] # 0%3
>>> i = i + 1
>>> li[ i%n ] # 1%3
>>> i = i + 1
>>> li[ i%n ] # 2%3
>>> i = i + 1
>>> li[ i%n ] # 3%3
>>> i = i + 1
>>> li[ i%n ] # 4%3
>>> i = i + 1
```

---
🙀 EXTRA : 🙀 out of scope

```python
>>> a = 5%2 # 
>>> a = -5%2 # 
>>> a = 5%-2 # 
>>> a = -5%-2 # 
```

`🏷️ will be covered at end of class`

---

### `Exponent operator ( ** )`

- usage is purely on maths.
- find square root and cube root

```python
>>> 2**3   #
>>> 2**1   #
>>> 2**-1  #
>>> 2**0.5 # 
```

```python
# other examples
>>> 4**2
>>> 5*4**2
>>> -3**2
>>> (-3)**2
>>> 4**0.5
>>> 4**-0.5
>>> 4**-2

```

`usage`

- square root
- cube root
  - math.ceil
  - math.floor

---
🙀 EXTRA : 🙀 out of scope

```python
>>>  -3**2
```

- why in python we use # for comments
- why not `//` for comments

`🏷️ will be covered at end of class`

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

- Numeric type basics is enough for problem solving

---

`ADDITIONAL NOTES`

##### REPL

REPL stands for Read-Eval-Print Loop. It is an interactive programming environment that takes user inputs (one at a time), evaluates them, and returns the result to the user. This process is repeated in a loop, hence the name "Read-Eval-Print Loop."

---
