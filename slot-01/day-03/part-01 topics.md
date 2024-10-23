# SLOT-01 | day-03

## `logical operators`

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

## `Flow control`

### if

### else

### while

### for

### break

### continue

### pass

### conditional operator
