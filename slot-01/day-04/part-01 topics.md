# slot 01 | day 04

## Factor problems

### print all the factors

```python
# using while loop
n = int(input())

i = 1
while i<=n:
  if n%i == 0:
    print(i)
  i = i+ 1
```

```python
# using for loop
n = int(input())
for i in range(1,n+1):
    if n%i == 0:
      print(i)
```

### prime numbers

```python
n = int(input())

i = 2
while i<n:
   if n%i == 0:
      print("not a prime number")
      break
   i = i + 1
else:
    print("it is a prime number")
```

```python
# check if a prime no, effectiantly

n = int(input("Enter a number: "))

if n < 2:
    print("not a prime number")
else:
    i = 2
    while i <= int(n**0.5):  # Only go up to the square root of n
        if n % i == 0:
            print("not a prime number")
            break
        i += 1
    else:
        print("it is a prime number")
```

- print all n prime numbers

```python
n = int(input("Enter a number: "))

print("Prime numbers up to", n, "are:")

for num in range(2, n + 1):  # Starting from 2, as 0 and 1 are not prime
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # Check up to the square root of num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

```

#### Explanation

1. **Outer Loop**: The outer `for` loop iterates through each number (`num`) from `2` up to `n`.
2. **Inner Loop**: For each `num`, the inner `for` loop checks divisibility from `2` up to the square root of `num`. If `num` is divisible by any `i`, it's not a prime number, and we set `is_prime` to `False` and exit the inner loop.
3. **Printing Primes**: If `is_prime` remains `True` after the inner loop, `num` is prime and is printed.

This code efficiently finds and prints all prime numbers up to `n`.

### Number crunching problems

#### Number of digits

```python
n = int(input())

count = 0
while n!=0:
  n = n//10
  count = count + 1
print(count)
```

### Sum of digits

```python
n = int(input())

total = 0
while n!=0:
  digit = digit % 10
  n = n//10
  total = total + digit
print(total)
```

### Reverse number

```python
n = int(input())

rev = 0
while n!=0:
  digit = n%10
  n = n//10
  rev = rev*10 + digit
print(rev)
```

### Adam number

```python
# Input
n = int(input("Enter a number: "))

# Step 1: Calculate the square of the original number
original_square = n * n

# Step 2: Reverse the original number
rev = 0
temp = n
while temp != 0:
    digit = temp % 10
    temp = temp // 10
    rev = rev * 10 + digit

# Step 3: Calculate the square of the reversed number
reversed_square = rev * rev

# Step 4: Reverse the square of the reversed number
rev_of_reversed_square = 0
temp = reversed_square
while temp != 0:
    digit = temp % 10
    temp = temp // 10
    rev_of_reversed_square = rev_of_reversed_square * 10 + digit

# Step 5: Check if the square of the original number is equal to the reversed square of the reversed number
if original_square == rev_of_reversed_square:
    print("Is an Adam number.")
else:
    print("Is not an Adam number.")

```

- Pattern problems
  - Simple star patterns
  - [pattern printing](https://github.com/avicreationstudio/python-problem-solving/blob/main/Python-coding-problems/pattern-printing/pattern-01.md)
  - Simple number patterns
  - [patterns](https://github.com/avicreationstudio/python-problem-solving/blob/main/Python-coding-problems/pattern-printing/pattern-02.md)
