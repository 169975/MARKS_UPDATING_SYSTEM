class Person:#contains attributes and methods that are common to both students and lecturers
    pass
    def __init__(self, name, role):
        self.name = name
        self.role = role


    def do_exams(self):
        print(f"{self.name} has done exams")
        return 0
    
    #method overriding
class Student2(Person):
    pass

    def do_exams(self):
        print(f"{self.name} has not done exams")
        return 0
    
student = Student2("Ken","Student")
print(student.do_exams())
