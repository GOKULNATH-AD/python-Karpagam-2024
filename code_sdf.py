# from flask import Flask 
# from flask_cors import CORS 

# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def index():
#     return "hello world"

# app.run()

# a = 10
# b = 20
# c = a + b

# n = c * (c+1)


try:
    n = int(input("Enter a number: "))
    if n==0:
        res = 34/0 # Raise ZeroDivisionError
        print(res)
    elif n<0:
        li = [1,2,3,4,5]
        print(li[100]) # Raise IndexError
    else:
        val = int("string") # Raise ValueError
        print(val)
except ZeroDivisionError:
    print("ZeroDivisionError")
except IndexError:
    print("IndexError")
except Exception as e:
    print("Exception: ", e)
finally:
    print("finally code executed...")




