### **Notes on Unit Testing in Python for Students**

---

### **What is Unit Testing?**

- definition: unit testing is a software developement practice that involves testing individual units of code in isolation to ensure they function as expected.

- As a devoper, I want to make sure my code is running properly.
- Usually we will manually test each and every test case.
- Now lets consider you are manually testing every 2 days once. which is annoying.
- Now to write and check our test case automatically.
- We use a technique called unit-testing.
   
---

### **Why Use Unit Testing?**

1. **Catch Errors Early:** Unit tests help catch bugs early in the development process.
2. **Ensure Code Quality:** By testing each function or method, you ensure that your code works as intended.
3. **Automate Testing:** Once tests are written, they can be run automatically, saving time for developers.
4. **Regression Testing:** a type of software testing that ensures that new changes to an application don't break existing functionality.

---

### **Key Components of Unit Testing**

1. **Test Case:** A test case is a single unit of testing. It checks a small unit of functionality in the program, usually a function or method. In Python, you create a test case by subclassing the `unittest.TestCase` class.

2. **Test Method:** A test method is a function that checks a particular functionality. It must begin with the word "test" to be recognized by the `unittest` framework.

3. **Assertions:** Assertions are used to check if the output of the code matches the expected value. Some common assertions include:
   - `assertEqual(a, b)` — Checks if `a` equals `b`
   - `assertNotEqual(a, b)` — Checks if `a` does not equal `b`
   - `assertTrue(x)` — Checks if `x` is True
   - `assertFalse(x)` — Checks if `x` is False
   - `assertRaises(ExceptionType, function, args)` — Checks if a function raises a specific exception

4. **Test Runner:** The test runner is used to execute the tests. In Python, you can use `unittest.main()` to automatically run all the tests defined in a test case class.

---

# `area_of_circle.py`

```python
from math import pi 

def circle_area(r):
    if type(r) not in [int,float]:
        raise ValueError("can only handle int, float datatype.")
    if r<0:
        raise ValueError("neg value cannot be processed")
    return pi * (r * r)
```   
# `circle_area_test.py`

```python
import unittest 
import circle_area as ca
import math 

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # check if basic functionality of area is working...
        self.assertAlmostEqual(ca.circle_area(2), math.pi*(2*2))
        self.assertAlmostEqual(ca.circle_area(4), math.pi*(4*4))
        self.assertAlmostEqual(ca.circle_area(3), math.pi*(3*3))

    def test_area_with_invalid_types(self):
        # check functionality of area with diff invalid datatype.
        self.assertRaises(ValueError,ca.circle_area,-2)
        self.assertRaises(ValueError,ca.circle_area,"2")
        self.assertRaises(ValueError,ca.circle_area,True)
        self.assertRaises(ValueError,ca.circle_area,False)
        self.assertRaises(ValueError,ca.circle_area,[1,2])
        self.assertRaises(ValueError,ca.circle_area,(1,2))

    def test_area_with_valid_types(self):
        # check functionality of area with diff invalid datatype.
        self.assertAlmostEqual(ca.circle_area(4), math.pi*(4*4))
        self.assertAlmostEqual(ca.circle_area(4.5), math.pi*(4.5*4.5))
        
unittest.main()
```
