class MyCustomError(Exception):
   pass

a = 19
try:
    # Code that may raise MyCustomError
    print('hello')
    a = 123423
    raise MyCustomError("An error occurred")
except MyCustomError as e:
    print(e)
