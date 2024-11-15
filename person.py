class Person:#contains attributes and methods that are common to both students and lecturers
    pass
    def __init__(self, name, role):
        self.name = name
        self.role = role


    def borrow_book(self):
        print(f"{self.name} has borrowed a book")
        return 0


    


