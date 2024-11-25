# slot-02 | day-01

    1. Write a code to segregate the number into odd
      digits first even digits next
      Sample input: 34582014
      Sample output: 35148204
    
```python
def segregate_odd_even(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Initialize empty strings for odd and even digits
    odd_digits = ""
    even_digits = ""
    
    # Iterate through each digit in the string
    for digit in num_str:
        # Check if the digit is odd or even
        if int(digit) % 2 != 0:
            odd_digits += digit  # Append to odd_digits
        else:
            even_digits += digit  # Append to even_digits
    
    # Concatenate odd and even digits
    result = odd_digits + even_digits
    return result

# Sample input
input_number = 34582014
output = segregate_odd_even(input_number)
print(f"Input: {input_number}")
print(f"Output: {output}")
```

---

    2. Write a code to check whether the number is
        strong number or not
        Sample input: 145
        Sample output: Yes
[Strong Numbers | Practice | GeeksforGeeks
](https://www.geeksforgeeks.org/problems/strong-numbers3315/1)

```python
def factorial(n):
    # Calculate the factorial of n without inbuilt functions
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_strong_number(number):
    # Convert the number to a string for digit-by-digit processing
    num_str = str(number)
    
    # Initialize the sum of factorials
    sum_of_factorials = 0
    
    # Calculate the factorial of each digit and add to the sum
    for digit in num_str:
        digit_int = int(digit)
        sum_of_factorials += factorial(digit_int)
    
    # Check if the sum of factorials equals the original number
    return sum_of_factorials == number

# Sample Input
input_number = 145
if is_strong_number(input_number):
    print("Yes")  # Output: Yes (145 is a strong number)
else:
    print("No")

```

    3. Write a code to generate all amicable numbers in
        the given range
        Sample input: 1 1000
        Sample output: 220 284
        
Here’s the Python code to generate all amicable numbers in a given range:

---

### **What are Amicable Numbers?**

Amicable numbers are two numbers such that the sum of the proper divisors of one number equals the other, and vice versa.

For example:

- **220** and **284** are amicable numbers:
  - Proper divisors of 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 → Sum = 284
  - Proper divisors of 284: 1, 2, 4, 71, 142 → Sum = 220

---

### **Python Code**

```python
def sum_of_divisors(num):
    # Calculate the sum of proper divisors of num
    divisor_sum = 0
    for i in range(1, num // 2 + 1):  # Proper divisors are less than num
        if num % i == 0:
            divisor_sum += i
    return divisor_sum

def find_amicable_numbers(start, end):
    # Find all amicable numbers in the given range
    amicable_pairs = []
    for num in range(start, end + 1):
        # Find the sum of divisors of the current number
        pair = sum_of_divisors(num)
        # Check if the pair is amicable and avoid duplicates
        if pair > num and pair <= end and sum_of_divisors(pair) == num:
            amicable_pairs.append((num, pair))
    return amicable_pairs

# Sample input
start_range = 1
end_range = 1000

# Generate and print amicable numbers
amicable_numbers = find_amicable_numbers(start_range, end_range)
for a, b in amicable_numbers:
    print(a, b)
```

---

### **Explanation**

1. **Sum of Divisors Function (`sum_of_divisors`)**:
   - Finds the proper divisors of a number and calculates their sum.
   - Iterates up to `num // 2` because no proper divisor is greater than half the number.

2. **Find Amicable Numbers**:
   - Iterates through the range `[start, end]`.
   - For each number, calculates its "amicable pair" using the `sum_of_divisors` function.
   - Checks if:
     - The pair’s sum of divisors equals the original number.
     - The pair is larger than the original number (to avoid duplicates).
     - The pair lies within the range.

3. **Output**:
   - Each amicable pair is printed as a separate line.

---

### **Sample Input/Output**

#### Input

```plaintext
1 1000
```

#### Output

```plaintext
220 284
```

Let me know if you'd like further clarification!
