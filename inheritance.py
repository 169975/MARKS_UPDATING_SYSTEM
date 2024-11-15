class Student:
    def __init__(self, name, id_no):
        self.name =name
        self.id_no = id_no

    def sign_attendance(self):
            print(f"{self.name} has signed attendance")
            return 0


#child class 
class Class_rep(Student):
    pass
        
student = Student("John", 11)
print(student.sign_attendance())