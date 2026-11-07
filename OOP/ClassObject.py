class Student:
    def __init__(self):
        self.roll_no = 101
        self.name = "Ponmalar"

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)


s = Student()
s.display()