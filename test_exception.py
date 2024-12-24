class Student:
    def __init__(self):
        self._name = "Alice"  # Protected attribute

    def _display(self): # Protected method as it is starting with one underscore.
        print("Student Name:", self._name)  

class Child(Student):
    def show_name(self):
        print("student name",self._name) # accessing inside its child class. ( possible )


obj = Child()
obj.show_name() # Output: Alice
obj._display() # Output: Student Name: Alice
print(obj._name) # Output: Alice