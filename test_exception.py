

try:
    str_value = "string"
    if not str_value.isdigit():
        raise ValueError("Cannot convert to an integer : ", str_value)
    val = int(str_value)
    print(val)
except ValueError as e:
    print("ValueError message: ", e)
finally:
    print("finally code executed...")




# try:
#     val = int("string") # Raise ValueError
#     print(val)
# except ValueError as e:
#     print("Exception: ", e)
# finally:
#     print("finally code executed...")



