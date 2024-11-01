class Person:
    pass
    def __init__(self, name, id_no):
        self.name =name
        self.id_no = id_no

    def sign_attendance(self):
            print(f"{self.name} has signed attendance")
            return 0
        
class Student(Person):
    pass
        
student = Student("John", 11)
print(student.sign_attendance())