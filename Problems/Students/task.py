class Student:
    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    # calculate the id here
    def make_id(self):
        return self.name[0].upper() + self.last_name + self.birth_year


name1 = input()
last_name1 = input()
birth_year1 = input()
student1 = Student(name1, last_name1, birth_year1)
print(student1.make_id())
