# slot-01 | day-01

## problem-01

    💡question:
     
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

## problem-02

    💡question:
     
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

## problem-03

    Given with temperature ‘n’ in Celsius the challenge
    is to convert the given temperature to Fahrenheit
    and display it.
    Sample input : 100.00
    Sample output : 212.0
    Sample input 2: -40
    Sample output: -40.0

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

<!-- ```python
def convert_days(total_days):
    # Calculating years, weeks and remaining days
    years = total_days // 365
    remaining_days = total_days % 365
    weeks = remaining_days // 7
    days = remaining_days % 7
    
    return years, weeks, days

# Taking input from the user
total_days = int(input("Number of days: "))

# Getting the conversion result
years, weeks, days = convert_days(total_days)

# Printing the results
print(f"Years: {years}")
print(f"Weeks: {weeks}")
print(f"Days: {days}")
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
def process_mobile_number(mobile_number):
    # Step 1: Check if the number includes a country code (12 digits) and ignore it
    if len(mobile_number) == 12 and mobile_number.startswith("91"):
        mobile_number = mobile_number[2:]
    
    # Step 2: Split the 10-digit number into two parts
    left_part = mobile_number[:5]
    right_part = mobile_number[5:]
    
    # Step 3: Swap the two parts
    new_number = right_part + left_part
    
    return new_number

# Taking input from the user
mobile_number = input("Enter the mobile number: ")

# Getting the processed mobile number
new_mobile_number = process_mobile_number(mobile_number)

# Printing the result
print(f"Processed mobile number: {new_mobile_number}")

``` -->
