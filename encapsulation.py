class Student:
    def __init__(self, marks):
        self.marks = marks
    
    def set_marks(self , value):
        self.__marks= value

    def get_marks(self):
            return self.__marks
        
student = Student(100)
student.set_marks(98)
print(student.get_marks())