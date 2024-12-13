# exception handling

### Basic Notes on `try`, `except`, and `finally` in Python

Python's exception handling mechanism allows you to manage errors gracefully. The `try`, `except`, and `finally` blocks are used to catch and handle exceptions. Here's a breakdown:

#### 1. `try` Block

- The code that might raise an exception is placed inside the `try` block.
- If no exceptions occur, the `except` block is skipped.

#### 2. `except` Block

- This block is executed if an exception occurs in the `try` block.
- You can specify one or more exception types to handle different exceptions separately.

#### 3. `finally` Block

- The `finally` block contains code that will run no matter what.
- It is executed after the `try` and `except` blocks, whether an exception occurred or not.
- It's commonly used for cleanup actions (e.g., closing files or releasing resources).

### Example

```python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if the specific exception occurs
    print("Cannot divide by zero!")
finally:
    # Code that runs no matter what
    print("This runs no matter what.")
```

### Explanation

1. **`try` Block**: The division by zero raises a `ZeroDivisionError`.
2. **`except` Block**: Catches the `ZeroDivisionError` and prints an error message.
3. **`finally` Block**: Runs regardless of whether an exception was raised or not, ensuring that the cleanup code is executed.

### Multiple `except` Blocks

You can have multiple `except` blocks to handle different types of exceptions.

```python
try:
    value = int("abc")
except ValueError:
    print("ValueError: Invalid literal for int()")
except TypeError:
    print("TypeError: Type mismatch")
finally:
    print("Execution completed.")
```

---

## `8-mark`

| **Aspect**               | **Error**                                                                                     | **Exception**                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **Definition**           | Errors are issues in a program that can cause it to stop running.                              | Exceptions are events that can be caught and handled within the program.                   |
| **Handling**             | Usually not handled by the program itself. The program terminates.                            | Can be handled using try-except blocks to allow the program to continue running.           |
| **Examples**             | SyntaxError, IndentationError, MemoryError                                                    | ValueError, IndexError, KeyError, ZeroDivisionError                                        |
| **Source**               | Detected before or during the execution of the program (compile-time or runtime).              | Typically detected during the execution of the program (runtime).                          |

---

## `raise exception`

### Purpose

- Used to manually raise an exception.
- Useful for handling error conditions and custom error reporting.

#### example 01

```python
def fn(x,y):
    if y==0:
        raise ValueError("💀 ZERO Is not possible 💀")
    return x/y 

print(fn(1,0))
```

#### example 02

```python
def calculate_square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return x ** 0.5

try:
    result = calculate_square_root(-5)
except ValueError as e:
    print(e)  # Output: Cannot calculate square root of a negative number
```

## `User-defined-exception`

### Basic Points on User-Defined Exceptions in Python

- User-defined exceptions used to create custom exception
- This can make your error handling more easy
- And your code more readable.

#### Key Points

1. **Purpose**:
   - Provide more meaningful error messages.
   - control over exception handling.

2. **Defining a Custom Exception**:
   - Create a new class that inherits from the built-in `Exception` class or any of its subclasses.

3. **Syntax**:

   ```python
   class MyCustomError(Exception):
       pass
   ```

4. **Raising a Custom Exception**:
   - Use the `raise` keyword to raise the custom exception.

   ```python
   raise MyCustomError("This is a custom error message")
   ```

5. **Catching a Custom Exception**:
   - Use a `try-except` block to handle the custom exception.

   ```python
   try:
       # Code that may raise MyCustomError
       raise MyCustomError("An error occurred")
   except MyCustomError as e:
       print(e)
   ```

6. **Example**:

   ```python
   class NegativeNumberError(Exception):
        pass

   def check_positive(number):
       if number < 0:
           raise NegativeNumberError(number)
       return number

   try:
       check_positive(-5)
   except NegativeNumberError as e:
       print(e)
   ```

   - **Defining the Exception**: `NegativeNumberError` inherits from `Exception` and includes a custom message.
   - **Raising the Exception**: The `check_positive` function raises `NegativeNumberError` if the input number is negative.
   - **Catching the Exception**: The `try-except` block catches the custom exception and prints the error message.
