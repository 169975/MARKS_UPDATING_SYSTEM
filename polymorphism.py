from abc import ABC, abstractmethod

class Person:#contains attributes and methods that are common to both students and lecturers
    pass
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    @abstractmethod
    def do_exams(self):
        print(f"{self.name} has done exams")
        return 0
    
    #method overriding
class Student2(Person):
    def __init__(self, name, role):
        super().__init__(name, role)

    # def do_exams(self):
    #     print(f"{self.name} has not done exams")
    #     return 0
    
student = Student2("Ken","Student")
print(student.do_exams())

student2 = Student2("Ken1","Student")
print(student.do_exams())
