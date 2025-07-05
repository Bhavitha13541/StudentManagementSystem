class Student:
    def __init__(self,roll_number,name,gender,age,marks):
        self.roll_number = roll_number
        self.name = name
        self.gender = gender
        self.age = age
        self.marks = marks
            
    def __str__(self):
        return f'\n---------------------------------------------------\n\033[36mroll_number = {self.roll_number}\nname = {self.name}\nage = {self.age}\ngender = {self.gender}\nmarks = {self.marks}\033[0m\n---------------------------------------------------\n\n'