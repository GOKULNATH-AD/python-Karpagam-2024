# slot-01 | day-02

## some in-build function

- In case of strings
  - usage of single, double and triple quotes
  - and `.split()` which is used while getting input values.
  - `"hello"*3` for multiplying strings.

```python
>>> print("Hello my name is {}.".format('doremon'))
```

---

## `comparison operators`

### types

- Equality
- Relational
- Membership
- Identity

---

- `==` Equal To
- `!=` Not Equal To
- `>` Greater Than
- `<` Less Than
- `>=` Greater Than or Equal To
- `<=`  Lesser Than or Equal To
- `in` # checks if given item in sequence
- `not in` # checks if given item not in sequence
- `is` # check if left content `id` is same as right `id`
- `is not` # check if left content `id` is not same as right `id`
- `NOTE :` # we cannot do comparison on complex types.

#### `Lexicographical comparison`

```python
# this means, you can compare strings in python
# How this is working ? 🤔 
# - It will compare each characters ASCII value
print( 'abc' == 'abc' ) # True
print( 'abc' == 'bbc' ) # False
print( 'abc' <= 'bbc' ) # True
```

### `logical operators`

- `and`
- `or`
- `not`

```python
# mostly we use logical operators 
# - to compare multiple conditions like
a = 10
b = 20
c = 30
if not ( a>b and b>=c or a==c ):
   print('condition satisfied')
```

```python
>>> 10 and 20 and 0 and 100 and 200
0
>>> 10 and 20 and [] and 20 and (1,2)
[]

# in above cases. It will convert each and every thing into its boolean type then evaluates. Once it stop evaluation it will through the ans. 
# 10 -> bool(10)  -> True
# 20 -> bool(20)  -> True
# [] -> bool([])  -> False
# 20 -> bool(20)  -> True

# As we are using only `and`. Python will stop once it gets 
# False ( bool([]) -> False ).
# so only we got output as `[]`
```

## MUTABLE AND IMMUTABLE

- Immutable Objects are of in-built datatypes like int, bool, string, Unicode, and tuple. In simple words, an immutable object can’t be changed after it is created.
- Mutable Objects are of type Python list, Python dict, or Python set. Custom classes are generally mutable.
