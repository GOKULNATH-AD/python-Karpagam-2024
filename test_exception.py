class Student:
    def __init__(self):
        self.__name = "Alice"  # Private attribute

    def __display(self):  # Private method
        print(f"Student Name: {self.__name}")

    def show_name(self):  # Public method to access private members
        self.__display()

# Accessing private members
s = Student()
# print(s.__name)  # Error: Attribute not accessible directly
# s.__display() # Error: Method not accessible directly
s.show_name()  

'''
output:

Student Name: Alice
'''