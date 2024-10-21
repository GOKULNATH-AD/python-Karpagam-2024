# slot-01 | day-01

## problem-01

    Write a code to print your 
    name , roll number ,
    CGPA, gender , date of birth

    Sample input: no input
    Sample output:
    Name : Harish
    Roll.no : 12
    CGPA : 7.5
    Gender : M
    Date of birth : 24/9/2000
<!-- 
```python
name = input("Enter your name: ")
roll_no = input("Enter your roll number: ")
cgpa = input("Enter your CGPA: ")
gender = input("Enter your gender (M/F): ")
dob = input("Enter your date of birth (dd/mm/yyyy): ")

print("\nName :", name)
print("Roll.no :", roll_no)
print("CGPA :", cgpa)
print("Gender :", gender)
print("Date of birth :", dob)
``` -->

## problem-02

    Given radius in decimal point ,write a code to find
    the diameter, area and circumference of the circle
    Sample input : 2.3
    Sample output:
    Diameter = 4.6
    Area = 16.610599999999998
    Circumference = 14.443999999999999
    Sample input : 6
    Sample output:
    Diameter = 12.000000
    Area = 113.03999999999999
    Circumference = 37.68
<!-- 
```python
import math

radius = float(input("Enter the radius of the circle: "))

diameter = 2 * radius
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("Diameter =", diameter)
print("Area =", area)
print("Circumference =", circumference)
``` -->

## problem-03

    Given with temperature ‘n’ in Celsius the challenge
    is to convert the given temperature to Fahrenheit
    and display it.
    Sample input : 100.00
    Sample output : 212.0
    Sample input 2: -40
    Sample output: -40.0
<!-- 
```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Fahrenheit =", fahrenheit)
``` -->


## problem-04

    Write a code to convert specified days into years,
    weeks and days.
    Note: Ignore leap year.
    Sample input
    Number of days : 1329
    Sample Output :
    Years: 3
    Weeks: 33
    Days: 3
    5. You are given a
<!-- 
```python
days_input = int(input("Number of days: "))

days_in_year = 365
days_in_week = 7

years = days_input // days_in_year
remaining_days = days_input % days_in_year
weeks = remaining_days // days_in_week
days = remaining_days % days_in_week

print("Years:", years)
print("Weeks:", weeks)
print("Days:", days)
``` -->

## problem-05

    You are given a mobile number that may either:
    ● Have 10 digits (standard mobile number), or
    ● Have 12 digits (including the country code "91").
    
    Your task is to
    
    1. Ignore the country code if it is present. If the
    number has 12 digits, only the last 10 digits (i.e.,
    the actual mobile number) should be considered
    for further processing.

    2. Split the 10-digit mobile number into two parts:
        ○ Left part: The first 5 digits of the 10-digit mobile number.
        ○ Right part: The last 5 digits of the 10-digit mobile number.

    3. Create a new number by swapping the two parts:
        ○ The right part of the number will become
        the left part of the new number.
        ○ The left part of the number will become
        the right part of the new number.

            Sample input: 918765432109
            Sample output: 3210987654
<!-- 
```python
mobile_number = input("Enter the mobile number: ")

if len(mobile_number) == 12 and mobile_number.startswith("91"):
    mobile_number = mobile_number[2:]  # Keep only the last 10 digits

if len(mobile_number) != 10:
    print("Invalid mobile number. Please enter a 10-digit mobile number or a 12-digit number with country code.")
else:
    left_part = mobile_number[:5]  # First 5 digits
    right_part = mobile_number[5:]  # Last 5 digits

    new_number = right_part + left_part

    print(new_number)
``` -->