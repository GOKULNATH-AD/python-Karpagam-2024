# Decorators

- In Python, a decorator is a concept that used to add new functionality to an existing function without modifying source-code.
- Some times, it can be used to update class functionality also.

```python
def validate_zero(fn):
    def validate(x,y):
        if y==0:
            return float('inf')
        return fn(x,y)
    return validate
    
@validate_zero
def div(x,y):
    return x/y
```

- Here by default in python, if we do val divide by zero, we will get an ZeroDivisionError.
- Mathematically anything divided by zero suppose to give infinity.
- So here We are giving additional functionality to division function.
- For that we are using a python concept called decorators.
