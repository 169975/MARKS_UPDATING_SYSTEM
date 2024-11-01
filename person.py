class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Student(Person):
    def __init__(self, name, role):
        super().__init__(name, role)

    def do_exams(self):
        print(f"{self.name}")
        return 0
    
Student= Person("John","student")
print(Student.do_exams())


class Lecturer(Person):
    def __init__(self, name, role):
        super().__init__(name, role)

    def update_marks(self):
        print(f"{self.name}")
        return 0

Lecturer= Person("Paul","Lecturer")
print(Lecturer.update_marks())
