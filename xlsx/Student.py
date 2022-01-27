class Student:
    schoolName = 'XYZ School' # class attribute

    def __init__(self, name, age):
        self.name=name # instance attribute
        self.age=age # instance attribute

    def print_student(self):
        print("Student: ", self.name, " ", self.age)