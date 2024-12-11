### Basic Notes on File Handling in Python

File handling in Python allows you to work with files—reading, writing, and manipulating them. Python provides built-in functions and methods to handle files efficiently.

---

### File Operations

1. **Opening a File**: Use the `open()` function.
2. **Reading/Writing Data**: Use file methods like `read()`, `write()`, etc.
3. **Closing a File**: Use the `close()` method to free up resources.

---

### File Modes

| **Mode** | **Description**                                         |priority|
|----------|---------------------------------------------------------|--------|
| `'r'`    | Open a file for **reading** (default).                  |high|
| `'w'`    | Open a file for **writing** (overwrites existing data). |high|
| `'a'`    | Open a file for **appending** (data is added to the end).|high|
| `'x'`    | Create a new file; raises an error if the file exists.  |low|
| `'b'`    | Binary mode (e.g., `'rb'` or `'wb'` for binary files).  |low|
| `'t'`    | Text mode (default, e.g., `'rt'` or `'wt'`).            |low|

---

### Common File Handling Methods

#### 1. **Opening and Closing Files**

```python
file = open("example.txt", "r")  # Open file in read mode
print(file.read())              # Read file content
file.close()                    # Close the file
```

#### 2. **Using `with` Statement**

The `with` statement automatically closes the file after the block is executed.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

---

### Reading Files

#### **Read Entire File**

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

#### **Read Line by Line**

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Remove extra newline characters
```

#### **Read Specific Number of Characters**

```python
with open("example.txt", "r") as file:
    content = file.read(10)  # Read first 10 characters
    print(content)
```

#### **Read All Lines into a List**

```python
with open("example.txt", "r") as file:
    lines = file.readlines()  # Returns a list of lines
    print(lines)
```

---

### Writing to Files

#### **Write Over File Content**

```python
with open("example.txt", "w") as file:
    file.write("Hello, World!")
```

#### **Append to Existing File**

```python
with open("example.txt", "a") as file:
    file.write("\nThis is an additional line.")
```

---

### Useful File Methods

| **Method**       | **Description**                                |
|-------------------|-----------------------------------------------|
| `read(size)`      | Reads specified `size` of characters.         |
| `readline()`      | Reads one line from the file.                 |
| `readlines()`     | Reads all lines and returns as a list.        |
| `write(text)`     | Writes `text` to the file.                    |
| `writelines(list)`| Writes a list of strings to the file.         |

---

### Example: Combining Reading and Writing

- copy content from "source.txt" file and paste in new file "destination.txt"

```python
# Read from a file and write its content to another file
with open("source.txt", "r") as source_file:
    content = source_file.read()

with open("destination.txt", "w") as destination_file:
    destination_file.write(content)
```

---
