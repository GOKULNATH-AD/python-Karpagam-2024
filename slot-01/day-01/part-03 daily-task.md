# slot-01 | day-01

## task-01

    Write a code that accepts length and breadth of the rectangle
    , the task is to print area and perimeter of the rectangle
    Sample input: 5 2
    Sample output :
    Area : 10
    Perimeter : 14

```python
length, breadth = map(float, input("Enter the length and breadth of the rectangle (separated by space): ").split())

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area :", area)
print("Perimeter :", perimeter)
```

## task-02

    Write a code that converts the given inches to centimeter
    Sample input: 8
    Sample output: 20.32

```python
inches = float(input("Enter the value in inches: "))

centimeters = inches * 2.54

print(centimeters)
```

## task-03

    Write a code that takes number of seconds as the input and
    converts to hh:mm:ss format
    Sample input: 14325
    Sample output: 03:58:45

```python
total_seconds = int(input("Enter the number of seconds: "))

hours = total_seconds // 3600  # 1 hour = 3600 seconds
minutes = (total_seconds % 3600) // 60  # Remaining seconds converted to minutes
seconds = total_seconds % 60  # Remaining seconds

print(f"{hours:02}:{minutes:02}:{seconds:02}")
```

## task-04

    Given n1, n2 where n2 is larger than n1 , your task is to find
    the next multiple of n1 which is greater than n2.
    Sample input: 4 22
    Sample output: 24
    Sample input: 5 27
    Sample output: 30

```python
n1, n2 = map(int, input("Enter two numbers (n1 n2) where n2 > n1: ").split())
next_multiple = (n2 // n1 + 1) * n1
print(next_multiple)
```