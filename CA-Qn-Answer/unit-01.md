# TOPICS

## `square root`

## `GCD`

Brute force approach

```python
def find_gcd(x, y):
    gcd = min(x, y)  # Start with the smaller of the two numbers
    
    while True:
        if x % gcd == 0 and y % gcd == 0:
            return gcd
        gcd -= 1  # Decrement and check for the next possible divisor

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = find_gcd(num1, num2)
print("GCD:", gcd)

```

Euclidean algorithm is preferred for efficiency

```python
def find_gcd(a, b):
    while b != 0:
        a = b
        b = a % b
    return a

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))
print("gcd:", find_gcd(x, y))

```

## `LCM`

Brute force approach

- Brute force is nothing but, applying exactly same logic.
- Without using any optimizing technic.

```python
def find_lcm(x, y):
    lcm = max(x, y)
    
    while True:
        if lcm % x == 0 and lcm % y == 0:
            return lcm
        lcm += 1

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = find_lcm(num1, num2)
print("LCM:", lcm)
```

The optimized solution for finding the **LCM (Least Common Multiple)** uses the formula:

![formula for lcm](image-1.png)

Here’s the Python implementation using this formula:

```python
def find_gcd(a, b):
    # Euclidean algorithm to find GCD
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)  # Calculate GCD
    return abs(a * b) // gcd  # Use the LCM formula

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = find_lcm(num1, num2)
print("LCM:", lcm)
```

### Explanation

1. **GCD Calculation**:
   - Uses the **Euclidean algorithm**, which is efficient for finding the GCD of two numbers.

2. **LCM Formula**:
   - The relationship between LCM and GCD ensures we only need one iteration to calculate the LCM.

3. **Absolute Value**:
   - `abs(a * b)` handles any negative numbers, ensuring the result is positive.

---

### Example Execution

For `num1 = 12` and `num2 = 15`:

1. GCD = 3 (calculated using the Euclidean algorithm).
2. LCM = \(\frac{12 \times 15}{3} = 60\).
3. Output: `LCM: 60`.

---

This solution is much faster and avoids unnecessary iterations compared to the brute force method, making it suitable for larger numbers.
