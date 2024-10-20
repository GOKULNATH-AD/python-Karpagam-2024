# slot-01 | day-02

## DATATYPES ( string )

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
- `in`
- `not in`
- `is`
- `not is`

`NOTE: make sure you understand your relation`

### `logical operators`

- `and`
- `or`
- `not`

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

- Immutable Objects are of in-built datatypes like int, float, bool, string, Unicode, and tuple. In simple words, an immutable object can’t be changed after it is created.
- Mutable Objects are of type Python list, Python dict, or Python set. Custom classes are generally mutable.
- list
- tuple
- dictionary
- set
